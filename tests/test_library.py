"""Testes comportamentais: baseline, adulterações, IDs e release."""
import json, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import library

class IntegrityTests(unittest.TestCase):
    def run_cli(self,base,*args):
        return subprocess.run([sys.executable,str(base/'tools'/'library.py'),*args],
                              cwd=base,text=True,capture_output=True,check=False)
    def test_historical_baseline(self):
        data=library.historical_audit()
        self.assertEqual((data['v1_0_count'],data['v1_1_count'],data['preserved_ids']), (273,647,273))
        self.assertEqual(data['removed_ids'], [])
        self.assertEqual(data['unexpected_content_changes'], [])
        self.assertEqual(set(data['renamed']), {'1102','1506','2009'})
    def test_manifest_integrity(self):
        self.assertEqual(library.validate(),[])
    def test_index_determinism(self):
        self.assertEqual(library.write_indexes(library.load(library.MANIFEST),
               (library.SOURCES/'Biblioteca_Mestre_Prompts_TI_v1.1.md').read_text(),check=True),[])
    def copy_repo(self):
        tmp=tempfile.TemporaryDirectory()
        base=Path(tmp.name)/'repository';shutil.copytree(ROOT,base)
        self.addCleanup(tmp.cleanup)
        return base
    def test_tamper_prompt_is_blocked(self):
        base=self.copy_repo()
        p=base/'prompts'/'0700-0799'/'0711.md'
        p.write_text(p.read_text(encoding='utf-8')+'\nTentativa de alteração silenciosa.\n',encoding='utf-8')
        r=self.run_cli(base,'validate')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('hash divergente: 0711',r.stdout)
    def test_deleted_id_is_blocked(self):
        base=self.copy_repo()
        (base/'prompts'/'0700-0799'/'0711.md').unlink()
        r=self.run_cli(base,'validate')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('arquivo ausente: 0711',r.stdout)
    def test_duplicate_id_is_blocked(self):
        base=self.copy_repo()
        m=base/'catalog'/'manifest.json';doc=json.loads(m.read_text(encoding='utf-8'))
        doc['prompts'].append(dict(doc['prompts'][0]));m.write_text(json.dumps(doc,ensure_ascii=False))
        r=self.run_cli(base,'validate')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('ID duplicado:',r.stdout)
    def test_stage_with_reason_creates_versioned_snapshot(self):
        base=self.copy_repo()
        p=base/'prompts'/'0700-0799'/'0711.md'
        p.write_text(p.read_text(encoding='utf-8')+'\n<!-- Atualização editorial testada. -->\n',encoding='utf-8')
        r=self.run_cli(base,'stage','--version','2.1.1','--reason','teste controlado')
        self.assertEqual(r.returncode,0,r.stderr+r.stdout)
        self.assertIn('alterados=1',r.stdout)
        self.assertTrue((base/'releases'/'v2.1.1.json').is_file())
        rr=self.run_cli(base,'validate');self.assertEqual(rr.returncode,0,rr.stdout+rr.stderr)
    def test_complementary_collection_integrity(self):
        import collections_integration
        self.assertEqual(collections_integration.validate(),[])
        m=collections_integration.load(collections_integration.MANIFEST)
        self.assertEqual((len(m['entries']),len(m['sections'])),(128,30))
        self.assertEqual(len([x for x in m['entries'] if x['coverage']=='potential_gap']),11)
        self.assertEqual(len({x['id'] for x in m['entries']}),128)

    def test_complementary_collection_tamper_blocked(self):
        base=self.copy_repo()
        p=base/'colecoes'/'programacao-design'/'prompts'/'BPD-052.md'
        p.write_text(p.read_text(encoding='utf-8')+'\nALTERAÇÃO NÃO VERSIONADA\n',encoding='utf-8')
        r=self.run_cli(base,'validate')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('entrada divergente do original ou hash: BPD-052',r.stdout)

    def test_complementary_collection_deleted_source_blocked(self):
        base=self.copy_repo()
        (base/'originais'/'Biblioteca-de-Prompts-para-Programação-e-Design.txt').unlink()
        r=self.run_cli(base,'validate')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('manifesto/fonte da coleção ausente',r.stdout)

    def test_complementary_collection_mismatched_reference_blocked(self):
        base=self.copy_repo()
        p=base/'colecoes'/'programacao-design'/'manifest.json'
        data=json.loads(p.read_text(encoding='utf-8'))
        data['entries'][0]['related_canonical_ids'].append('9999')
        p.write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
        r=self.run_cli(base,'validate')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('link a ID canônico ausente: BPD-001',r.stdout)

    def test_v2_catalogue_has_exact_new_ux_ids(self):
        m=library.load(library.MANIFEST)
        now={p['id'] for p in m['prompts']}
        old={p['id'] for p in library.load(library.RELEASES/'v1.1.0.json')['prompts']}
        self.assertEqual(len(now),659)
        self.assertEqual(now-old,{f'{i:04d}' for i in range(3601,3613)})
        self.assertEqual(old-now,set())
    def test_v2_contracts_tamper_is_blocked(self):
        base=self.copy_repo()
        f=base/'contracts'/'3603.json'
        d=json.loads(f.read_text(encoding='utf-8'));d['content_sha256']='0'*64
        f.write_text(json.dumps(d,ensure_ascii=False),encoding='utf-8')
        r=self.run_cli(base,'validate')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('contrato divergente 3603/content_sha256',r.stdout)
    def test_v2_snapshot_rollback_is_blocked(self):
        base=self.copy_repo()
        f=base/'releases'/'v2.0.0.json'
        d=json.loads(f.read_text(encoding='utf-8'))
        d['prompts']=[x for x in d['prompts'] if x['id']!='0404']
        d['total_prompts']-=1
        f.write_text(json.dumps(d,ensure_ascii=False),encoding='utf-8')
        r=self.run_cli(base,'validate')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('IDs removidos entre releases',r.stdout)
    def test_v2_contracts_complete(self):
        sys.path.insert(0,str(ROOT/'tools'))
        import v2_contracts
        self.assertEqual(v2_contracts.validate_contracts(),[])
        m=library.load(library.MANIFEST)
        self.assertEqual(len(list((ROOT/'contracts').glob('*.json'))),m['total_prompts'])

    def test_init_blocked_without_force(self):
        r=self.run_cli(ROOT,'init')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('Manifesto já existe',r.stderr)
    def test_stage_requires_reason(self):
        r=self.run_cli(ROOT,'stage','--version','2.1.1','--reason','')
        self.assertNotEqual(r.returncode,0)
        self.assertIn('Motivo',r.stderr)

if __name__=='__main__':unittest.main()
