#!/usr/bin/env python3
"""Valida contratos v2 e decisões de curadoria editorial sem bibliotecas externas."""
from pathlib import Path
import json, re, sys, hashlib
ROOT=Path(__file__).resolve().parents[1]

def validate_contracts():
    errors=[]
    master=json.loads((ROOT/'catalog/manifest.json').read_text(encoding='utf-8'))
    expected={p['id']:p for p in master['prompts']}
    contracts=list((ROOT/'contracts').glob('*.json'))
    if {p.stem for p in contracts} != set(expected):errors.append('contratos v2 incompletos ou adicionais')
    for f in contracts:
        obj=json.loads(f.read_text(encoding='utf-8'));ref=expected.get(f.stem)
        if ref is None:continue
        for key in ['id','title','content_sha256']:
            if obj.get(key)!=ref.get('content_sha256' if key=='content_sha256' else key):errors.append(f'contrato divergente {f.stem}/{key}')
        if obj.get('schema_version')!='2.0.0' or obj.get('status') not in ('CURATED','SOURCE_EXTRACTED'):
            errors.append(f'schema ou status inválido: {f.stem}')
        if not all(isinstance(obj.get(k),str) and obj[k].strip() for k in ('goal','inputs','output_contract','acceptance_criteria')):
            errors.append(f'contrato sem informações essenciais: {f.stem}')
        if not isinstance(obj.get('related_ids'),list) or any(k not in expected for k in obj['related_ids']):
            errors.append(f'referência inválida em contrato: {f.stem}')
        if not isinstance(obj.get('source_links'),list) or any(not re.fullmatch('BPD-[0-9]{3}',k) for k in obj['source_links']):
            errors.append(f'proveniência BPD inválida: {f.stem}')
        if obj.get('human_approval')=='APPROVED' and (not obj.get('reviewer') or not obj.get('reviewed_at')):
            errors.append(f'aprovação humana sem autoria/data: {f.stem}')
    decisions=json.loads((ROOT/'catalog/ux_curadoria_v2.json').read_text(encoding='utf-8'))
    if {x['id'] for x in decisions['new_prompts']}!=set(f'{i:04d}' for i in range(3601,3613)):
        errors.append('IDs curados para UX não correspondem a 3601..3612')
    collection=json.loads((ROOT/'colecoes/programacao-design/manifest.json').read_text(encoding='utf-8'))
    bpd={x['id'] for x in collection['entries']}
    for item in decisions['new_prompts']:
        if set(item['bpd'])-bpd:errors.append('curadoria aponta para BPD ausente: '+item['id'])
    return errors

def sync_contracts(master):
    """Em releases futuras, sincroniza metadados extraídos; mudanças curadas exigem revisão humana."""
    import hashlib, re
    contract_dir=ROOT/'contracts'
    contract_dir.mkdir(exist_ok=True)
    for rec in master['prompts']:
        file=contract_dir/(rec['id']+'.json')
        source=(ROOT/rec['content_path']).read_text(encoding='utf-8')
        def field(name):
            match=re.search(r'^\*\*'+re.escape(name)+r':\*\*\s*(.*?)\s*$',source,re.M)
            return match.group(1).strip() if match else ''
        if file.exists():
            item=json.loads(file.read_text(encoding='utf-8'))
            if item.get('status')=='CURATED' and item.get('content_sha256')!=rec['content_sha256']:
                raise ValueError('Mudança em prompt CURATED exige revisão e atualização explícita de contrato: '+rec['id'])
        else:
            item={'schema_version':'2.0.0','id':rec['id'],'status':'SOURCE_EXTRACTED',
                'guardrails':'Política padrão; revisão editorial necessária','related_ids':[],
                'source_links':[],'source_type':'new-unreviewed','reviewer':None,
                'reviewed_at':None,'human_approval':'NOT_RECORDED'}
        item['title']=rec['title']
        item['content_sha256']=rec['content_sha256']
        if item['status']=='SOURCE_EXTRACTED':
            item['goal']=field('Objetivo') or rec['title']
            item['when_to_use']=field('Quando utilizar') or rec['title']
            item['inputs']=field('Entradas necessárias') or '[OBJETIVO]'
            item['output_contract']=field('Saída esperada') or 'Entrega verificável'
            item['acceptance_criteria']=field('Critérios de validação') or 'Critérios demonstrados por evidências'
            item['human_approval']='NOT_RECORDED'
        file.write_text(json.dumps(item,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':
    errs=validate_contracts()
    if errs:
        for e in errs:print('FAIL:',e)
        sys.exit(1)
    m=json.loads((ROOT/'catalog/manifest.json').read_text(encoding='utf-8'))
    print(f'CONTRACTS PASS: {len(m["prompts"])} contratos v2, 12 curados e {len(m["prompts"])-12} extraídos do legado')
