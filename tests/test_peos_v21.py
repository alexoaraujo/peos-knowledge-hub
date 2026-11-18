import hashlib, json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
import peos_engine as pe
class PEOSv21Tests(unittest.TestCase):
 def test_gate(self):self.assertEqual(pe.validate(),[])
 def test_pmu_count(self):self.assertEqual(len(pe.load(ROOT/'pmu/manifest.json')['prompts']),10)
 def test_workflow_count(self):self.assertEqual(len(pe.load(ROOT/'workflows/manifest.json')['workflows']),10)
 def test_universal_fallback(self):self.assertEqual(pe.compose('tarefa técnica não classificada')['pmu_id'],'PMU-001')
 def test_audit_router(self):self.assertEqual(pe.compose('auditoria integral do projeto')['pmu_id'],'PMU-003')
 def test_design_router(self):self.assertEqual(pe.compose('wireframe UX e design')['pmu_id'],'PMU-006')
 def test_no_execution(self):self.assertEqual(pe.compose('deploy release')['execution_status'],'PLAN_ONLY')
 def test_gate_not_faked(self):self.assertTrue(all(x=='NOT_EVALUATED' for x in pe.compose('segurança')['gates'].values()))
 def test_dependencies_pinned(self):
  result=pe.compose('full stack');self.assertTrue(result['canonical_dependencies']);self.assertTrue(all(len(x['sha256'])==64 for x in result['canonical_dependencies']))
 def test_router_rejects_false_positive_embedded_api_word(self):
  self.assertEqual(pe.select('capivara'),[])
  self.assertEqual(pe.select('apicultura'),[])
  self.assertEqual(pe.compose('capivara')['pmu_id'],'PMU-001')
 def test_router_recognizes_api_at_word_boundary(self):
  self.assertIn('PMU-005',pe.select('Criar API REST'))
  self.assertIn('PMU-005',pe.select('API-rest'))
  self.assertIn('PMU-005',pe.select('Criar APIs REST'))
  self.assertIn('PMU-005',pe.select('Integrar full-stack'))
 def test_router_recognizes_auth0_and_rbac(self):
  self.assertIn('PMU-007',pe.select('Configurar Auth0 com RBAC'))
  self.assertIn('PMU-007',pe.select('Implementar OAuth2 e RBAC'))
 def test_router_matches_phrases_with_extra_spaces(self):
  self.assertIn('PMU-005',pe.select('Integração full   stack'))
 def test_router_preserves_existing_specialist_selection(self):
  self.assertEqual(pe.compose('auditoria integral do projeto')['pmu_id'],'PMU-003')
  self.assertEqual(pe.compose('wireframe UX e design')['pmu_id'],'PMU-006')
 def test_unknown_pmu_rejected(self):
  with self.assertRaises(ValueError):pe.compose('teste','PMU-999')
 def test_tamper_detection(self):
  m=pe.load(ROOT/'pmu/manifest.json');p=m['prompts'][0];self.assertEqual(hashlib.sha256((ROOT/p['prompt_path']).read_bytes()).hexdigest(),p['sha256'])
 def test_history_preserved(self):
  a=pe.load(ROOT/'releases/v2.0.0.json');b=pe.load(ROOT/'catalog/manifest.json');self.assertEqual([(p['id'],p['content_sha256']) for p in a['prompts']],[(p['id'],p['content_sha256']) for p in b['prompts']])
