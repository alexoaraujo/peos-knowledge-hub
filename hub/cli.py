"""PEOS Knowledge Hub CLI; never mutates external systems."""
import argparse
import json
import sys
from pathlib import Path
from . import catalog

def main(argv=None):
    p = argparse.ArgumentParser(description='PEOS Knowledge Hub (read-only)')
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('stats')
    s=sub.add_parser('search')
    s.add_argument('--query', required=True)
    s.add_argument('--namespace', choices=['canonical','bpd','pmu'])
    s.add_argument('--limit', type=int, default=20)
    c=sub.add_parser('compose')
    c.add_argument('--goal', required=True)
    c.add_argument('--pmu', default=None)
    args=p.parse_args(argv)
    try:
        if args.cmd=='stats': output=catalog.stats()
        elif args.cmd=='search': output=catalog.search(args.query,args.namespace,args.limit)
        else:
            sys.path.insert(0,str(catalog.ROOT/'tools'))
            import peos_engine
            problems=peos_engine.validate()
            if problems:raise ValueError('; '.join(problems))
            output=peos_engine.compose(args.goal,args.pmu)
        print(json.dumps(output,ensure_ascii=False,indent=2))
        return 0
    except ValueError as exc:
        print(str(exc),file=sys.stderr)
        return 2

if __name__=='__main__':
    raise SystemExit(main())
