"""Static accessibility and security contracts for read-only PEOS portal."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PORTAL = ROOT / 'hub-portal'


class PortalHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.labels = set()
        self.scripts = []
        self.links = []
        self.skip_links = []
        self.duplicate_ids = set()
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        element_id = values.get('id')
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)
        if tag == 'label' and 'for' in values:
            self.labels.add(values['for'])
        if tag == 'script':
            self.scripts.append(values.get('src'))
        if tag == 'link' and values.get('rel') == 'stylesheet':
            self.links.append(values.get('href'))
        if tag == 'a' and values.get('class') == 'skip-link':
            self.skip_links.append(values.get('href'))


class PortalAccessibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (PORTAL / 'index.html').read_text(encoding='utf-8')
        cls.js = (PORTAL / 'app.js').read_text(encoding='utf-8')
        cls.css = (PORTAL / 'enhancements.css').read_text(encoding='utf-8')
        cls.parser = PortalHTML()
        cls.parser.feed(cls.html)

    def test_accessible_inputs_and_unique_ids(self):
        p = self.parser
        self.assertFalse(p.duplicate_ids)
        self.assertTrue({'q', 'ns', 'sort', 'category', 'group', 'tag'}.issubset(p.labels))
        self.assertTrue({'results', 'result-count', 'clear', 'more', 'load-error', 'retry'}.issubset(p.ids))
        self.assertIn('#catalog-results', p.skip_links)
        self.assertIn('aria-live="polite"', self.html)

    def test_assets_are_local_and_present(self):
        self.assertEqual(self.parser.scripts, ['search.js', 'app.js', 'plan-preview.js'])
        self.assertIn('enhancements.css', self.parser.links)
        for asset in self.parser.scripts + self.parser.links:
            self.assertTrue((PORTAL / asset).is_file(), asset)

    def test_untrusted_catalog_data_never_used_as_html(self):
        self.assertNotIn('innerHTML', self.js)
        self.assertNotIn('insertAdjacentHTML', self.js)
        self.assertIn('textContent', self.js)
        self.assertIn('safePromptPath', self.js)
        self.assertIn("s === '..'", self.js)

    def test_pmu_references_remain_local_and_fail_closed(self):
        self.assertIn("fetch('../pmu/manifest.json')", self.js)
        self.assertIn("pmuReferenceState = 'error'", self.js)
        self.assertIn("safePromptPath(item.path)", self.js)
        self.assertIn("Referências canônicas indisponíveis", self.js)
        self.assertIn("SHA-256: ", self.js)
        self.assertIn(".item details summary:focus-visible", self.css)

    def test_plan_preview_has_accessible_controls_and_no_execution(self):
        self.assertTrue({'plan-goal', 'plan-pmu'}.issubset(self.parser.labels))
        self.assertTrue({'plan-form', 'plan-submit', 'plan-message', 'plan-output'}.issubset(self.parser.ids))
        self.assertIn('id="plan-message" role="status"', self.html)
        preview = (PORTAL / 'plan-preview.js').read_text(encoding='utf-8')
        self.assertNotIn('innerHTML', preview)
        self.assertNotIn('insertAdjacentHTML', preview)
        self.assertIn("PLAN_ONLY", preview)
        self.assertIn("BLOCKED_UNTIL_VERIFIED", preview)
        self.assertIn("pmuSelect.disabled = true", preview)
        self.assertIn("fetch('../workflows/manifest.json')", preview)
        self.assertIn("fetch('../pmu/manifest.json')", preview)
        self.assertNotIn('eval(', preview)
        self.assertNotIn('new Function(', preview)

    def test_progressive_loading_and_responsive_states(self):
        self.assertIn('PAGE_SIZE = 40', self.js)
        self.assertIn('showMore()', self.js)
        self.assertIn('Nenhum prompt encontrado.', self.js)
        self.assertIn('prefers-reduced-motion', self.css)
        self.assertIn('@media(max-width:640px)', self.css)


if __name__ == '__main__':
    unittest.main()
