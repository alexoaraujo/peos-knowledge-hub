"""Unified read-only views over the versioned upstream manifests."""
from __future__ import annotations
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_json(name: str, root: Path = ROOT):
    return json.loads((root / name).read_text(encoding="utf-8"))

def entries(root: Path = ROOT) -> list[dict]:
    canonical = read_json('catalog/manifest.json', root)['prompts']
    bpd = read_json('colecoes/programacao-design/manifest.json', root)['entries']
    pmu = read_json('pmu/manifest.json', root)['prompts']
    result = []
    for p in canonical:
        result.append({'id': p['id'], 'namespace': 'canonical', 'title': p['title'],
                       'group': p.get('group'), 'category': p.get('category'),
                       'path': p['content_path'], 'sha256': p['content_sha256'],
                       'status': p['status'], 'tags': p.get('tags', [])})
    for p in bpd:
        result.append({'id': p['id'], 'namespace': 'bpd', 'title': p['title'],
                       'group': p.get('group_suggested'), 'category': p.get('category_suggested'),
                       'path': p['content_path'], 'sha256': p['content_sha256'],
                       'status': p['review_status'], 'tags': []})
    for p in pmu:
        result.append({'id': p['id'], 'namespace': 'pmu', 'title': p['name'],
                       'group': None, 'category': 'Prompt Mestre Unificado',
                       'path': p['prompt_path'], 'sha256': p['sha256'],
                       'status': p['status'], 'tags': [p['kind']]})
    return result

def normalize(s: str) -> str:
    t = unicodedata.normalize('NFKD', s.lower())
    return ''.join(c for c in t if not unicodedata.combining(c))

def search(query: str, namespace: str | None = None, limit: int = 20, root: Path = ROOT) -> list[dict]:
    if namespace is not None and namespace not in ('canonical', 'bpd', 'pmu'):
        raise ValueError('Unknown namespace')
    if not 1 <= limit <= 1000:
        raise ValueError('limit must be 1..1000')
    words = list(dict.fromkeys(re.findall(r'\w+', normalize(query))))
    ranked = []
    for p in entries(root):
        if namespace and p['namespace'] != namespace:
            continue
        title = normalize(p['title'])
        category = normalize(p.get('category') or '')
        corpus = normalize(' '.join([p['id'], p['title'], p.get('category') or '',
                                    p.get('group') or '', ' '.join(p.get('tags') or [])]))
        if words and not all(w in corpus for w in words):
            continue
        score = sum((12 if w in normalize(p['id']) else 0) + (5 if w in title else 0) +
                    (2 if w in category else 0) for w in words)
        ranked.append((-score, p['id'], p))
    return [r[-1] for r in sorted(ranked)[:limit]]

def stats(root: Path = ROOT) -> dict:
    es = entries(root)
    return {'total_prompts': len(es), 'by_namespace': {n:sum(p['namespace']==n for p in es)
            for n in ('canonical', 'bpd', 'pmu')},
            'total_workflows':len(read_json('workflows/manifest.json',root)['workflows']),
            'library_version':read_json('catalog/manifest.json',root)['library_version']}
