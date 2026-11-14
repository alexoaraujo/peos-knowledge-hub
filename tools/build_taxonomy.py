"""Inicializa taxonomia editorial proposta; não reclassifica os IDs originais."""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).parent))
from library import extract,ROOT,TAXONOMY
source=(ROOT/'originais/Biblioteca_Mestre_Prompts_TI_v1.1.md').read_text(encoding='utf-8')
entries,_=extract(source)
by={}
for p in entries.values():
    k=p['id'][:2]+'00';by[k]=p['category']

# group, sector, and contiguous editorial subcategories per original category.
data={
'0000':('G01 — Estratégia, gestão e governança','Direção técnica',[(1,10,'Criação, diagnóstico e evolução'),(11,20,'Decisão, auditoria e release'),(21,28,'Execução, evidências e gates')]),
'0100':('G02 — Engenharia e arquitetura','Engenharia de software',[(1,5,'Requisitos e análise'),(6,10,'Qualidade e manutenção'),(11,20,'Engenharia de código e práticas avançadas')]),
'0200':('G02 — Engenharia e arquitetura','Arquitetura de sistemas',[(1,5,'Estilos, domínio e modularização'),(6,10,'Distribuição e decisões arquiteturais'),(11,15,'Modelagem e padrões arquiteturais'),(16,20,'Arquiteturas especializadas')]),
'0300':('G03 — Desenvolvimento e integrações','Backend e serviços',[(1,8,'Frameworks e runtimes'),(9,16,'Serviços seguros e padrões backend'),(17,22,'Operação e engenharia de serviços')]),
'0400':('G03 — Desenvolvimento e integrações','Frontend e experiência',[(1,10,'Interfaces, UX e qualidade'),(11,18,'Renderização e experiência web'),(19,22,'Resiliência e design de interface')]),
'0500':('G03 — Desenvolvimento e integrações','Full Stack e mobile',[(1,6,'Full Stack e entrega'),(7,12,'Aplicações mobile'),(13,16,'Monorepos e integração de aplicações')]),
'0600':('G03 — Desenvolvimento e integrações','APIs e interoperabilidade',[(1,8,'Design e contratos de APIs'),(9,14,'Protocolos e APIs avançadas'),(15,20,'Resiliência e governança de APIs')]),
'0700':('G04 — Dados, analytics e IA','Bancos e persistência',[(1,10,'Modelagem e administração de dados'),(11,18,'PostgreSQL e operações avançadas'),(19,22,'Bancos especializados')]),
'0800':('G04 — Dados, analytics e IA','Engenharia de dados',[(1,6,'Pipelines e governança de dados'),(7,12,'Streaming e plataformas de processamento'),(13,16,'Contratos e modelagem analítica')]),
'0900':('G04 — Dados, analytics e IA','Ciência de dados e ML',[(1,8,'Ciclo de vida de ML'),(9,16,'Modelagem avançada e MLOps')]),
'1000':('G04 — Dados, analytics e IA','BI e analytics',[(1,5,'BI, SQL e painéis'),(6,13,'Analytics e governança avançados')]),
'1100':('G05 — Plataforma e operações','Entrega e automação',[(1,8,'Pipelines e releases'),(9,14,'Entrega contínua e GitOps'),(15,18,'Governança e promoção de ambientes')]),
'1200':('G05 — Plataforma e operações','Containers e orquestração',[(1,8,'Containerização e fundamentos Kubernetes'),(9,18,'Kubernetes avançado')]),
'1300':('G05 — Plataforma e operações','Infraestrutura como código',[(1,8,'IaC e automação operacional'),(9,18,'Infraestrutura e testes avançados')]),
'1400':('G05 — Plataforma e operações','Plataformas cloud',[(1,8,'Plataformas cloud e provedores'),(9,17,'Operação e segurança de cloud'),(18,26,'Ambientes, previews e cloud avançada')]),
'1500':('G06 — Segurança e identidade','Engenharia de segurança',[(1,10,'Fundamentos e auditoria AppSec'),(11,18,'Avaliações, frameworks e supply chain'),(19,26,'Ameaças e controles avançados')]),
'1600':('G07 — Qualidade, auditoria e suporte','Qualidade e testes',[(1,10,'Fundamentos e testes automatizados'),(11,16,'Ferramentas e testes avançados'),(17,22,'Qualidade, dados e gates')]),
'1700':('G04 — Dados, analytics e IA','LLMs e agentes',[(1,10,'Prompts, agentes e RAG'),(11,18,'Contexto, estruturação e coordenação'),(19,26,'Busca, observabilidade e governança')]),
'1800':('G05 — Plataforma e operações','Infraestrutura de redes',[(1,8,'Redes e conectividade'),(9,18,'Redes modernas e diagnóstico')]),
'1900':('G05 — Plataforma e operações','Operação de sistemas',[(1,8,'Administração de sistemas'),(9,18,'Serviços, segurança e confiabilidade')]),
'2000':('G05 — Plataforma e operações','Git e colaboração',[(1,10,'Git, PRs e governança'),(11,18,'Proteção de repositórios e Actions'),(19,22,'Artefatos, templates e repositórios')]),
'2100':('G05 — Plataforma e operações','Confiabilidade e observabilidade',[(1,10,'Práticas SRE e incidentes'),(11,18,'Instrumentação, métricas e alerta'),(19,22,'Monitoramento e rastreamento')]),
'2200':('G07 — Qualidade, auditoria e suporte','Atendimento técnico',[(1,6,'Suporte e resolução'),(7,12,'Suporte avançado e canais')]),
'2300':('G01 — Estratégia, gestão e governança','Gestão de projetos',[(1,10,'Gestão e planejamento'),(11,18,'Gestão ágil e coordenação')]),
'2400':('G08 — Documentação e coding agents','Documentação e conhecimento',[(1,10,'Documentos e artefatos técnicos'),(11,18,'Conteúdos especializados e docs as code')]),
'2500':('G07 — Qualidade, auditoria e suporte','Auditoria e controles',[(1,12,'Auditorias técnicas e operacionais'),(13,22,'Auditorias especializadas')]),
'2600':('G07 — Qualidade, auditoria e suporte','Diagnóstico e resposta',[(1,10,'Diagnóstico geral e RCA'),(11,22,'Falhas e diagnósticos especializados')]),
'2700':('G02 — Engenharia e arquitetura','Desempenho e resiliência',[(1,6,'Performance e arquitetura de escala'),(7,14,'Performance especializada')]),
'2800':('G02 — Engenharia e arquitetura','Modernização e migrações',[(1,6,'Estratégias de modernização'),(7,14,'Migrações especializadas e compatibilidade')]),
'2900':('G02 — Engenharia e arquitetura','Platform Engineering e DX',[(1,4,'Fundamentos de Developer Experience'),(5,12,'Plataformas internas e autosserviço')]),
'3000':('G01 — Estratégia, gestão e governança','FinOps e economia',[(1,4,'Gestão e governança de custos'),(5,10,'Custos técnicos especializados')]),
'3100':('G01 — Estratégia, gestão e governança','Governança, riscos e privacidade',[(1,4,'Governança técnica e privacidade'),(5,12,'Compliance, risco e evidências')]),
'3200':('G04 — Dados, analytics e IA','Mensageria e sistemas distribuídos',[(1,4,'Kafka e entrega de eventos'),(5,8,'RabbitMQ e mensageria confiável'),(9,12,'Consistência e padrões distribuídos')]),
'3300':('G06 — Segurança e identidade','Identity e access management',[(1,5,'Identidades e federação'),(6,10,'Autorização e identidades privilegiadas')]),
'3400':('G06 — Segurança e identidade','Cadeia de suprimentos de software',[(1,5,'Proveniência e dependências'),(6,10,'Integridade e builds')]),
'3500':('G08 — Documentação e coding agents','Engenharia assistida por IA',[(1,5,'Instruções e especificação para agentes'),(6,12,'Execução e validação por agentes')]),
}
assert set(data)==set(by),set(data)^set(by)
sector_by_category={
'0000':'Governança e planejamento','2300':'Governança e planejamento','3100':'Governança e planejamento','3000':'Economia e FinOps',
'0100':'Engenharia de software e arquitetura','0200':'Engenharia de software e arquitetura',
'2700':'Desempenho e resiliência','2800':'Transformação e plataformas','2900':'Transformação e plataformas',
'0300':'Backend e serviços','0400':'Desenvolvimento de aplicações','0500':'Desenvolvimento de aplicações','0600':'Integração e APIs',
'0700':'Dados e pipelines','0800':'Dados e pipelines','0900':'Analytics e ML','1000':'Analytics e ML',
'1700':'IA e sistemas cognitivos','3200':'Mensageria e sistemas distribuídos',
'1100':'Automação e entrega','1300':'Automação e entrega','2000':'Automação e entrega',
'1200':'Cloud e runtime','1400':'Cloud e runtime','1800':'Infraestrutura e redes','1900':'Infraestrutura e redes',
'2100':'Confiabilidade e observabilidade',
'1500':'Segurança e supply chain','3400':'Segurança e supply chain','3300':'Identidade e acesso',
'1600':'Qualidade e auditoria','2500':'Qualidade e auditoria','2200':'Suporte e diagnóstico','2600':'Suporte e diagnóstico',
'2400':'Conhecimento e documentação','3500':'Agentes de desenvolvimento'
}
assert set(sector_by_category)==set(by)
categories=[]
for k in sorted(by):
 g,s,subs=data[k];s=sector_by_category[k];base=int(k)
 categories.append({'code':k,'name':by[k],'group':g,'technical_sector':s,
     'subcategories':[{'name':name,'from':base+start,'to':base+end} for start,end,name in subs]})
groups=sorted(set(x['group'] for x in categories))
sectors=sorted(set(x['technical_sector'] for x in categories))
tax={'schema_version':'1.0.0','taxonomic_policy':'editorial-mapping-does-not-change-permanent-ID',
     'groups':groups,'technical_sectors':sectors,'categories':categories,
     'orthogonal_facets':['professional_role','project_phase','technology_tag','business_vertical','workflow','risk','deliverable'],
     'business_vertical_policy':'Somente atribuir com evidência; novos setores de negócio não são presumidos na migração legado.'}
Path(TAXONOMY).write_text(json.dumps(tax,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('taxonomy created',len(groups),len(sectors),len(categories),sum(len(c['subcategories']) for c in categories))
