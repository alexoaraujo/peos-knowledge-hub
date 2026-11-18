#!/usr/bin/env python3
"""Read-only integrity check for the Programação e Design collection.

BPD IDs are local and canonical-prompt references express thematic affinity only.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTION = re.compile(r"^## (\d+)\. ", re.MULTILINE)
ROW = re.compile(r"^\| `(?P<id>BPD-\d{3})` \| \[(?P<title>[^\]]+)\]\(prompts/(?P<file>BPD-\d{3}\.md)\) \|", re.MULTILINE)


def validate(root: Path = ROOT) -> list[str]:
    folder = root / 'colecoes' / 'programacao-design'
    index_path = folder / 'INDEX.md'
    if not index_path.is_file():
        return [f'Missing index: {index_path}']
    data = index_path.read_text(encoding='utf-8')
    errors = []
    sections = [int(x) for x in SECTION.findall(data)]
    if sections != list(range(1, 31)):
        errors.append(f'Expected 30 consecutively numbered sections, found {sections!r}')
    matches = list(ROW.finditer(data))
    ids = [m['id'] for m in matches]
    if len(matches) != 128:
        errors.append(f'Expected 128 BPD index entries, found {len(matches)}')
    if len(set(ids)) != len(ids):
        errors.append('Duplicate local BPD IDs in index')
    expected = [f'BPD-{n:03}' for n in range(1, 129)]
    if ids != expected:
        errors.append('BPD index IDs are missing, reordered or unexpected')
    for match in matches:
        id_ = match['id']
        file_ = match['file']
        if file_ != id_ + '.md':
            errors.append(f'{id_}: incorrect link {file_}')
        path = folder / 'prompts' / file_
        if not path.is_file():
            errors.append(f'{id_}: missing prompt file {path}')
        elif not path.read_text(encoding='utf-8').strip():
            errors.append(f'{id_}: empty prompt file')
    actual = {p.name for p in (folder / 'prompts').glob('BPD-*.md')}
    expected_files = {x + '.md' for x in expected}
    if actual != expected_files:
        extras = sorted(actual - expected_files)
        missing = sorted(expected_files - actual)
        errors.append(f'BPD file set differs; missing={missing}, extras={extras}')
    if 'afinidade de tema, não identidade funcional' not in data:
        errors.append('Missing explicit local-ID / thematic-affinity disclaimer')
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args(argv)
    errors = validate(args.root)
    if errors:
        for error in errors:
            print('FAIL:', error, file=sys.stderr)
        return 1
    print('PASS: 128 BPD entries, 30 sections, links, local IDs and file set')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
