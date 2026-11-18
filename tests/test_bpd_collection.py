"""Behavioral tests for local BPD index integrity; no canonical files modified."""
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validate_bpd_collection', ROOT / 'tools' / 'validate_bpd_collection.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class BPDCollectionTests(unittest.TestCase):
    def test_original_index_passes(self):
        self.assertEqual(mod.validate(ROOT), [])

    def test_duplicate_bpd_id_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)
            shutil.copytree(ROOT / 'colecoes' / 'programacao-design', path / 'colecoes' / 'programacao-design')
            index = path / 'colecoes' / 'programacao-design' / 'INDEX.md'
            data = index.read_text(encoding='utf-8')
            index.write_text(data.replace('`BPD-002` |', '`BPD-001` |', 1), encoding='utf-8')
            self.assertTrue(mod.validate(path))

    def test_missing_bpd_file_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)
            shutil.copytree(ROOT / 'colecoes' / 'programacao-design', path / 'colecoes' / 'programacao-design')
            (path / 'colecoes' / 'programacao-design' / 'prompts' / 'BPD-065.md').unlink()
            self.assertTrue(any('BPD-065' in e for e in mod.validate(path)))

    def test_affinity_disclaimer_required(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)
            shutil.copytree(ROOT / 'colecoes' / 'programacao-design', path / 'colecoes' / 'programacao-design')
            index = path / 'colecoes' / 'programacao-design' / 'INDEX.md'
            index.write_text(index.read_text(encoding='utf-8').replace('afinidade de tema, não identidade funcional', 'equivalência funcional'), encoding='utf-8')
            self.assertTrue(any('affinity' in e for e in mod.validate(path)))
