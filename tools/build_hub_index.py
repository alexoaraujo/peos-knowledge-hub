#!/usr/bin/env python3
"""Build a reproducible, read-only browser index using Python stdlib."""
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from hub.catalog import ROOT, entries, stats

TARGET=ROOT/'hub-portal/catalog.json'
def build():
    return json.dumps({'schema_version':'1.0.0','summary':stats(), 'entries':entries()},
                      ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n'
def main(argv=None):
    ap=argparse.ArgumentParser()
    ap.add_argument('--check',action='store_true')
    args=ap.parse_args(argv)
    data=build()
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding='utf-8')!=data:
            print('FAIL: hub index not reproducible',file=sys.stderr);return 1
        print('PASS: deterministic hub index');return 0
    TARGET.write_text(data,encoding='utf-8')
    print('Wrote:',TARGET)
    return 0
if __name__=='__main__':raise SystemExit(main())
