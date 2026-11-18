#!/usr/bin/env python3
"""PEOS deterministic composition engine (stdlib-only). Produces plans, never executes infrastructure changes."""
from pathlib import Path
import argparse, hashlib, json, re, sys, unicodedata
ROOT=Path(__file__).resolve().parents[1]
def load(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def norm(s):
 s=unicodedata.normalize('NFKD',s.lower())
 return ''.join(c for c in s if not unicodedata.combining(c))
KEYWORDS={
 'PMU-002':['criar projeto','novo projeto','do zero','mvp','requisitos','planejamento'],
 'PMU-003':['auditoria','auditar','revisar integral','diagnostico','360'],
 'PMU-004':['continuar','continue','retomar','pendencias','proximo gate'],
 'PMU-005':['full stack','frontend','backend','api','implementar modulo'],
 'PMU-006':['design','ux','ui','wireframe','acessibilidade','prototipo'],
 'PMU-007':['seguranca','compliance','rbac','rls','auth','auth0','ameaca'],
 'PMU-008':['dados','data pipeline','machine learning','inteligencia artificial','llm'],
 'PMU-009':['devops','sre','deploy','release','ci/cd','observabilidade'],
 'PMU-010':['migracao','modernizacao','legado','refatorar','cutover']}
def validate():
 m=load(ROOT/'pmu/manifest.json');w=load(ROOT/'workflows/manifest.json');canonical=load(ROOT/'catalog/manifest.json')
 ids={x['id'] for x in canonical['prompts']};pmus={x['id'] for x in m['prompts']};errors=[]
 if len(ids)!=659 or canonical['library_version']!='2.1.0':errors.append('baseline canônica inesperada')
 if len(pmus)!=10 or len(m['prompts'])!=10:errors.append('PMUs ausentes/duplicados')
 for p in m['prompts']:
  path=ROOT/p['prompt_path']
  if not path.is_file():errors.append('PMU ausente: '+p['id']);continue
  if hashlib.sha256(path.read_bytes()).hexdigest()!=p['sha256']:errors.append('hash PMU divergente: '+p['id'])
  if len(p['refs'])!=len(set(p['refs'])) or set(p['refs'])-ids:errors.append('referência canônica inválida: '+p['id'])
  if not p['stages']:errors.append('etapas ausentes: '+p['id'])
 if len(w['workflows'])!=10:errors.append('workflows incompletos')
 for wf in w['workflows']:
  if wf['pmu_id'] not in pmus:errors.append('workflow com PMU inexistente')
  if load(ROOT/'workflows'/(wf['id']+'.json'))!=wf:errors.append('workflow alterado: '+wf['id'])
  if not wf['steps'] or any(not s['evidence_required'] for s in wf['steps']):errors.append('workflow sem gate de evidência')
 prev=load(ROOT/'releases/v2.0.0.json')
 old={x['id']:(x['content_sha256'],x['category']) for x in prev['prompts']}
 now={x['id']:(x['content_sha256'],x['category']) for x in canonical['prompts']}
 if old!=now:errors.append('regressão de ID/hash/categoria canônicos')
 return errors
def keyword_matches(normalized_query, keyword):
 """Match whole words/phrases, never arbitrary substrings (e.g. api in capivara)."""
 pattern = r'(?<!\w)' + re.escape(norm(keyword)).replace(r'\ ', r'\s+') + r'(?!\w)'
 return re.search(pattern, normalized_query) is not None
def select(query):
 q=norm(query);rank=[]
 for pid,words in KEYWORDS.items():
  score=sum(3 if ' ' in word else 1 for word in words if keyword_matches(q,word))
  if score:rank.append((score,pid))
 return [p for _,p in sorted(rank,key=lambda x:(-x[0],x[1]))]
def compose(query,preferred=None):
 m=load(ROOT/'pmu/manifest.json');byid={x['id']:x for x in m['prompts']}
 if preferred and preferred not in byid:raise ValueError('PMU desconhecido')
 ranked=select(query);chosen=preferred or (ranked[0] if ranked else 'PMU-001')
 p=byid[chosen];canonical={x['id']:x for x in load(ROOT/'catalog/manifest.json')['prompts']}
 return {'library_version':'2.1.0','request':query,'pmu_id':chosen,'pmu_version':p['version'],'pmu_sha256':p['sha256'],
  'routing':{'method':'deterministic-keyword','candidates':ranked,'confidence':'heuristic-not-semantic-validation'},
  'canonical_dependencies':[{'id':i,'content_version':canonical[i]['content_version'],'sha256':canonical[i]['content_sha256']} for i in p['refs']],
  'workflow_id':'WF-'+chosen.split('-')[1],
  'steps':[{'name':s,'status':'NOT_STARTED','evidence':None,'gate':'BLOCKED_UNTIL_VERIFIED'} for s in p['stages']],
  'execution_status':'PLAN_ONLY','permissions':'NO_EXTERNAL_MUTATIONS','gates':{f'G{i}':'NOT_EVALUATED' for i in range(7)},
  'notes':['Plano gerado sem execução de ferramentas externas.','Requer avaliação de contexto, autorização e evidências reais.']}
def main():
 ap=argparse.ArgumentParser();sub=ap.add_subparsers(dest='cmd',required=True)
 sub.add_parser('validate');c=sub.add_parser('compose');c.add_argument('--goal',required=True);c.add_argument('--pmu',default=None);c.add_argument('--output',default=None)
 args=ap.parse_args()
 if args.cmd=='validate':
  errors=validate();print('PASS: motor, 10 PMUs, 10 workflows e 659 hashes preservados' if not errors else '\n'.join(errors));return bool(errors)
 errors=validate()
 if errors:print('\n'.join(errors),file=sys.stderr);return 1
 try:out=compose(args.goal,args.pmu)
 except ValueError as exc:print(str(exc),file=sys.stderr);return 2
 result=json.dumps(out,ensure_ascii=False,indent=2)+'\n'
 if args.output:Path(args.output).write_text(result,encoding='utf-8')
 else:print(result,end='')
 return 0
if __name__=='__main__':sys.exit(main())
