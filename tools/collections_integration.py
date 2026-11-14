#!/usr/bin/env python3
"""Importa e verifica uma coleção complementar sem renumerar o catálogo mestre.

Sem dependências externas. Fonte de verdade da coleção: arquivo original + manifesto +
checksums por entrada. IDs BPD não são IDs canônicos da Biblioteca Mestre.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLL = ROOT / 'colecoes' / 'programacao-design'
SOURCE = ROOT / 'originais' / 'Biblioteca-de-Prompts-para-Programação-e-Design.txt'
MASTER = ROOT / 'catalog' / 'manifest.json'
MANIFEST = COLL / 'manifest.json'
RELEASE = COLL / 'releases' / 'v1.0.0.json'
INDEX = COLL / 'INDEX.md'
GAPS = COLL / 'CANDIDATOS_A_NOVOS_PROMPTS.md'
EXPORT = ROOT / 'dist' / 'Catalogo_Integrado.csv'
DOC = ROOT / 'dist' / 'Guia_Integrado_Programacao_Design.md'
UNIFIED = ROOT / 'dist' / 'Biblioteca_Mestre_TI_Integrada_Completa.md'
RE_SECTION = re.compile(r'^#{1,3}\s+(\d{1,2})\.\s+(.+?)\s*$')
RE_ITEM = re.compile(r'^\s*(\d{1,3})\.\s+\*\*(.*?)\*\*\s*$')

# Mapeamento editorial de proximidade de finalidade. Não implica identidade semântica.
# Equivalências completas somente após uma revisão por especialista.
RELATED = {
    1:['0001','0101'],2:['0006','0011'],3:['2302','0101'],4:['0101','0102'],5:['2301','0011'],
    6:['0102'],7:['0103'],8:['0105','0102'],9:['0101','0104'],10:['0104'],
    11:['2301','0025'],12:['2306','2301'],13:['2303','2307'],14:['2306'],15:['2308','2316'],
    16:['0201','0501'],17:['0201','0007'],18:['0204','0212'],19:['0203'],20:['0202','0212'],
    21:['0007','0011'],22:['0401','0402'],23:['0301','0303'],24:['0701','0702'],25:['0007','0011'],
    26:['0019','2907'],27:['0504','0513'],28:['0110','2003'],29:['1104','0117'],30:['1104','1503'],
    31:['0701'],32:['0702'],33:['0701','2409'],34:['0704'],35:['2506','0708'],
    36:['0601'],37:['0601'],38:['0602'],39:['0608'],40:['0608','2505'],
    41:['0301','0502'],42:['0318','0203'],43:['0311'],44:['0114'],45:['0005','2505'],
    46:['0401','0402'],47:['0404','0502'],48:['0404'],49:['0408','0420'],50:['0420','0502'],
    51:['0404','0409'],52:['0404','2409'],53:['0404'],54:['0404','2504'],55:['0404','0422'],
    56:['0404','0422'],57:['0404'],58:['0422'],59:['0404','0422'],60:['0404','2504'],
    61:['0405','0406'],62:['0405','0505'],63:['0409','0405'],64:['0404','0405'],
    65:['0405','1620'],66:['0405','1620'],67:['0407','0405'],
    68:['0309','0503'],69:['3307','0309'],70:['0309','1525'],
    71:['1501','2509'],72:['1502','1520'],73:['1503'],74:['1505'],
    75:['0108','2502'],76:['0108'],77:['2005','0120'],78:['2503','0201'],
    79:['0004','0109'],80:['2601','0005'],81:['2622'],82:['2604'],83:['2610'],
    84:['0005'],85:['0110'],86:['0113','0110'],87:['2801','0008'],
    88:['1601'],89:['1602'],90:['1603'],91:['1604'],92:['1609','1610'],
    93:['0016','2701'],94:['0406','2710'],95:['2709'],96:['0703','0716'],
    97:['0028','0209'],98:['1201'],99:['1101','1102'],100:['1105'],
    101:['2103'],102:['2102','2105'],103:['2122','2111'],104:['2102'],
    105:['2401'],106:['0013','2410'],107:['2403'],108:['2411'],
    109:['0002','2501'],110:['2511'],111:['0002','2510'],112:['0025','2303'],113:['0010','0020'],
    114:['0023','0022'],115:['0502','0021'],116:['0027','0003'],117:['0003','0112'],118:['0010','0020'],
    119:['0201','0011'],120:['0011','2301'],121:['0502'],122:['0404','0405'],123:['0702','2506'],
    124:['1101','2508'],125:['1501','2509'],126:['0001','0502','0404'],127:['0003','0021'],128:['0001','0020'],
}
# Lacuna potencial = não há ficha mestre com o mesmo artefato de UX/UI explicitamente descrito.
# Revisão humana necessária; não cria novos IDs automaticamente.
GAP_NUMBERS = {51,52,53,54,55,59,60,61,62,63,64}

def sha(data: bytes | str) -> str:
    if isinstance(data,str): data=data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()

def load(path: Path): return json.loads(path.read_text(encoding='utf-8'))

def dump(path: Path, value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def parse_source(source: str):
    """Extrai entradas e mantém texto exato, após a linha do cabeçalho até o próximo divisor."""
    lines=source.splitlines(keepends=True)
    headings=[];starts=[];section=None
    for pos,line in enumerate(lines):
        h=RE_SECTION.fullmatch(line.rstrip('\r\n'))
        if h:
            section=(int(h.group(1)),h.group(2))
            headings.append((pos,section))
        m=RE_ITEM.fullmatch(line.rstrip('\r\n'))
        if m:
            if section is None: raise ValueError('Item fora de uma seção')
            starts.append((pos,int(m.group(1)),m.group(2),section))
    found=[]
    for idx,(pos,num,title,sect) in enumerate(starts):
        end=starts[idx+1][0] if idx+1<len(starts) else len(lines)
        # Remove separadores de seção somente da borda do excerto;
        # preserva integralmente texto interno, inclusive o prompt longo 126.
        next_heading=next((j for j,_ in headings if pos<j<end),None)
        if next_heading is not None:end=next_heading
        excerpt=''.join(lines[pos:end]).rstrip()
        excerpt=re.sub(r'\n\s*---\s*$', '', excerpt).rstrip()+'\n'
        found.append(dict(number=num,title=title,section_number=sect[0],section=sect[1],excerpt=excerpt,
                          source_start_line=pos+1,source_end_line=end))
    if [x['number'] for x in found]!=list(range(1,129)):
        raise ValueError('Enumeração original não corresponde a 1..128')
    if len(headings)!=30 or {a for _,(a,_) in headings}!=set(range(1,31)):
        raise ValueError('Seções originais não correspondem a 1..30')
    return found,[{'number':n,'title':s} for _,(n,s) in headings]

def create():
    if MANIFEST.exists():raise ValueError('Coleção já importada. Operação bloqueada para proteger baseline. Não sobrescreva sem uma migração versionada.')
    src=SOURCE.read_text(encoding='utf-8')
    items,sections=parse_source(src)
    master=load(MASTER); ids={p['id']:p for p in master['prompts']}
    if len(ids)!=647:raise ValueError('A coleção exige baseline canônica de 647 prompts')
    rows=[]
    for item in items:
        n=item['number']; pointers=RELATED.get(n,[])
        if not pointers or any(key not in ids for key in pointers):raise ValueError(f'Referência inexistente na coleção: {n}')
        primary=ids[pointers[0]]
        path=f'colecoes/programacao-design/prompts/BPD-{n:03d}.md'
        target=ROOT/path;target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(item['excerpt'],encoding='utf-8')
        rows.append({'id':f'BPD-{n:03d}','source_number':n,'title':item['title'],
                     'section_number':item['section_number'],'section':item['section'],
                     'source_start_line':item['source_start_line'],'source_end_line':item['source_end_line'],
                     'group_suggested':primary['group'],'technical_sector_suggested':primary['technical_sector'],
                     'category_suggested':'Design de Produto e UX (candidata)' if n in GAP_NUMBERS else primary['category'],
                     'subcategory_suggested':item['section'],
                     'related_canonical_ids':pointers,'relation':'related-not-necessarily-equivalent',
                     'coverage':'potential_gap' if n in GAP_NUMBERS else 'complementary',
                     'review_status':'EDITORIAL_REVIEW_REQUIRED',
                     'content_path':path,'content_sha256':sha(item['excerpt'])})
    manifest={'schema_version':'1.0.0','collection_id':'programacao-design','collection_version':'1.0.0',
              'base_library_version':'1.1.0','source_file':str(SOURCE.relative_to(ROOT)),
              'source_sha256':sha(SOURCE.read_bytes()),'source_entries':128,'source_sections':30,
              'id_policy':'BPD-local-namespace-no-canonical-id-reuse',
              'editorial_policy':'Related links are NOT semantic duplicates. Promote to new canonical ID only after human review.',
              'sections':sections,'entries':rows}
    dump(MANIFEST,manifest);dump(RELEASE,manifest)
    build_indexes(manifest,write=True)
    print(f'IMPORT PASS: {len(rows)} itens, {len(sections)} seções, 11 candidatos a lacuna, 647 IDs canônicos preservados')

def output_text(manifest):
    refs={p['id']:p for p in load(MASTER)['prompts']}
    rows=manifest['entries']
    index=['# Índice da coleção — Programação e Design','',f'**128 itens originais, 30 seções; {len(refs)} IDs canônicos atualmente registrados.**',
           '', '> IDs `BPD-001` a `BPD-128` são identificadores **locais**. Ligações a prompts mestres indicam afinidade de tema, não identidade funcional.','']
    for sec in manifest['sections']:
        index.append(f"## {sec['number']}. {sec['title']}")
        index.append('')
        index.append('| ID local | Prompt | Categoria sugerida | Relacionado a | Situação |')
        index.append('|---|---|---|---|---|')
        for r in rows:
            if r['section_number']==sec['number']:
                link=' / '.join('`'+x+'`' for x in r['related_canonical_ids'])
                state='Revisar lacuna' if r['coverage']=='potential_gap' else 'Complementar'
                index.append(f"| `{r['id']}` | [{r['title']}](prompts/{r['id']}.md) | {r['category_suggested']} | {link} | {state} |")
        index.append('')
    gaps=['# Candidatos a novas finalidades canônicas: Design de Produto e UX','',
          '**Proposta editorial, não aprovação de novos IDs.**',
          'O catálogo mestre v1.1 possui design system, acessibilidade e componentes, mas não lista',
          'necessariamente como finalidades próprias todos os artefatos abaixo. Antes de adicionar IDs',
          'canônicos, comparar objetivos, contratos de saída e critérios de validação com o catálogo completo.','',
          '| Referência local | Finalidade candidata | Prompt relacionado |','|---|---|---|']
    for r in rows:
        if r['coverage']=='potential_gap':
            gaps.append(f"| `{r['id']}` | {r['title']} | {', '.join(r['related_canonical_ids'])} |")
    gaps+=['','## Política de inclusão','',
           '- Nenhum número original 1..128 substitui ou reutiliza um ID canônico.',
           '- Incorporar apenas novas finalidades distintas após análise humana e atribuição de ID livre.',
           '- Especializações de UX, wireframes e layout devem ter saída, entradas e critérios de aceite próprios.',
           '- Preservar os textos originais nesta coleção para permitir auditoria de proveniência.','']
    out=io.StringIO(); writer=csv.writer(out,lineterminator='\n')
    writer.writerow(['namespace','id','title','group','sector','category','subcategory','status','related_canonical_ids','content_path'])
    for p in refs.values():
        writer.writerow(['MASTER',p['id'],p['title'],p['group'],p['technical_sector'],p['category'],p['subcategory'],p['status'],'',p['content_path']])
    for r in rows:
        writer.writerow(['BPD',r['id'],r['title'],r['group_suggested'],r['technical_sector_suggested'],r['category_suggested'],r['subcategory_suggested'],r['review_status'],';'.join(r['related_canonical_ids']),r['content_path']])
    doc=['# Guia de integração — Biblioteca Mestre e Programação e Design','',
         '## Escopo','',
         f"- Biblioteca Mestre: {len(refs)} fichas e IDs canônicos, versão {load(MASTER)['library_version']}; baseline da coleção: {manifest['base_library_version']}.",
         f"- Coleção Programação e Design: {len(rows)} itens locais, {len(manifest['sections'])} seções.",
         f"- Inventário combinado: {len(refs)+len(rows)} entradas navegáveis; NÃO representam necessariamente finalidades distintas.",
         f"- Candidatos a lacunas de UX/UI: {sum(r['coverage']=='potential_gap' for r in rows)} (em revisão).",'',
         '## Navegação','',
         '- [Índice da coleção](../colecoes/programacao-design/INDEX.md)',
         '- [Candidatos a novos prompts de UX](../colecoes/programacao-design/CANDIDATOS_A_NOVOS_PROMPTS.md)',
         '- [Catálogo integrado CSV](Catalogo_Integrado.csv)',
         '- [Biblioteca integrada em um único Markdown](Biblioteca_Mestre_TI_Integrada_Completa.md)',
         '- [Documento original](../originais/Biblioteca-de-Prompts-para-Programação-e-Design.txt)',
         '', '## Governança de IDs','',
         'IDs BPD são locais, independentes dos quatro dígitos permanentes da Biblioteca Mestre.',
         'Não considerar que uma associação temática indica duplicata ou equivalência exata.','',
         'A coleção preserva a baseline original; a curadoria 2.0 de UX é registrada separadamente em `catalog/ux_curadoria_v2.json`.',
         '','## Validação','',
         'Execute `python3 tools/collections_integration.py check` e `python3 tools/library.py validate`.','']
    master_compiled=ROOT/'dist'/f"Biblioteca_Mestre_TI_Estruturada_v{load(MASTER)['library_version']}.md"
    appendix=['', '---', '', '# Apêndice — Coleção Programação e Design (128 entradas locais)', '',
       '> Conteúdo complementar preservado da fonte original. IDs `BPD-*` são locais e não substituem os IDs mestres.', '']
    for sec in manifest['sections']:
        appendix.extend([f"## BPD / Seção {sec['number']:02d} — {sec['title']}",''])
        for entry in rows:
            if entry['section_number']==sec['number']:
                appendix.extend([f"### {entry['id']} — {entry['title']}",'',
                                 (ROOT/entry['content_path']).read_text(encoding='utf-8').rstrip(),'', ''])
    unified=master_compiled.read_text(encoding='utf-8').rstrip()+'\n'+\
        '\n'.join(appendix).rstrip()+'\n'
    return {INDEX:'\n'.join(index).rstrip()+'\n',GAPS:'\n'.join(gaps).rstrip()+'\n',
            EXPORT:out.getvalue(),DOC:'\n'.join(doc),UNIFIED:unified}

def build_indexes(manifest,write=False):
    expected=output_text(manifest)
    errors=[]
    for path,content in expected.items():
        if write:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(content,encoding='utf-8')
        elif not path.is_file() or path.read_text(encoding='utf-8')!=content:
            errors.append(f'índice integrado desatualizado: {path.relative_to(ROOT)}')
    return errors

def validate():
    issues=[]
    if not MANIFEST.is_file() or not SOURCE.is_file():return ['manifesto/fonte da coleção ausente']
    m=load(MANIFEST); base=load(MASTER)
    if m['schema_version']!='1.0.0' or m['collection_version']!='1.0.0':issues.append('versão da coleção inesperada')
    baseline_file=ROOT/'releases'/('v'+m['base_library_version']+'.json')
    if not baseline_file.is_file():
        issues.append('snapshot da baseline mestre ausente')
    else:
        baseline=load(baseline_file)
        if not {p['id'] for p in baseline['prompts']} <= {p['id'] for p in base['prompts']}:
            issues.append('IDs da baseline mestre não preservados')
    if m!=load(RELEASE):issues.append('snapshot da coleção diverge do manifesto')
    if sha(SOURCE.read_bytes())!=m['source_sha256']:issues.append('hash da fonte da coleção divergente')
    parsed,sections=parse_source(SOURCE.read_text(encoding='utf-8'))
    entries=m['entries']; related={p['id'] for p in base['prompts']}; seen=set()
    if len(entries)!=128 or m['source_entries']!=128 or len(sections)!=30 or m['source_sections']!=30:
        issues.append('contagem de seções/entradas divergente')
    if sections!=m['sections']:issues.append('títulos das seções divergentes')
    for idx,item in enumerate(parsed):
        if idx>=len(entries):break
        row=entries[idx];key=f'BPD-{item["number"]:03d}'
        if row['id']!=key or key in seen:issues.append(f'ID local incorreto ou duplicado: {key}')
        seen.add(key)
        if row['title']!=item['title'] or row['section']!=item['section'] or row['section_number']!=item['section_number']:
            issues.append(f'metadados originais incorretos: {key}')
        if row['source_start_line']!=item['source_start_line'] or row['source_end_line']!=item['source_end_line']:
            issues.append(f'localização original divergente: {key}')
        if set(row['related_canonical_ids'])-related:issues.append(f'link a ID canônico ausente: {key}')
        if row['coverage'] not in ('complementary','potential_gap'):issues.append(f'cobertura inválida: {key}')
        path=ROOT/row['content_path']
        if path!=COLL/'prompts'/f'{key}.md':issues.append(f'caminho inválido: {key}')
        if not path.is_file():issues.append(f'entrada da coleção ausente: {key}');continue
        actual=path.read_text(encoding='utf-8')
        if actual!=item['excerpt'] or sha(actual)!=row['content_sha256']:
            issues.append(f'entrada divergente do original ou hash: {key}')
    actual_files={x.name for x in (COLL/'prompts').glob('*.md')}
    if actual_files!={f'BPD-{n:03d}.md' for n in range(1,129)}:issues.append('arquivos da coleção ausentes/adicionais')
    if len(seen)!=128:issues.append('IDs locais ausentes')
    if len({p['id'] for p in base['prompts']})<647:issues.append('IDs canônicos históricos ausentes')
    issues+=build_indexes(m,write=False)
    return issues

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['import','check','render'])
    args=parser.parse_args()
    if args.command=='import':create();return
    if args.command=='render':
        problems=validate()
        if problems:
            # Re-rendering is only for an index state modified by documented change.
            for p in problems:
                if not p.startswith('índice integrado desatualizado'):raise ValueError(p)
        build_indexes(load(MANIFEST),write=True)
        print('RENDER PASS: índices da coleção atualizados')
        return
    problems=validate()
    if problems:
        for item in problems:print('FAIL:',item)
        raise SystemExit(1)
    print('COLLECTION PASS: 128 itens, 30 seções, fonte intacta, vínculos válidos, 647 IDs históricos preservados')

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,OSError) as exc:print('ERROR:',exc,file=sys.stderr);sys.exit(1)
