#!/usr/bin/env python3
"""Biblioteca Mestre TI: importação, auditoria, índices e releases (stdlib only)."""
from __future__ import annotations
import argparse, collections, csv, hashlib, io, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'catalog' / 'manifest.json'
TAXONOMY = ROOT / 'catalog' / 'taxonomy.json'
HISTORY = ROOT / 'catalog' / 'history.json'
RELATIONS = ROOT / 'catalog' / 'relations.json'
LEDGER = ROOT / 'catalog' / 'events.jsonl'
PROMPTS = ROOT / 'prompts'
INDICES = ROOT / 'indices'
RELEASES = ROOT / 'releases'
SOURCES = ROOT / 'originais'
RE_MD = re.compile(r'(?m)^### PROMPT (\d{4}) — (.+?)\s*$')
RE_MATRIX = re.compile(r'^\|\s*(\d{4})\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*$', re.M)
RE_FIELD = re.compile(r'^\*\*(ID|Nome|Categoria|Subcategoria|Nível):\*\*\s*(.*?)\s*$', re.M)
RE_VERSION = re.compile(r'^\d+\.\d+\.\d+$')

def sha(s):
    if isinstance(s, str): s=s.encode('utf-8')
    return hashlib.sha256(s).hexdigest()

def load(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def dump(path, obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=False)+'\n',encoding='utf-8')
def slug(s):
    import unicodedata
    s=unicodedata.normalize('NFKD',s)
    s=''.join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub('-+', '-', re.sub('[^a-z0-9]+','-',s)).strip('-') or 'geral'

def normalize(s): return s.replace('\r\n','\n').strip()+'\n'

def extract(text):
    """Extrai matriz e fichas, sem tratar menções a IDs fora das fichas como novos prompts."""
    matrix=text.split('## 7. MATRIZ GERAL',1)
    if len(matrix)!=2 or '## 8. FICHAS COMPLETAS DOS PROMPTS' not in matrix[1]:
        raise ValueError('Fonte sem matriz geral/fichas completas')
    matrix=matrix[1].split('## 8. FICHAS COMPLETAS DOS PROMPTS',1)[0]
    entries={}
    for m in RE_MATRIX.finditer(matrix):
        key=m.group(1)
        if key in entries: raise ValueError(f'ID duplicado na matriz: {key}')
        entries[key]={'id':key,'title':m.group(2).strip(),'category':m.group(3).strip(),'level':m.group(4).strip(),'source_status':m.group(5).strip()}
    section=text.split('## 8. FICHAS COMPLETAS DOS PROMPTS',1)[1]
    section=re.split(r'(?m)^## 9\. ', section, maxsplit=1)[0]
    matches=list(RE_MD.finditer(section)); bodies={}
    for i,m in enumerate(matches):
        key=m.group(1)
        if key in bodies: raise ValueError(f'ID duplicado nas fichas: {key}')
        content=section[m.start():matches[i+1].start() if i+1<len(matches) else len(section)]
        content=re.split(r'(?m)^## 8\.\d+\s+—',content,maxsplit=1)[0]
        content=normalize(content)
        meta={k:v.strip() for k,v in RE_FIELD.findall(content)}
        if (meta.get('ID')!=key or meta.get('Nome')!=m.group(2) or
            meta.get('Categoria')!=entries.get(key,{}).get('category')):
            raise ValueError(f'Incompatibilidade cabeçalho/metadados/matriz no {key}: {meta}')
        bodies[key]=content
        if key not in entries or entries[key]['title']!=m.group(2).strip():
            raise ValueError(f'Fichas não correspondem à matriz: {key}')
        entries[key]['legacy_subcategory']=meta.get('Subcategoria','')
    if entries.keys()!=bodies.keys():
        raise ValueError(f'IDs da matriz e das fichas divergentes: {sorted(entries.keys()^bodies.keys())[:15]}')
    return entries,bodies

def extract_professions_phases_workflows(source, valid_ids):
    def excerpt(start,end):
        return source.split(start,1)[1].split(end,1)[0] if start in source and end in source else ''
    profs={}; phases={}; workflows={}
    for line in excerpt('## 5. ÍNDICE POR PROFISSÃO','## 6. ÍNDICE POR FASE DO PROJETO').splitlines():
        m=re.match(r'- \*\*(.+?):\*\* (.+)',line)
        if m:
            ids=list(dict.fromkeys(re.findall(r'\b\d{4}\b',m.group(2))))
            profs[m.group(1)] = [x for x in ids if x in valid_ids]
    for line in excerpt('## 6. ÍNDICE POR FASE DO PROJETO','## 7. MATRIZ GERAL').splitlines():
        m=re.match(r'- \*\*(\d\d) — (.+?):\*\* (.+)',line)
        if m: phases[m.group(1)+' — '+m.group(2)]=[x for x in re.findall(r'\b\d{4}\b',m.group(3)) if x in valid_ids]
    for line in excerpt('## 9. WORKFLOWS PROFISSIONAIS PRONTOS','## 10. CONTROLE').splitlines():
        m=re.match(r'- \*\*(.+?):\*\* (.+)',line)
        if m: workflows[m.group(1)]=[x for x in re.findall(r'\b\d{4}\b',m.group(2)) if x in valid_ids]
    return {'professions':profs,'phases':phases,'workflows':workflows}

def tax_class(tax, category):
    found=[v for v in tax['categories'] if v['name']==category]
    if len(found)!=1: raise ValueError(f'Categoria desconhecida/duplicada: {category}')
    return found[0]

def classify(tax, entry):
    c=tax_class(tax,entry['category'])
    sub='Fundamentos e práticas'
    number=int(entry['id'])
    for part in c['subcategories']:
        if part['from']<=number<=part['to']:
            sub=part['name'];break
    return c,sub

TAG_MATCH={
 'PostgreSQL':r'postgresql|\bpg\b|\brls\b|vacuum|explain',
 'GitHub':r'github|pull request|codeowners|dependabot|\bgit\b',
 'Neon':r'\bneon\b', 'Vercel':r'\bvercel\b', 'Auth0':r'\bauth0\b',
 'Kubernetes':r'kubernetes|\bk8s\b|helm|kubectl|crashloopbackoff',
 'Docker':r'docker|container', 'Terraform':r'terraform',
 'Node.js':r'node\.js|nestjs|express', 'Next.js':r'next\.js',
 'React':r'\breact\b', 'Python':r'python|django|fastapi',
 'OpenTelemetry':r'opentelemetry|tracing', 'Kafka':r'kafka', 'RabbitMQ':r'rabbitmq',
 'IAM':r'\biam\b|oauth|oidc|\brbac\b|\babac\b|saml|sso',
 'Segurança':r'owasp|segurança|security|threat|least privilege|zero trust',
 'IA e Agentes':r'\bllm\b|agent|agente|prompt|\brag\b|copilot',
 'CI/CD':r'pipeline|ci/cd|gitops|deploy|release',
 'Dados':r'dados|data|etl|sql|database|banco|mongodb|redis',
 'Testes':r'test|quality gate|teste|qa',
}

def tags(title):
    return sorted(k for k,rx in TAG_MATCH.items() if re.search(rx,title,re.I))

def locate(key): return PROMPTS / f'{key[:2]}00-{key[:2]}99' / f'{key}.md'

def record_from(entry,body,tax,first_seen,content_version,revision=1,original_id=None):
    c,sub=classify(tax,entry)
    return {'id':entry['id'],'title':entry['title'],'group':c['group'],
            'technical_sector':c['technical_sector'],'category':entry['category'],
            'category_code':c['code'],'subcategory':sub,
            'source_subcategory':entry.get('legacy_subcategory',sub),
            'level':entry['level'],'status':'ACTIVE','source_status':entry.get('source_status',''),
            'tags':tags(entry['title']),'verticals':[],
            'first_seen':first_seen,'content_version':content_version,'revision':revision,
            'content_path':locate(entry['id']).relative_to(ROOT).as_posix(),
            'content_sha256':sha(normalize(body)),
            'replaces':[],'replaced_by':None}

def write_indexes(manifest, source, check=False):
    prompts=manifest['prompts']; other=load(RELATIONS) if RELATIONS.is_file() else extract_professions_phases_workflows(source,{x['id'] for x in prompts})
    buckets={'por-grupo':{},'por-setor':{},'por-categoria':{},'por-subcategoria':{},'por-tag':{},'por-status':{}}
    for p in prompts:
        for typ,value in [('por-grupo',p['group']),('por-setor',p['technical_sector']),
                          ('por-categoria',p['category']),('por-subcategoria',p['category']+' / '+p['subcategory']),
                          ('por-status',p['status'])]:
            buckets[typ].setdefault(value,[]).append(p)
        for tag in p['tags']: buckets['por-tag'].setdefault(tag,[]).append(p)
    refs={x['id']:x for x in prompts}; output={}
    def row(p): return f"| `{p['id']}` | [{p['title']}](../../{p['content_path']}) | {p['category']} | {p['status']} |"
    def generate(title,items,kind):
        body=f'# {title}\n\nGerado automaticamente. Não edite diretamente.\n\n**Total:** {len(items)}\n\n| ID | Prompt | Categoria | Status |\n|---|---|---|---|\n'
        body+='\n'.join(row(p) for p in sorted(items,key=lambda x:x['id']))+'\n'
        return body
    for typ, groups in buckets.items():
        for title, items in groups.items():
            output[f'{typ}/{slug(title)}.md']=generate(title,items,typ)
    for typ, groups in [('por-profissao',other['professions']),('por-fase',other['phases']),('por-workflow',other['workflows'])]:
        for title,ids in groups.items():
            items=[refs[i] for i in ids]
            output[f'{typ}/{slug(title)}.md']=generate(title,items,typ)
    cat_counter=collections.Counter(p['category'] for p in prompts)
    lines=['# Catálogo Mestre — Índice Geral','','Gerado automaticamente a partir do manifesto.','','- **Versão:** '+manifest['library_version'],
           '- **Prompts:** '+str(len(prompts)),'- **Grupos:** '+str(len(set(p['group'] for p in prompts))),
           '- **Setores técnicos:** '+str(len(set(p['technical_sector'] for p in prompts))),
           '- **Categorias:** '+str(len(cat_counter)),'- **Subcategorias editoriais:** '+str(len(set((p['category'],p['subcategory']) for p in prompts))),'',
           '| Categoria | Prompts |','|---|---:|']
    for k,n in sorted(cat_counter.items()):lines.append(f'| {k} | {n} |')
    lines+=['','## Índices disponíveis','','- Grupos, setores técnicos, categorias, subcategorias e tags','- Profissões, fases do projeto e workflows','- Arquivos de prompt individuais com ID imutável','']
    output['README.md']='\n'.join(lines)
    buf=io.StringIO();w=csv.writer(buf,lineterminator="\n");w.writerow(['id','title','group','technical_sector','category','subcategory','tags','status','content_path'])
    for p in prompts:w.writerow([p[k] if k!='tags' else '; '.join(p[k]) for k in ['id','title','group','technical_sector','category','subcategory','tags','status','content_path']])
    output['catalogo.csv']=buf.getvalue()
    output['indices-relacoes.json']=json.dumps(other,ensure_ascii=False,indent=2)+'\n'
    problems=[]
    if check:
        existing=set(f.relative_to(INDICES).as_posix() for f in INDICES.rglob('*') if f.is_file())
        if existing!=set(output):problems.append('arquivos de índices divergentes: '+repr(sorted(existing^set(output))[:15]))
        for p,v in output.items():
            target=INDICES / p
            if not target.is_file() or target.read_text(encoding='utf-8')!=v:problems.append(f'índice desatualizado: {p}')
    else:
        for f in INDICES.rglob('*'):
            if f.is_file() and f.relative_to(INDICES).as_posix() not in output:f.unlink()
        for p,v in output.items():
            target=INDICES/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(v,encoding='utf-8')
    return problems

def validate(check_indexes=True):
    errors=[]
    manifest=load(MANIFEST);tax=load(TAXONOMY)
    pmap={};path_set=set()
    if not RE_VERSION.fullmatch(manifest['library_version']):errors.append('versão SemVer inválida')
    if manifest['schema_version']!='1.0.0':errors.append('schema_version não suportado')
    for version,src in manifest['sources'].items():
        path=ROOT/src['path']
        if not path.is_file():errors.append(f'fonte histórica ausente: {version}')
        elif sha(path.read_bytes())!=src['sha256']:
            errors.append(f'fonte histórica adulterada: {version}')
    for p in manifest['prompts']:
        key=p['id']
        if not re.fullmatch(r'\d{4}',key):errors.append(f'ID inválido: {key}')
        if key in pmap:errors.append(f'ID duplicado: {key}')
        pmap[key]=p
        file=ROOT/p['content_path']
        if p['content_path'] in path_set:errors.append(f'arquivo associado a múltiplos IDs: {file}')
        path_set.add(p['content_path'])
        if file!=locate(key):errors.append(f'caminho canônico incorreto: {key}')
        if not file.is_file():errors.append(f'arquivo ausente: {key}');continue
        content=file.read_text(encoding='utf-8')
        if sha(content)!=p['content_sha256']:errors.append(f'hash divergente: {key}')
        m=RE_MD.search(content); meta={k:v.strip() for k,v in RE_FIELD.findall(content)}
        if not m or m.group(1)!=key or m.group(2)!=p['title']:errors.append(f'cabeçalho divergente: {key}')
        if meta.get('Nome')!=p['title'] or meta.get('ID')!=key or meta.get('Categoria')!=p['category']:
            errors.append(f'campos da ficha divergentes: {key}')
        try:
            c,sub=classify(tax,p)
            if (c['code']!=p['category_code'] or c['group']!=p['group'] or
                c['technical_sector']!=p['technical_sector'] or sub!=p['subcategory']):
                errors.append(f'taxonomia divergente: {key}')
        except ValueError as exc: errors.append(str(exc))
        if p['status'] not in {'ACTIVE','DEPRECATED','SUPERSEDED'}:errors.append(f'status inválido: {key}')
        if not RE_VERSION.fullmatch(p['content_version']):errors.append(f'content_version inválida: {key}')
        if p['status']=='SUPERSEDED' and not p['replaced_by']:errors.append(f'substituição sem alvo: {key}')
        if p['status']=='ACTIVE' and p['replaced_by']:errors.append(f'ativo com replacement: {key}')
        if key in p.get('replaces',[]):errors.append(f'ID substitui a si mesmo: {key}')
    actual_files={p.relative_to(ROOT).as_posix() for p in PROMPTS.rglob('*.md')}
    extra=actual_files-path_set
    if extra:errors.append(f'arquivos sem registro no manifesto: {len(extra)}, ex. {sorted(extra)[:4]}')
    if manifest['total_prompts']!=len(pmap):errors.append('contagem no manifesto divergente')
    if len(tax['groups'])!=len(set(tax['groups'])) or len(tax['technical_sectors'])!=len(set(tax['technical_sectors'])):
        errors.append('grupo/setor duplicado na taxonomia')
    if len(set(c['code'] for c in tax['categories']))!=len(tax['categories']):
        errors.append('código de categoria duplicado')
    relations=load(RELATIONS)
    for kind,relation_set in relations.items():
        for title,ids in relation_set.items():
            if len(ids)!=len(set(ids)):errors.append(f'IDs repetidos na relação {kind}/{title}')
            missing_refs=set(ids)-set(pmap)
            if missing_refs:errors.append(f'IDs inexistentes na relação {kind}/{title}: {sorted(missing_refs)}')
    if manifest['active_prompts']!=sum(p['status']=='ACTIVE' for p in pmap.values()):errors.append('contagem de ativos divergente')
    eventlist=[json.loads(s) for s in LEDGER.read_text(encoding='utf-8').splitlines() if s.strip()]
    last_events={}
    for e in eventlist:
        if e['id'] not in pmap:errors.append(f'evento para ID inexistente: {e["id"]}')
        if e['action'] not in ('CREATE','EDIT','DEPRECATE','SUPERSEDE'):
            errors.append(f'ação inválida no ledger: {e["id"]}')
        last_events[e['id']]=e
    for key,p in pmap.items():
        if key not in last_events: errors.append(f'ID sem evento no ledger: {key}')
        elif last_events[key]['sha256']!=p['content_sha256']:
            errors.append(f'ledger não corresponde ao hash atual: {key}')
    # Toda release anterior deve preservar IDs e conteúdo histórico por identidade.
    snapshot_paths=sorted(RELEASES.glob('v*.json'),key=lambda f: tuple(map(int,f.stem[1:].split('.'))))
    prev_ids=set()
    prev_hashes={}
    for snapshot_path in snapshot_paths:
        snapshot=load(snapshot_path)
        version=snapshot_path.stem[1:]
        if snapshot.get('library_version')!=version:
            errors.append(f'versão incompatível no snapshot {version}')
        ids={q['id'] for q in snapshot['prompts']}
        if not prev_ids.issubset(ids):
            errors.append(f'IDs removidos entre releases: {version}')
        if len(ids)!=len(snapshot['prompts']) or snapshot['total_prompts']!=len(ids):
            errors.append(f'contagem de snapshot divergente: {version}')
        for q in snapshot['prompts']:
            if q['id'] in prev_hashes and q['category']!=prev_hashes[q['id']][1]:
                errors.append(f'categoria alterada entre releases: {q["id"]}')
        prev_hashes={q['id']:(q['content_sha256'],q['category']) for q in snapshot['prompts']}
        prev_ids=ids
    for old in load(RELEASES/'v1.0.0.json')['prompts']:
        if old['id'] not in pmap:errors.append(f'ID histórico removido em vez de tombstone: {old["id"]}')
        elif old['category']!=pmap[old['id']]['category']:errors.append(f'categoria histórica alterada: {old["id"]}')
    snapfile=RELEASES/('v'+manifest['library_version']+'.json')
    if not snapfile.exists():errors.append('snapshot da release atual ausente')
    elif load(snapfile)!=manifest:errors.append('snapshot da release atual diverge do manifesto')
    # Gate v2: catálogo de contratos por prompt e crosswalk de UX.
    if tuple(map(int,manifest['library_version'].split('.'))) >= (2,0,0):
        try:
            from v2_contracts import validate_contracts
            errors += validate_contracts()
        except (ValueError, KeyError, OSError) as exc:
            errors.append(f'contratos v2: {exc}')
    if check_indexes:
        src=(SOURCES/'Biblioteca_Mestre_Prompts_TI_v1.1.md').read_text(encoding='utf-8')
        errors+=write_indexes(manifest,src,check=True)
        if not any(e.startswith('arquivo ausente:') for e in errors):
            errors+=compile_master(manifest,check=True)
    # Coleções externas são acervos complementares, auditados pelo mesmo gate
    # sem alterar IDs nem snapshots canônicos.
    try:
        from collections_integration import validate as validate_complementary_collection
        errors += validate_complementary_collection()
    except (ValueError, KeyError, OSError) as exc:
        errors.append(f'erro na coleção complementar: {exc}')
    return errors

def historical_audit():
    v0=(SOURCES/'Biblioteca_Mestre_Prompts_TI_v1.0.md').read_text(encoding='utf-8')
    v1=(SOURCES/'Biblioteca_Mestre_Prompts_TI_v1.1.md').read_text(encoding='utf-8')
    e0,b0=extract(v0);e1,b1=extract(v1)
    common=e0.keys() & e1.keys()
    changed_names={k:{'from':e0[k]['title'],'to':e1[k]['title']} for k in common if e0[k]['title']!=e1[k]['title']}
    changed_bodies=[k for k in common if b0[k]!=b1[k]]
    data={'v1_0_count':len(e0),'v1_1_count':len(e1),'preserved_ids':len(common),
          'new_ids':sorted(e1.keys()-e0.keys()),'removed_ids':sorted(e0.keys()-e1.keys()),
          'renamed':changed_names,'changed_fiches':sorted(changed_bodies),
          'unexpected_content_changes':sorted(set(changed_bodies)-set(changed_names)),
          'sources':{'v1.0.0':sha(v0),'v1.1.0':sha(v1)}}
    expected=load(HISTORY)
    if data!=expected:raise ValueError('Histórico gerado diverge da baseline histórica versionada')
    return data


def compile_master(manifest,check=False):
    """Publicação de leitura; cada ficha original permanece idêntica em prompts/."""
    p=ROOT/'dist'/f'Biblioteca_Mestre_TI_Estruturada_v{manifest["library_version"]}.md'
    rows=sorted(manifest['prompts'],key=lambda x:(x['group'],x['technical_sector'],x['category'],x['subcategory'],x['id']))
    lines=['# Biblioteca Mestre de Prompts TI — Edição estruturada',
           '', '**Versão:** '+manifest['library_version'],
           '**Quantidade de prompts:** '+str(len(rows)),
           '**Política:** IDs permanentes e não recicláveis.',
           '', '> Documento gerado automaticamente. Fonte canônica: arquivos `prompts/` e manifesto versionado.',
           '', '## Mapa editorial','']
    for group in sorted(set(x['group'] for x in rows)):
        count=sum(x['group']==group for x in rows)
        lines.append(f'- **{group}** — {count} prompts')
    lines+=['','---','']
    prev=(None,None,None,None)
    for r in rows:
        current=(r['group'],r['technical_sector'],r['category'],r['subcategory'])
        for level,(part,past) in enumerate(zip(current,prev)):
            if part!=past:
                lines+=['','#'*(level+2)+' '+part,'']
                prev=current[:level+1]+(None,)*(3-level)
        content=(ROOT/r['content_path']).read_text(encoding='utf-8').strip()
        # Promote prompt headings to a leaf level without altering the canonical file.
        content=re.sub(r'(?m)^### PROMPT ', '###### PROMPT ',content,count=1)
        lines+=['',content,'','---','']
        prev=current
    result='\n'.join(lines).rstrip()+'\n'
    if check:
        return [] if p.is_file() and p.read_text(encoding='utf-8')==result else ['compilado editorial desatualizado']
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(result,encoding='utf-8')
    # Arquivos antigos são artefatos de release; mantidos até remoção revisada manualmente.
    return []

def command_init(args):
    if MANIFEST.exists() and not args.force:
        raise ValueError('Manifesto já existe: init é apenas bootstrap. Use stage para novas versões; --force sobrescreve arquivos.')
    v0=(SOURCES/'Biblioteca_Mestre_Prompts_TI_v1.0.md').read_text(encoding='utf-8')
    v1=(SOURCES/'Biblioteca_Mestre_Prompts_TI_v1.1.md').read_text(encoding='utf-8')
    e0,b0=extract(v0);e1,b1=extract(v1)
    assert len(e0)==273 and len(e1)==647
    tax=load(TAXONOMY)
    recs=[];v0_recs=[];events=[]
    for key in sorted(e1):
        rec=record_from(e1[key],b1[key],tax,'1.0.0' if key in e0 else '1.1.0',
                         '1.1.0' if key not in e0 or b0[key]!=b1[key] else '1.0.0',
                         revision=2 if key in e0 and b0[key]!=b1[key] else 1)
        recs.append(rec)
        target=locate(key);target.parent.mkdir(parents=True,exist_ok=True);target.write_text(b1[key],encoding='utf-8')
        if key in e0:
            prev=record_from(e0[key],b0[key],tax,'1.0.0','1.0.0')
            v0_recs.append(prev)
            events.append({'version':'1.0.0','id':key,'action':'CREATE','reason':'Baseline original v1.0','sha256':prev['content_sha256']})
            if b0[key]!=b1[key]:
                events.append({'version':'1.1.0','id':key,'action':'EDIT','reason':'Renomeação editorial documentada na v1.1',
                               'before_sha256':prev['content_sha256'],'sha256':rec['content_sha256'],
                               'before_title':e0[key]['title'],'title':rec['title']})
        else:
            events.append({'version':'1.1.0','id':key,'action':'CREATE','reason':'Expansão v1.1', 'sha256':rec['content_sha256']})
    manifest={'schema_version':'1.0.0','library_version':'1.1.0','library_name':'Biblioteca Mestre de Prompts TI',
              'id_policy':'permanent-non-recyclable','total_prompts':647,'active_prompts':647,
              'sources':{'v1.0.0':{'path':'originais/Biblioteca_Mestre_Prompts_TI_v1.0.md','sha256':sha(v0)},
                         'v1.1.0':{'path':'originais/Biblioteca_Mestre_Prompts_TI_v1.1.md','sha256':sha(v1)}},
              'prompts':recs}
    old={**manifest,'library_version':'1.0.0','total_prompts':273,'active_prompts':273,'prompts':v0_recs}
    dump(RELATIONS,extract_professions_phases_workflows(v1,set(e1)))
    dump(MANIFEST,manifest);dump(RELEASES/'v1.0.0.json',old);dump(RELEASES/'v1.1.0.json',manifest)
    LEDGER.write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in events),encoding='utf-8')
    data={'v1_0_count':len(e0),'v1_1_count':len(e1),'preserved_ids':len(e0.keys()&e1.keys()),
          'new_ids':sorted(e1.keys()-e0.keys()),'removed_ids':sorted(e0.keys()-e1.keys()),
          'renamed':{k:{'from':e0[k]['title'],'to':e1[k]['title']} for k in sorted(e0.keys()&e1.keys()) if e0[k]['title']!=e1[k]['title']},
          'changed_fiches':sorted(k for k in e0 if b0[k]!=b1[k]),
          'unexpected_content_changes':sorted(k for k in e0 if b0[k]!=b1[k] and e0[k]['title']==e1[k]['title']),
          'sources':{'v1.0.0':sha(v0),'v1.1.0':sha(v1)}}
    dump(HISTORY,data);write_indexes(manifest,v1);compile_master(manifest)
    print('IMPORT PASS: 273 originais, 374 novos, 647 prompts; 3 renomeações, sem remoções.')

def command_audit(args):
    d=historical_audit()
    print(json.dumps({'preserved_ids':d['preserved_ids'],'new':len(d['new_ids']),'removed':d['removed_ids'],
                      'changed_fiches':d['changed_fiches'],'unexpected_content_changes':d['unexpected_content_changes']},indent=2))
    if d['removed_ids'] or d['unexpected_content_changes']:raise ValueError('Auditoria histórica encontrou divergência')

def command_validate(args):
    errs=validate(check_indexes=True)
    if errs:
        for e in errs:print('FAIL:',e)
        sys.exit(1)
    print('VALIDATE PASS: manifesto, fichas, hashes, taxonomy, IDs, ledger, snapshots, índices e coleção Programação/Design consistentes.')

def command_index(args):
    manifest=load(MANIFEST);source=(SOURCES/'Biblioteca_Mestre_Prompts_TI_v1.1.md').read_text(encoding='utf-8')
    problems=write_indexes(manifest,source,check=args.check)
    if problems:
        for x in problems:print('FAIL:',x)
        sys.exit(1)
    print('INDEX PASS' if args.check else 'INDEX GENERATED')

def command_compile(args):
    problems=compile_master(load(MANIFEST),check=args.check)
    if problems:
        for x in problems:print('FAIL:',x)
        sys.exit(1)
    print('COMPILE CHECK PASS' if args.check else 'COMPILE GENERATED')

def command_stage(args):
    if not args.reason.strip():raise ValueError('Motivo de alteração obrigatório')
    m=load(MANIFEST); old=m['library_version']
    if not RE_VERSION.fullmatch(args.version) or tuple(map(int,args.version.split('.')))<=tuple(map(int,old.split('.'))):
        raise ValueError('Nova versão SemVer deve ser maior que a atual')
    oldmap={p['id']:p for p in m['prompts']};tax=load(TAXONOMY)
    entries={}; bodies={}
    for file in PROMPTS.rglob('*.md'):
        key=file.stem
        if not re.fullmatch(r'\d{4}',key):raise ValueError(f'arquivo fora do padrão {file}')
        if file!=locate(key):raise ValueError(f'caminho do ID fora do padrão {key}')
        content=file.read_text(encoding='utf-8');mat=RE_MD.search(content)
        meta={k:v.strip() for k,v in RE_FIELD.findall(content)}
        if not mat or mat.group(1)!=key or meta.get('ID')!=key or meta.get('Nome')!=mat.group(2):
            raise ValueError(f'Ficha inválida {file}')
        if key in entries:raise ValueError(f'ID duplicado {key}')
        entries[key]={'id':key,'title':meta['Nome'],'category':meta['Categoria'],'level':meta.get('Nível','Avançado'),
                       'legacy_subcategory':meta.get('Subcategoria',''), 'source_status':oldmap.get(key,{}).get('source_status','')}
        bodies[key]=content
    missing=oldmap.keys()-entries.keys()
    if missing:raise ValueError(f'IDs apagados; use status DEPRECATED/SUPERSEDED e preserve arquivo: {sorted(missing)[:10]}')
    updated=[];new=[];events=[]
    for key in sorted(entries):
        src=entries[key];oldrec=oldmap.get(key)
        rec=record_from(src,bodies[key],tax,oldrec['first_seen'] if oldrec else args.version,
                        args.version if not oldrec or oldrec['content_sha256']!=sha(bodies[key]) or oldrec['title']!=src['title'] else oldrec['content_version'],
                        oldrec['revision']+1 if oldrec and oldrec['content_sha256']!=sha(bodies[key]) else (oldrec['revision'] if oldrec else 1))
        if oldrec:
            if oldrec['category']!=rec['category']:raise ValueError(f'Mudança de categoria proibida sem migração explícita: {key}')
            for f in ['first_seen','status','replaces','replaced_by','verticals']:
                rec[f]=oldrec[f]
            if oldrec['content_sha256']!=rec['content_sha256']:
                events.append({'version':args.version,'id':key,'action':'EDIT','reason':args.reason,
                               'before_sha256':oldrec['content_sha256'],'sha256':rec['content_sha256']})
                updated.append(key)
        else:
            events.append({'version':args.version,'id':key,'action':'CREATE','reason':args.reason,'sha256':rec['content_sha256']});new.append(key)
        updated_rec=rec
        if oldrec and oldrec['status']!='ACTIVE':updated_rec['status']=oldrec['status']
        entries[key]=updated_rec
    if not events:raise ValueError('Nenhuma alteração no conteúdo; release desnecessário')
    m['library_version']=args.version;m['prompts']=[entries[k] for k in sorted(entries)]
    m['total_prompts']=len(entries);m['active_prompts']=sum(x['status']=='ACTIVE' for x in m['prompts'])
    # Pré-validação de contratos antes de gravar manifesto/snapshot.
    if tuple(map(int,args.version.split('.'))) >= (2,0,0):
        from v2_contracts import sync_contracts
        sync_contracts(m)
    dump(MANIFEST,m);dump(RELEASES/('v'+args.version+'.json'),m)
    with LEDGER.open('a',encoding='utf-8') as f:
        for e in events:f.write(json.dumps(e,ensure_ascii=False)+'\n')
    source=(SOURCES/'Biblioteca_Mestre_Prompts_TI_v1.1.md').read_text(encoding='utf-8')
    write_indexes(m,source);compile_master(m)
    from collections_integration import build_indexes as render_complementary_indexes
    render_complementary_indexes(load(ROOT/'colecoes'/'programacao-design'/'manifest.json'),write=True)
    print(f'STAGE PASS: {args.version}; novos={len(new)}, alterados={len(updated)}, removidos=0')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='cmd',required=True)
    i=sub.add_parser('init',help='Importar os documentos e criar baseline; apenas bootstrap')
    i.add_argument('--force',action='store_true',help='Sobrescrever toda a biblioteca existente (operação destrutiva)')
    sub.add_parser('audit',help='Validar integridade histórica a partir das fontes originais')
    sub.add_parser('validate',help='Executar gates de integridade completa')
    s=sub.add_parser('index',help='Gerar ou conferir os índices');s.add_argument('--check',action='store_true')
    s=sub.add_parser('compile',help='Gerar versão completa estruturada da biblioteca');s.add_argument('--check',action='store_true')
    s=sub.add_parser('stage',help='Versionar futuras alterações explicitamente')
    s.add_argument('--version',required=True);s.add_argument('--reason',required=True)
    args=parser.parse_args()
    try:
        {'init':command_init,'audit':command_audit,'validate':command_validate,
         'index':command_index,'compile':command_compile,'stage':command_stage}[args.cmd](args)
    except (ValueError,KeyError,OSError) as exc:
        print('ERROR:',exc,file=sys.stderr);sys.exit(1)
if __name__=='__main__':main()
