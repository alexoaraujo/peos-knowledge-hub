import hashlib, json, subprocess, sys, unittest
from pathlib import Path
from hub import catalog

ROOT=Path(__file__).resolve().parents[1]
class HubTests(unittest.TestCase):
    def test_counts_and_unique_ids(self):
        s=catalog.stats();self.assertEqual(s['total_prompts'],797)
        self.assertEqual(s['by_namespace'],{'canonical':659,'bpd':128,'pmu':10})
        self.assertEqual(s['total_workflows'],10)
        es=catalog.entries();self.assertEqual(len({(e['namespace'],e['id']) for e in es}),797)
    def test_search_accent_insensitive(self):
        results=catalog.search('seguranca',limit=1000)
        self.assertTrue(results)
        self.assertTrue(any('Segurança' in p['title'] or 'Segurança' in (p.get('category') or '') for p in results))
    def test_namespace_isolation(self):
        self.assertTrue(all(x['namespace']=='pmu' for x in catalog.search('',namespace='pmu')))
        with self.assertRaises(ValueError):catalog.search('teste',namespace='invalid')
    def test_hashes_of_all_entries(self):
        for x in catalog.entries():
            q=ROOT/x['path'];self.assertTrue(q.is_file(),x['id'])
            self.assertEqual(hashlib.sha256(q.read_bytes()).hexdigest(),x['sha256'],x['id'])
    def test_agent_manifest_references(self):
        d=catalog.read_json('agents/manifest.json')['agents']
        self.assertEqual(len(d),10)
        pmus={p['id'] for p in catalog.read_json('pmu/manifest.json')['prompts']}
        wfs={w['id'] for w in catalog.read_json('workflows/manifest.json')['workflows']}
        for a in d:
            self.assertIn(a['pmu_id'],pmus);self.assertIn(a['workflow_id'],wfs)
            self.assertEqual(a['permissions'],[])
            self.assertEqual(a['execution_mode'],'PLAN_ONLY')
    def test_generated_index_is_reproducible(self):
        completed=subprocess.run([sys.executable,'tools/build_hub_index.py','--check'],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(completed.returncode,0,completed.stdout+completed.stderr)
    def test_cli_compose_is_not_execution(self):
        completed=subprocess.run([sys.executable,'-m','hub.cli','compose','--goal','Criar Projeto PEOS Knowledge Hub'],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(completed.returncode,0,completed.stdout+completed.stderr)
        p=json.loads(completed.stdout)
        self.assertEqual(p['pmu_id'],'PMU-002')
        self.assertEqual(p['execution_status'],'PLAN_ONLY')
        self.assertEqual(p['permissions'],'NO_EXTERNAL_MUTATIONS')
        self.assertTrue(all(v=='NOT_EVALUATED' for v in p['gates'].values()))
    def test_registry(self):
        r=catalog.read_json('provenance/sources.json')
        self.assertEqual(len(r['sources']),3)
        self.assertTrue(all(len(x['archive_sha256'])==64 for x in r['sources']))
