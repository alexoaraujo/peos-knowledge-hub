# BIBLIOTECA MESTRE DE PROMPTS PARA PROFISSIONAIS DE TI
## Versão 1.0 — Núcleo profissional pesquisado, consolidado e numerado permanentemente

**Data de consolidação:** 23/08/2026  
**Quantidade de prompts nesta versão:** 273  
**Regra de identidade:** IDs são permanentes, não recicláveis e independentes da versão editorial do texto.

> Esta biblioteca é uma síntese própria baseada em documentação oficial, literatura técnica e bibliotecas públicas. Ela não copia literalmente coleções externas. Os prompts foram normalizados para uso profissional, com objetivo, entradas, contrato de saída e critérios de validação.

## 1. Governança da numeração permanente

- O formato canônico é **Prompt 0001**, **Prompt 0312**, etc. Em conversa, zeros à esquerda podem ser omitidos: “Prompt 312” é interpretado como **0312** quando não houver ambiguidade.
- Um ID identifica uma **finalidade**, não uma redação exata. Melhorias editoriais mantêm o ID e incrementam a versão interna.
- Mudança material de objetivo, escopo ou contrato de saída recebe **novo ID**.
- IDs removidos tornam-se *tombstones* (DEPRECATED/SUBSTITUÍDO) e **nunca são reutilizados**.
- Combinações são válidas: **Prompts 0003 + 2501 + 0020** significa continuidade -> auditoria de repositório -> gate de release.
- Quando prompts forem combinados, prevalecem: segurança e restrições explícitas > critérios de sucesso > escopo específico > formato de saída.
- Faixas vazias permanecem reservadas para expansão sem renumeração.

## 2. Princípios de construção adotados

1. **Outcome-first:** definir resultado e critérios de sucesso antes de prescrever passos desnecessários.
2. **Contexto explícito:** fornecer dados, arquivos, repositório, ambiente, versões e restrições relevantes.
3. **Contrato de saída:** especificar estrutura, nível de detalhe e campos obrigatórios.
4. **Evidência e fallback:** não inventar fatos; indicar o que é confirmado, inferido, recomendado ou não verificado.
5. **Validação:** todo prompt profissional inclui uma forma objetiva de conferir a conclusão.
6. **Iteração e evals:** prompts devem ser avaliados em casos representativos, edge cases e regressões.
7. **Segurança por projeto:** secrets, least privilege, supply chain, logs e rollback entram quando aplicáveis.
8. **Prompt enxuto:** repetir menos instruções e adicionar detalhe somente quando muda o comportamento esperado.

## 3. ÍNDICE / MENU MESTRE

- **0000-0099 — Prompts Mestres e Universais** (20 prompts nesta versão)
- **0100-0199 — Engenharia de Software** (10 prompts nesta versão)
- **0200-0299 — Arquitetura de Sistemas** (10 prompts nesta versão)
- **0300-0399 — Desenvolvimento Backend** (10 prompts nesta versão)
- **0400-0499 — Desenvolvimento Frontend** (10 prompts nesta versão)
- **0500-0599 — Full Stack e Mobile** (6 prompts nesta versão)
- **0600-0699 — APIs e Integrações** (8 prompts nesta versão)
- **0700-0799 — Banco de Dados** (10 prompts nesta versão)
- **0800-0899 — Data Engineering** (6 prompts nesta versão)
- **0900-0999 — Data Science e Machine Learning** (8 prompts nesta versão)
- **1000-1099 — Business Intelligence** (5 prompts nesta versão)
- **1100-1199 — DevOps e CI/CD** (8 prompts nesta versão)
- **1200-1299 — Containers e Kubernetes** (8 prompts nesta versão)
- **1300-1399 — IaC e Automação** (8 prompts nesta versão)
- **1400-1499 — Cloud Computing** (8 prompts nesta versão)
- **1500-1599 — Segurança da Informação** (10 prompts nesta versão)
- **1600-1699 — QA e Testes** (10 prompts nesta versão)
- **1700-1799 — Inteligência Artificial e LLM** (10 prompts nesta versão)
- **1800-1899 — Redes** (8 prompts nesta versão)
- **1900-1999 — Administração de Sistemas** (8 prompts nesta versão)
- **2000-2099 — Git e GitHub** (10 prompts nesta versão)
- **2100-2199 — SRE e Observabilidade** (10 prompts nesta versão)
- **2200-2299 — Suporte Técnico e Help Desk** (6 prompts nesta versão)
- **2300-2399 — Gestão de Projetos de TI** (10 prompts nesta versão)
- **2400-2499 — Documentação Técnica** (10 prompts nesta versão)
- **2500-2599 — Auditoria Técnica** (12 prompts nesta versão)
- **2600-2699 — Diagnóstico e Troubleshooting** (10 prompts nesta versão)
- **2700-2799 — Performance, Escalabilidade e Resiliência** (6 prompts nesta versão)
- **2800-2899 — Modernização e Migração** (6 prompts nesta versão)
- **2900-2999 — Platform Engineering e Developer Experience** (4 prompts nesta versão)
- **3000-3099 — FinOps e Custos** (4 prompts nesta versão)
- **3100-3199 — Governança, Risco e Privacidade** (4 prompts nesta versão)

## 4. ÍNDICE DE CONSULTA RÁPIDA — QUERO...

| Quero... | Prompt |
|---|---|
| Criar um sistema do zero | **0001 — Criar Projeto de Software do Zero** |
| Auditar projeto existente | **0002 — Auditoria Completa de Projeto** |
| Continuar projeto sem reiniciar | **0003 — Continuidade de Projeto** |
| Diagnosticar problema complexo | **0004 — Diagnóstico de Problemas** |
| Refatorar com segurança | **0005 — Refatoração Incremental Segura** |
| Pesquisar tecnologia | **0006 — Pesquisa Técnica Profunda** |
| Comparar tecnologias | **0007 — Comparação de Tecnologias** |
| Validar antes de release | **0020 — Release Readiness / Go-No-Go** |
| Levantar requisitos | **0101 — Levantamento de Requisitos** |
| Definir arquitetura | **0201 — Seleção de Estilo Arquitetural** |
| Criar backend | **0301 — Node.js + NestJS** |
| Criar frontend React | **0401 — React** |
| Implementar feature ponta a ponta | **0502 — Implementação de Feature Ponta a Ponta** |
| Criar API REST | **0601 — Design de API REST** |
| Documentar API | **0602 — OpenAPI / Swagger** |
| Modelar banco | **0701 — Modelagem Relacional** |
| Otimizar PostgreSQL | **0703 — Otimização de Queries SQL** |
| Criar ETL/ELT | **0801 — ETL / ELT** |
| Fazer EDA | **0901 — Análise Exploratória de Dados** |
| Criar dashboard Power BI | **1001 — Power BI** |
| Configurar CI/CD | **1101 — Estratégia CI/CD** |
| Criar GitHub Actions | **1102 — GitHub Actions** |
| Criar Dockerfile | **1201 — Dockerfile de Produção** |
| Implantar no Kubernetes | **1204 — Deployment Kubernetes** |
| Criar Terraform | **1301 — Terraform** |
| Escolher cloud | **1401 — Comparação AWS vs Azure vs GCP** |
| Auditar segurança | **1501 — Auditoria AppSec** |
| Criar estratégia de testes | **1601 — Estratégia de Testes** |
| Criar E2E Playwright | **1604 — E2E com Playwright** |
| Criar prompt profissional | **1701 — Engenharia de Prompts Profissional** |
| Criar RAG | **1703 — RAG** |
| Criar agente de IA | **1704 — Agentes de IA** |
| Diagnosticar DNS | **1802 — DNS** |
| Auditar Linux | **1901 — Auditoria Linux** |
| Revisar repositório GitHub | **2001 — Auditoria de Repositório GitHub** |
| Definir SLOs | **2101 — SLI, SLO e SLA** |
| Responder incidente | **2106 — Resposta a Incidentes SRE** |
| Triar chamado | **2201 — Triagem de Chamado** |
| Criar backlog | **2303 — Backlog Priorizado** |
| Criar roadmap | **2306 — Roadmap** |
| Criar README | **2401 — README Profissional** |
| Criar runbook | **2406 — Runbook** |
| Auditar produção | **2512 — Auditoria de Produção, Custos e Performance** |
| Investigar falha de deploy | **2602 — Falha de Deploy** |
| Analisar gargalo | **2706 — Análise de Gargalos** |
| Modernizar legado | **2801 — Modernização de Legado** |
| Criar golden path | **2903 — Golden Path** |
| Otimizar custo cloud | **3002 — Otimização de Custos Cloud** |
| Mapear compliance | **3102 — Mapeamento de Compliance** |

## 5. ÍNDICE POR PROFISSÃO

- **Desenvolvedor Frontend:** **0401** React, **0402** Next.js, **0404** Design System e Componentização, **0405** Acessibilidade Web, **0406** Performance Frontend, **1604** E2E com Playwright
- **Desenvolvedor Backend:** **0301** Node.js + NestJS, **0303** Python + FastAPI, **0309** Autenticação, Autorização e RBAC, **0310** Filas, Jobs, Webhooks e Cache, **0601** Design de API REST, **0703** Otimização de Queries SQL, **1603** Testes de Integração
- **Desenvolvedor Full Stack:** **0501** Arquitetura Full Stack, **0502** Implementação de Feature Ponta a Ponta, **0503** Autenticação Full Stack, **0601** Design de API REST, **0701** Modelagem Relacional, **1101** Estratégia CI/CD
- **Engenheiro de Software:** **0101** Levantamento de Requisitos, **0105** Análise de Sistemas, **0108** Code Review Profissional, **0110** Clean Code, SOLID e Design Patterns, **0005** Refatoração Incremental Segura, **0020** Release Readiness / Go-No-Go
- **Arquiteto de Software:** **0201** Seleção de Estilo Arquitetural, **0202** Domain-Driven Design (DDD), **0205** Microservices, **0208** SaaS Multi-Tenant, **0209** Alta Disponibilidade e Disaster Recovery, **0210** ADR — Architecture Decision Record
- **DevOps Engineer:** **1101** Estratégia CI/CD, **1102** GitHub Actions, **1104** Ambientes, Secrets e Variáveis, **1105** Deploy e Rollback, **1201** Dockerfile de Produção, **1301** Terraform
- **SRE:** **2101** SLI, SLO e SLA, **2102** Arquitetura de Observabilidade, **2105** Alertas Acionáveis, **2106** Resposta a Incidentes SRE, **2107** Postmortem Sem Culpa, **2108** Capacity Planning
- **Cloud Engineer:** **1401** Comparação AWS vs Azure vs GCP, **1402** Arquitetura AWS, **1403** Arquitetura Azure, **1404** Arquitetura Google Cloud, **0017** Arquitetura Cloud Well-Architected, **3002** Otimização de Custos Cloud
- **Security Engineer:** **1501** Auditoria AppSec, **1502** Threat Modeling e OWASP, **1504** IAM e Least Privilege, **1507** Hardening de Infraestrutura, **1509** Secure Code Review, **1510** Dependências e Software Supply Chain
- **DBA:** **0702** PostgreSQL Schema Design, **0703** Otimização de Queries SQL, **0704** Estratégia de Índices, **0705** Migrations Seguras, **0706** Backup, Restore e PITR, **0707** Replicação e Alta Disponibilidade
- **Data Engineer:** **0801** ETL / ELT, **0802** Pipeline de Dados, **0803** Qualidade de Dados, **0804** Data Lake / Data Warehouse, **0805** Governança e Linhagem, **0806** Observabilidade de Dados
- **Data Scientist:** **0901** Análise Exploratória de Dados, **0902** Feature Engineering, **0903** Seleção de Modelo, **0904** Treinamento e Validação, **0905** Métricas e Avaliação, **0908** MLOps
- **ML Engineer:** **0903** Seleção de Modelo, **0904** Treinamento e Validação, **0908** MLOps, **1703** RAG, **1710** Evals e Regressão de LLM
- **QA Engineer:** **1601** Estratégia de Testes, **1602** Testes Unitários, **1603** Testes de Integração, **1604** E2E com Playwright, **1607** Carga e Performance, **1610** Edge Cases e Testes Negativos
- **Automation Engineer:** **1303** Automação Bash, **1304** Automação PowerShell, **1305** Cron e Jobs Agendados, **1307** Workflow de Automação, **1308** Automação com Agentes de IA
- **Network Engineer:** **1801** Troubleshooting TCP/IP, **1802** DNS, **1805** Firewall e Proxy, **1806** Routing e Switching, **1807** Latência e Conectividade, **1808** Segurança de Rede
- **System Administrator:** **1901** Auditoria Linux, **1902** Windows Server, **1903** Usuários e Permissões, **1905** Análise de Logs de Sistema, **1907** Backup de Sistemas, **1908** Automação de SysAdmin
- **Support Engineer:** **2201** Triagem de Chamado, **2202** Reprodução de Erro, **2203** Análise de Logs para Suporte, **2205** Escalonamento Técnico, **2206** Resolução e Encerramento
- **Technical Lead:** **0002** Auditoria Completa de Projeto, **0003** Continuidade de Projeto, **0011** Tomada de Decisão Técnica, **0108** Code Review Profissional, **0210** ADR — Architecture Decision Record, **0020** Release Readiness / Go-No-Go
- **Engineering Manager:** **0011** Tomada de Decisão Técnica, **2301** Plano de Projeto de TI, **2303** Backlog Priorizado, **2306** Roadmap, **2308** Riscos e Dependências, **2309** Estimativas e Priorização
- **Product Manager de Tecnologia:** **0101** Levantamento de Requisitos, **0104** Critérios de Aceite, **2303** Backlog Priorizado, **2306** Roadmap, **2307** Épicos, Histórias e Tarefas, **2309** Estimativas e Priorização
- **Analista de Sistemas:** **0101** Levantamento de Requisitos, **0102** Requisitos Funcionais, **0103** Requisitos Não Funcionais, **0105** Análise de Sistemas, **0201** Seleção de Estilo Arquitetural
- **Analista de Segurança:** **1501** Auditoria AppSec, **1502** Threat Modeling e OWASP, **1508** Resposta a Incidentes de Segurança, **2509** Auditoria de Segurança, **3102** Mapeamento de Compliance
- **Analista de Dados:** **0901** Análise Exploratória de Dados, **1002** KPIs e Métricas, **1003** SQL Analítico, **1004** Dashboard Executivo, **1005** Qualidade e Governança de BI
- **BI Developer:** **1001** Power BI, **1002** KPIs e Métricas, **1003** SQL Analítico, **1004** Dashboard Executivo, **1005** Qualidade e Governança de BI

## 6. ÍNDICE POR FASE DO PROJETO

- **01 — Ideia:** **0006** Pesquisa Técnica Profunda → **0007** Comparação de Tecnologias → **0011** Tomada de Decisão Técnica
- **02 — Levantamento de requisitos:** **0101** Levantamento de Requisitos → **0102** Requisitos Funcionais → **0103** Requisitos Não Funcionais → **0104** Critérios de Aceite
- **03 — Planejamento:** **2301** Plano de Projeto de TI → **2303** Backlog Priorizado → **2308** Riscos e Dependências → **2309** Estimativas e Priorização
- **04 — Arquitetura:** **0201** Seleção de Estilo Arquitetural → **0202** Domain-Driven Design (DDD) → **0208** SaaS Multi-Tenant → **0210** ADR — Architecture Decision Record
- **05 — Desenvolvimento:** **0301** Node.js + NestJS → **0401** React → **0502** Implementação de Feature Ponta a Ponta
- **06 — Banco de dados:** **0701** Modelagem Relacional → **0702** PostgreSQL Schema Design → **0705** Migrations Seguras
- **07 — Integrações:** **0601** Design de API REST → **0605** Webhooks Confiáveis → **0606** Integração com Sistema Externo
- **08 — Segurança:** **1501** Auditoria AppSec → **1502** Threat Modeling e OWASP → **1504** IAM e Least Privilege
- **09 — Testes:** **1601** Estratégia de Testes → **1603** Testes de Integração → **1604** E2E com Playwright
- **10 — Infraestrutura:** **1201** Dockerfile de Produção → **1204** Deployment Kubernetes → **1301** Terraform
- **11 — Deploy:** **1105** Deploy e Rollback → **1405** Vercel → **0506** Deploy Full Stack
- **12 — Produção:** **0020** Release Readiness / Go-No-Go → **2102** Arquitetura de Observabilidade → **2512** Auditoria de Produção, Custos e Performance
- **13 — Monitoramento:** **2102** Arquitetura de Observabilidade → **2103** Estratégia de Logs → **2104** Métricas e Traces → **2105** Alertas Acionáveis
- **14 — Manutenção:** **0003** Continuidade de Projeto → **0106** Análise de Dívida Técnica → **1905** Análise de Logs de Sistema
- **15 — Troubleshooting:** **0004** Diagnóstico de Problemas → **2601** Diagnóstico de Bug → **2609** Problema em Produção
- **16 — Refatoração:** **0005** Refatoração Incremental Segura → **0106** Análise de Dívida Técnica → **0108** Code Review Profissional
- **17 — Escalabilidade:** **2702** Plano de Escalabilidade → **2704** Capacity Planning Técnico → **1208** Escalabilidade e Resiliência Kubernetes
- **18 — Auditoria:** **0002** Auditoria Completa de Projeto → **2501** Auditoria de Repositório → **2512** Auditoria de Produção, Custos e Performance
- **19 — Documentação:** **0013** Documentação Técnica Completa → **2401** README Profissional → **2406** Runbook
- **20 — Evolução:** **0003** Continuidade de Projeto → **0008** Modernização de Sistema → **2801** Modernização de Legado

## 7. MATRIZ GERAL

| ID | Prompt | Categoria | Nível | Status |
|---:|---|---|---|---|
| 0001 | Criar Projeto de Software do Zero | Prompts Mestres e Universais | Especialista | Consolidado |
| 0002 | Auditoria Completa de Projeto | Prompts Mestres e Universais | Especialista | Consolidado |
| 0003 | Continuidade de Projeto | Prompts Mestres e Universais | Especialista | Consolidado |
| 0004 | Diagnóstico de Problemas | Prompts Mestres e Universais | Especialista | Consolidado |
| 0005 | Refatoração Incremental Segura | Prompts Mestres e Universais | Especialista | Consolidado |
| 0006 | Pesquisa Técnica Profunda | Prompts Mestres e Universais | Especialista | Consolidado |
| 0007 | Comparação de Tecnologias | Prompts Mestres e Universais | Especialista | Consolidado |
| 0008 | Modernização de Sistema | Prompts Mestres e Universais | Especialista | Consolidado |
| 0009 | Migração Técnica | Prompts Mestres e Universais | Especialista | Consolidado |
| 0010 | Validação Final e Gate de Qualidade | Prompts Mestres e Universais | Especialista | Consolidado |
| 0011 | Tomada de Decisão Técnica | Prompts Mestres e Universais | Especialista | Consolidado |
| 0012 | Checklist Técnico Completo | Prompts Mestres e Universais | Especialista | Consolidado |
| 0013 | Documentação Técnica Completa | Prompts Mestres e Universais | Especialista | Consolidado |
| 0014 | Investigação de Incidente | Prompts Mestres e Universais | Especialista | Consolidado |
| 0015 | Auditoria Mestre de Segurança | Prompts Mestres e Universais | Especialista | Consolidado |
| 0016 | Auditoria Mestre de Performance | Prompts Mestres e Universais | Especialista | Consolidado |
| 0017 | Arquitetura Cloud Well-Architected | Prompts Mestres e Universais | Especialista | Consolidado |
| 0018 | Workflow Agentic com IA | Prompts Mestres e Universais | Especialista | Consolidado |
| 0019 | Onboarding de Repositório para IA | Prompts Mestres e Universais | Especialista | Consolidado |
| 0020 | Release Readiness / Go-No-Go | Prompts Mestres e Universais | Especialista | Consolidado |
| 0101 | Levantamento de Requisitos | Engenharia de Software | Intermediário | Criado e revisado |
| 0102 | Requisitos Funcionais | Engenharia de Software | Intermediário | Criado e revisado |
| 0103 | Requisitos Não Funcionais | Engenharia de Software | Intermediário | Criado e revisado |
| 0104 | Critérios de Aceite | Engenharia de Software | Intermediário | Criado e revisado |
| 0105 | Análise de Sistemas | Engenharia de Software | Avançado | Criado e revisado |
| 0106 | Análise de Dívida Técnica | Engenharia de Software | Avançado | Criado e revisado |
| 0107 | Análise de Dependências | Engenharia de Software | Avançado | Criado e revisado |
| 0108 | Code Review Profissional | Engenharia de Software | Avançado | Criado e revisado |
| 0109 | Debugging de Código | Engenharia de Software | Avançado | Criado e revisado |
| 0110 | Clean Code, SOLID e Design Patterns | Engenharia de Software | Avançado | Criado e revisado |
| 0201 | Seleção de Estilo Arquitetural | Arquitetura de Sistemas | Especialista | Criado e revisado |
| 0202 | Domain-Driven Design (DDD) | Arquitetura de Sistemas | Especialista | Criado e revisado |
| 0203 | Clean Architecture | Arquitetura de Sistemas | Especialista | Criado e revisado |
| 0204 | Monólito Modular | Arquitetura de Sistemas | Especialista | Criado e revisado |
| 0205 | Microservices | Arquitetura de Sistemas | Especialista | Criado e revisado |
| 0206 | Event-Driven Architecture | Arquitetura de Sistemas | Especialista | Criado e revisado |
| 0207 | Serverless Architecture | Arquitetura de Sistemas | Especialista | Criado e revisado |
| 0208 | SaaS Multi-Tenant | Arquitetura de Sistemas | Especialista | Criado e revisado |
| 0209 | Alta Disponibilidade e Disaster Recovery | Arquitetura de Sistemas | Especialista | Criado e revisado |
| 0210 | ADR — Architecture Decision Record | Arquitetura de Sistemas | Especialista | Criado e revisado |
| 0301 | Node.js + NestJS | Desenvolvimento Backend | Avançado | Criado e revisado |
| 0302 | Node.js + Express | Desenvolvimento Backend | Avançado | Criado e revisado |
| 0303 | Python + FastAPI | Desenvolvimento Backend | Avançado | Criado e revisado |
| 0304 | Python + Django | Desenvolvimento Backend | Avançado | Criado e revisado |
| 0305 | Java + Spring Boot | Desenvolvimento Backend | Avançado | Criado e revisado |
| 0306 | .NET Backend | Desenvolvimento Backend | Avançado | Criado e revisado |
| 0307 | Go Backend | Desenvolvimento Backend | Avançado | Criado e revisado |
| 0308 | PHP + Laravel | Desenvolvimento Backend | Avançado | Criado e revisado |
| 0309 | Autenticação, Autorização e RBAC | Desenvolvimento Backend | Avançado | Criado e revisado |
| 0310 | Filas, Jobs, Webhooks e Cache | Desenvolvimento Backend | Avançado | Criado e revisado |
| 0401 | React | Desenvolvimento Frontend | Avançado | Criado e revisado |
| 0402 | Next.js | Desenvolvimento Frontend | Avançado | Criado e revisado |
| 0403 | Vue / Angular | Desenvolvimento Frontend | Avançado | Criado e revisado |
| 0404 | Design System e Componentização | Desenvolvimento Frontend | Avançado | Criado e revisado |
| 0405 | Acessibilidade Web | Desenvolvimento Frontend | Avançado | Criado e revisado |
| 0406 | Performance Frontend | Desenvolvimento Frontend | Avançado | Criado e revisado |
| 0407 | Formulários e Validação | Desenvolvimento Frontend | Avançado | Criado e revisado |
| 0408 | Gerenciamento de Estado | Desenvolvimento Frontend | Avançado | Criado e revisado |
| 0409 | Dashboards e Interfaces de Dados | Desenvolvimento Frontend | Avançado | Criado e revisado |
| 0410 | SEO Técnico | Desenvolvimento Frontend | Avançado | Criado e revisado |
| 0501 | Arquitetura Full Stack | Full Stack e Mobile | Avançado | Criado e revisado |
| 0502 | Implementação de Feature Ponta a Ponta | Full Stack e Mobile | Avançado | Criado e revisado |
| 0503 | Autenticação Full Stack | Full Stack e Mobile | Avançado | Criado e revisado |
| 0504 | Monorepo | Full Stack e Mobile | Avançado | Criado e revisado |
| 0505 | Aplicação Mobile | Full Stack e Mobile | Avançado | Criado e revisado |
| 0506 | Deploy Full Stack | Full Stack e Mobile | Avançado | Criado e revisado |
| 0601 | Design de API REST | APIs e Integrações | Avançado | Criado e revisado |
| 0602 | OpenAPI / Swagger | APIs e Integrações | Avançado | Criado e revisado |
| 0603 | GraphQL | APIs e Integrações | Avançado | Criado e revisado |
| 0604 | OAuth 2.x / OIDC | APIs e Integrações | Avançado | Criado e revisado |
| 0605 | Webhooks Confiáveis | APIs e Integrações | Avançado | Criado e revisado |
| 0606 | Integração com Sistema Externo | APIs e Integrações | Avançado | Criado e revisado |
| 0607 | Revisão de Contrato de API | APIs e Integrações | Avançado | Criado e revisado |
| 0608 | Versionamento, Segurança e Testes de API | APIs e Integrações | Avançado | Criado e revisado |
| 0701 | Modelagem Relacional | Banco de Dados | Avançado | Criado e revisado |
| 0702 | PostgreSQL Schema Design | Banco de Dados | Avançado | Criado e revisado |
| 0703 | Otimização de Queries SQL | Banco de Dados | Avançado | Criado e revisado |
| 0704 | Estratégia de Índices | Banco de Dados | Avançado | Criado e revisado |
| 0705 | Migrations Seguras | Banco de Dados | Avançado | Criado e revisado |
| 0706 | Backup, Restore e PITR | Banco de Dados | Avançado | Criado e revisado |
| 0707 | Replicação e Alta Disponibilidade | Banco de Dados | Avançado | Criado e revisado |
| 0708 | Segurança de Banco de Dados | Banco de Dados | Avançado | Criado e revisado |
| 0709 | MySQL / SQL Server / Oracle | Banco de Dados | Avançado | Criado e revisado |
| 0710 | MongoDB, Redis e NoSQL | Banco de Dados | Avançado | Criado e revisado |
| 0801 | ETL / ELT | Data Engineering | Avançado | Criado e revisado |
| 0802 | Pipeline de Dados | Data Engineering | Avançado | Criado e revisado |
| 0803 | Qualidade de Dados | Data Engineering | Avançado | Criado e revisado |
| 0804 | Data Lake / Data Warehouse | Data Engineering | Avançado | Criado e revisado |
| 0805 | Governança e Linhagem | Data Engineering | Avançado | Criado e revisado |
| 0806 | Observabilidade de Dados | Data Engineering | Avançado | Criado e revisado |
| 0901 | Análise Exploratória de Dados | Data Science e Machine Learning | Avançado | Criado e revisado |
| 0902 | Feature Engineering | Data Science e Machine Learning | Avançado | Criado e revisado |
| 0903 | Seleção de Modelo | Data Science e Machine Learning | Avançado | Criado e revisado |
| 0904 | Treinamento e Validação | Data Science e Machine Learning | Avançado | Criado e revisado |
| 0905 | Métricas e Avaliação | Data Science e Machine Learning | Avançado | Criado e revisado |
| 0906 | NLP | Data Science e Machine Learning | Avançado | Criado e revisado |
| 0907 | Visão Computacional | Data Science e Machine Learning | Avançado | Criado e revisado |
| 0908 | MLOps | Data Science e Machine Learning | Avançado | Criado e revisado |
| 1001 | Power BI | Business Intelligence | Avançado | Criado e revisado |
| 1002 | KPIs e Métricas | Business Intelligence | Intermediário | Criado e revisado |
| 1003 | SQL Analítico | Business Intelligence | Avançado | Criado e revisado |
| 1004 | Dashboard Executivo | Business Intelligence | Avançado | Criado e revisado |
| 1005 | Qualidade e Governança de BI | Business Intelligence | Avançado | Criado e revisado |
| 1101 | Estratégia CI/CD | DevOps e CI/CD | Avançado | Criado e revisado |
| 1102 | GitHub Actions | DevOps e CI/CD | Avançado | Criado e revisado |
| 1103 | GitLab CI | DevOps e CI/CD | Avançado | Criado e revisado |
| 1104 | Ambientes, Secrets e Variáveis | DevOps e CI/CD | Avançado | Criado e revisado |
| 1105 | Deploy e Rollback | DevOps e CI/CD | Avançado | Criado e revisado |
| 1106 | Estratégia de Release | DevOps e CI/CD | Avançado | Criado e revisado |
| 1107 | Segurança de Pipeline | DevOps e CI/CD | Avançado | Criado e revisado |
| 1108 | Troubleshooting de Pipeline | DevOps e CI/CD | Avançado | Criado e revisado |
| 1201 | Dockerfile de Produção | Containers e Kubernetes | Avançado | Criado e revisado |
| 1202 | Docker Compose | Containers e Kubernetes | Avançado | Criado e revisado |
| 1203 | Segurança Docker | Containers e Kubernetes | Avançado | Criado e revisado |
| 1204 | Deployment Kubernetes | Containers e Kubernetes | Avançado | Criado e revisado |
| 1205 | Segurança Kubernetes | Containers e Kubernetes | Avançado | Criado e revisado |
| 1206 | Helm | Containers e Kubernetes | Avançado | Criado e revisado |
| 1207 | Observabilidade Kubernetes | Containers e Kubernetes | Avançado | Criado e revisado |
| 1208 | Escalabilidade e Resiliência Kubernetes | Containers e Kubernetes | Avançado | Criado e revisado |
| 1301 | Terraform | IaC e Automação | Avançado | Criado e revisado |
| 1302 | Auditoria de Infrastructure as Code | IaC e Automação | Avançado | Criado e revisado |
| 1303 | Automação Bash | IaC e Automação | Avançado | Criado e revisado |
| 1304 | Automação PowerShell | IaC e Automação | Avançado | Criado e revisado |
| 1305 | Cron e Jobs Agendados | IaC e Automação | Avançado | Criado e revisado |
| 1306 | RPA | IaC e Automação | Avançado | Criado e revisado |
| 1307 | Workflow de Automação | IaC e Automação | Avançado | Criado e revisado |
| 1308 | Automação com Agentes de IA | IaC e Automação | Avançado | Criado e revisado |
| 1401 | Comparação AWS vs Azure vs GCP | Cloud Computing | Avançado | Criado e revisado |
| 1402 | Arquitetura AWS | Cloud Computing | Avançado | Criado e revisado |
| 1403 | Arquitetura Azure | Cloud Computing | Avançado | Criado e revisado |
| 1404 | Arquitetura Google Cloud | Cloud Computing | Avançado | Criado e revisado |
| 1405 | Vercel | Cloud Computing | Avançado | Criado e revisado |
| 1406 | Cloudflare | Cloud Computing | Avançado | Criado e revisado |
| 1407 | Netlify / Render / Railway | Cloud Computing | Avançado | Criado e revisado |
| 1408 | Neon / Supabase | Cloud Computing | Avançado | Criado e revisado |
| 1501 | Auditoria AppSec | Segurança da Informação | Especialista | Criado e revisado |
| 1502 | Threat Modeling e OWASP | Segurança da Informação | Especialista | Criado e revisado |
| 1503 | Gestão de Secrets | Segurança da Informação | Especialista | Criado e revisado |
| 1504 | IAM e Least Privilege | Segurança da Informação | Especialista | Criado e revisado |
| 1505 | Segurança de APIs | Segurança da Informação | Especialista | Criado e revisado |
| 1506 | Segurança de Banco de Dados | Segurança da Informação | Especialista | Criado e revisado |
| 1507 | Hardening de Infraestrutura | Segurança da Informação | Especialista | Criado e revisado |
| 1508 | Resposta a Incidentes de Segurança | Segurança da Informação | Especialista | Criado e revisado |
| 1509 | Secure Code Review | Segurança da Informação | Especialista | Criado e revisado |
| 1510 | Dependências e Software Supply Chain | Segurança da Informação | Especialista | Criado e revisado |
| 1601 | Estratégia de Testes | QA e Testes | Avançado | Criado e revisado |
| 1602 | Testes Unitários | QA e Testes | Avançado | Criado e revisado |
| 1603 | Testes de Integração | QA e Testes | Avançado | Criado e revisado |
| 1604 | E2E com Playwright | QA e Testes | Avançado | Criado e revisado |
| 1605 | E2E com Cypress | QA e Testes | Avançado | Criado e revisado |
| 1606 | Testes de API / Postman | QA e Testes | Avançado | Criado e revisado |
| 1607 | Carga e Performance | QA e Testes | Avançado | Criado e revisado |
| 1608 | Testes de Segurança | QA e Testes | Avançado | Criado e revisado |
| 1609 | Cobertura e Qualidade | QA e Testes | Avançado | Criado e revisado |
| 1610 | Edge Cases e Testes Negativos | QA e Testes | Avançado | Criado e revisado |
| 1701 | Engenharia de Prompts Profissional | Inteligência Artificial e LLM | Especialista | Criado e revisado |
| 1702 | Avaliação e Otimização de Prompt | Inteligência Artificial e LLM | Especialista | Criado e revisado |
| 1703 | RAG | Inteligência Artificial e LLM | Especialista | Criado e revisado |
| 1704 | Agentes de IA | Inteligência Artificial e LLM | Especialista | Criado e revisado |
| 1705 | Function Calling / Tool Calling | Inteligência Artificial e LLM | Especialista | Criado e revisado |
| 1706 | Embeddings e Vector Databases | Inteligência Artificial e LLM | Especialista | Criado e revisado |
| 1707 | Análise de Documentos com IA | Inteligência Artificial e LLM | Especialista | Criado e revisado |
| 1708 | Classificação e Extração de Dados | Inteligência Artificial e LLM | Especialista | Criado e revisado |
| 1709 | Segurança contra Prompt Injection | Inteligência Artificial e LLM | Especialista | Criado e revisado |
| 1710 | Evals e Regressão de LLM | Inteligência Artificial e LLM | Especialista | Criado e revisado |
| 1801 | Troubleshooting TCP/IP | Redes | Avançado | Criado e revisado |
| 1802 | DNS | Redes | Avançado | Criado e revisado |
| 1803 | DHCP | Redes | Avançado | Criado e revisado |
| 1804 | VPN | Redes | Avançado | Criado e revisado |
| 1805 | Firewall e Proxy | Redes | Avançado | Criado e revisado |
| 1806 | Routing e Switching | Redes | Avançado | Criado e revisado |
| 1807 | Latência e Conectividade | Redes | Avançado | Criado e revisado |
| 1808 | Segurança de Rede | Redes | Avançado | Criado e revisado |
| 1901 | Auditoria Linux | Administração de Sistemas | Avançado | Criado e revisado |
| 1902 | Windows Server | Administração de Sistemas | Avançado | Criado e revisado |
| 1903 | Usuários e Permissões | Administração de Sistemas | Avançado | Criado e revisado |
| 1904 | Serviços e Processos | Administração de Sistemas | Avançado | Criado e revisado |
| 1905 | Análise de Logs de Sistema | Administração de Sistemas | Avançado | Criado e revisado |
| 1906 | Storage e Filesystems | Administração de Sistemas | Avançado | Criado e revisado |
| 1907 | Backup de Sistemas | Administração de Sistemas | Avançado | Criado e revisado |
| 1908 | Automação de SysAdmin | Administração de Sistemas | Avançado | Criado e revisado |
| 2001 | Auditoria de Repositório GitHub | Git e GitHub | Avançado | Criado e revisado |
| 2002 | Estratégia de Branches | Git e GitHub | Avançado | Criado e revisado |
| 2003 | Commits Profissionais | Git e GitHub | Avançado | Criado e revisado |
| 2004 | Pull Request | Git e GitHub | Avançado | Criado e revisado |
| 2005 | Code Review de PR | Git e GitHub | Avançado | Criado e revisado |
| 2006 | Merge, Rebase e Conflitos | Git e GitHub | Avançado | Criado e revisado |
| 2007 | Tags e Releases | Git e GitHub | Avançado | Criado e revisado |
| 2008 | Issues e GitHub Projects | Git e GitHub | Avançado | Criado e revisado |
| 2009 | GitHub Actions | Git e GitHub | Avançado | Criado e revisado |
| 2010 | Segurança de Repositório | Git e GitHub | Avançado | Criado e revisado |
| 2101 | SLI, SLO e SLA | SRE e Observabilidade | Especialista | Criado e revisado |
| 2102 | Arquitetura de Observabilidade | SRE e Observabilidade | Especialista | Criado e revisado |
| 2103 | Estratégia de Logs | SRE e Observabilidade | Especialista | Criado e revisado |
| 2104 | Métricas e Traces | SRE e Observabilidade | Especialista | Criado e revisado |
| 2105 | Alertas Acionáveis | SRE e Observabilidade | Especialista | Criado e revisado |
| 2106 | Resposta a Incidentes SRE | SRE e Observabilidade | Especialista | Criado e revisado |
| 2107 | Postmortem Sem Culpa | SRE e Observabilidade | Especialista | Criado e revisado |
| 2108 | Capacity Planning | SRE e Observabilidade | Especialista | Criado e revisado |
| 2109 | Reliability Review | SRE e Observabilidade | Especialista | Criado e revisado |
| 2110 | Game Day / Chaos / Recovery Drill | SRE e Observabilidade | Especialista | Criado e revisado |
| 2201 | Triagem de Chamado | Suporte Técnico e Help Desk | Intermediário | Criado e revisado |
| 2202 | Reprodução de Erro | Suporte Técnico e Help Desk | Avançado | Criado e revisado |
| 2203 | Análise de Logs para Suporte | Suporte Técnico e Help Desk | Avançado | Criado e revisado |
| 2204 | Base de Conhecimento | Suporte Técnico e Help Desk | Avançado | Criado e revisado |
| 2205 | Escalonamento Técnico | Suporte Técnico e Help Desk | Avançado | Criado e revisado |
| 2206 | Resolução e Encerramento | Suporte Técnico e Help Desk | Avançado | Criado e revisado |
| 2301 | Plano de Projeto de TI | Gestão de Projetos de TI | Avançado | Criado e revisado |
| 2302 | Escopo e Controle de Mudanças | Gestão de Projetos de TI | Avançado | Criado e revisado |
| 2303 | Backlog Priorizado | Gestão de Projetos de TI | Intermediário | Criado e revisado |
| 2304 | Planejamento de Sprint Scrum | Gestão de Projetos de TI | Avançado | Criado e revisado |
| 2305 | Fluxo Kanban | Gestão de Projetos de TI | Avançado | Criado e revisado |
| 2306 | Roadmap | Gestão de Projetos de TI | Avançado | Criado e revisado |
| 2307 | Épicos, Histórias e Tarefas | Gestão de Projetos de TI | Avançado | Criado e revisado |
| 2308 | Riscos e Dependências | Gestão de Projetos de TI | Avançado | Criado e revisado |
| 2309 | Estimativas e Priorização | Gestão de Projetos de TI | Avançado | Criado e revisado |
| 2310 | Jira + Confluence | Gestão de Projetos de TI | Avançado | Criado e revisado |
| 2401 | README Profissional | Documentação Técnica | Intermediário | Criado e revisado |
| 2402 | ADR | Documentação Técnica | Avançado | Criado e revisado |
| 2403 | Documentação de API | Documentação Técnica | Avançado | Criado e revisado |
| 2404 | Documentação de Banco | Documentação Técnica | Avançado | Criado e revisado |
| 2405 | Documentação de Infraestrutura | Documentação Técnica | Avançado | Criado e revisado |
| 2406 | Runbook | Documentação Técnica | Avançado | Criado e revisado |
| 2407 | Playbook / SOP | Documentação Técnica | Avançado | Criado e revisado |
| 2408 | Changelog e Release Notes | Documentação Técnica | Avançado | Criado e revisado |
| 2409 | Diagramas de Arquitetura | Documentação Técnica | Avançado | Criado e revisado |
| 2410 | Manual Técnico | Documentação Técnica | Avançado | Criado e revisado |
| 2501 | Auditoria de Repositório | Auditoria Técnica | Especialista | Criado e revisado |
| 2502 | Auditoria de Código | Auditoria Técnica | Especialista | Criado e revisado |
| 2503 | Auditoria de Arquitetura | Auditoria Técnica | Especialista | Criado e revisado |
| 2504 | Auditoria de Frontend | Auditoria Técnica | Especialista | Criado e revisado |
| 2505 | Auditoria de Backend | Auditoria Técnica | Especialista | Criado e revisado |
| 2506 | Auditoria de Banco de Dados | Auditoria Técnica | Especialista | Criado e revisado |
| 2507 | Auditoria de Infraestrutura | Auditoria Técnica | Especialista | Criado e revisado |
| 2508 | Auditoria de CI/CD | Auditoria Técnica | Especialista | Criado e revisado |
| 2509 | Auditoria de Segurança | Auditoria Técnica | Especialista | Criado e revisado |
| 2510 | Auditoria de Testes | Auditoria Técnica | Especialista | Criado e revisado |
| 2511 | Auditoria de Documentação | Auditoria Técnica | Especialista | Criado e revisado |
| 2512 | Auditoria de Produção, Custos e Performance | Auditoria Técnica | Especialista | Criado e revisado |
| 2601 | Diagnóstico de Bug | Diagnóstico e Troubleshooting | Avançado | Criado e revisado |
| 2602 | Falha de Deploy | Diagnóstico e Troubleshooting | Avançado | Criado e revisado |
| 2603 | Problema de Banco de Dados | Diagnóstico e Troubleshooting | Avançado | Criado e revisado |
| 2604 | Problema de API | Diagnóstico e Troubleshooting | Avançado | Criado e revisado |
| 2605 | Problema de Autenticação | Diagnóstico e Troubleshooting | Avançado | Criado e revisado |
| 2606 | Problema de Rede | Diagnóstico e Troubleshooting | Avançado | Criado e revisado |
| 2607 | Problema de Infraestrutura | Diagnóstico e Troubleshooting | Avançado | Criado e revisado |
| 2608 | Problema de Performance | Diagnóstico e Troubleshooting | Avançado | Criado e revisado |
| 2609 | Problema em Produção | Diagnóstico e Troubleshooting | Avançado | Criado e revisado |
| 2610 | Root Cause Analysis (RCA) | Diagnóstico e Troubleshooting | Avançado | Criado e revisado |
| 2701 | Baseline de Performance | Performance, Escalabilidade e Resiliência | Especialista | Criado e revisado |
| 2702 | Plano de Escalabilidade | Performance, Escalabilidade e Resiliência | Especialista | Criado e revisado |
| 2703 | Resiliência e Fault Tolerance | Performance, Escalabilidade e Resiliência | Especialista | Criado e revisado |
| 2704 | Capacity Planning Técnico | Performance, Escalabilidade e Resiliência | Especialista | Criado e revisado |
| 2705 | Otimização de Custos e Recursos | Performance, Escalabilidade e Resiliência | Especialista | Criado e revisado |
| 2706 | Análise de Gargalos | Performance, Escalabilidade e Resiliência | Especialista | Criado e revisado |
| 2801 | Modernização de Legado | Modernização e Migração | Especialista | Criado e revisado |
| 2802 | Estratégia de Migração | Modernização e Migração | Especialista | Criado e revisado |
| 2803 | Upgrade de Dependências | Modernização e Migração | Especialista | Criado e revisado |
| 2804 | Upgrade de Framework | Modernização e Migração | Especialista | Criado e revisado |
| 2805 | Migração de Banco de Dados | Modernização e Migração | Especialista | Criado e revisado |
| 2806 | Migração para Cloud | Modernização e Migração | Especialista | Criado e revisado |
| 2901 | Developer Experience Audit | Platform Engineering e Developer Experience | Especialista | Criado e revisado |
| 2902 | Platform Engineering | Platform Engineering e Developer Experience | Especialista | Criado e revisado |
| 2903 | Golden Path | Platform Engineering e Developer Experience | Especialista | Criado e revisado |
| 2904 | Self-Service para Desenvolvedores | Platform Engineering e Developer Experience | Especialista | Criado e revisado |
| 3001 | Auditoria FinOps | FinOps e Custos | Especialista | Criado e revisado |
| 3002 | Otimização de Custos Cloud | FinOps e Custos | Especialista | Criado e revisado |
| 3003 | Unit Economics de Infraestrutura | FinOps e Custos | Especialista | Criado e revisado |
| 3004 | Budget, Forecast e Anomalias | FinOps e Custos | Especialista | Criado e revisado |
| 3101 | Governança Técnica | Governança, Risco e Privacidade | Especialista | Criado e revisado |
| 3102 | Mapeamento de Compliance | Governança, Risco e Privacidade | Especialista | Criado e revisado |
| 3103 | Privacidade e Data Protection | Governança, Risco e Privacidade | Especialista | Criado e revisado |
| 3104 | Registro de Riscos Técnicos | Governança, Risco e Privacidade | Especialista | Criado e revisado |

## 8. FICHAS COMPLETAS DOS PROMPTS

### PROMPT 0001 — Criar Projeto de Software do Zero

**ID:** 0001  
**Nome:** Criar Projeto de Software do Zero  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Criar Projeto de Software do Zero  
**Objetivo:** executar Criar Projeto de Software do Zero com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver criar projeto de software do zero em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
Atue como arquiteto de software, tech lead, DevOps, especialista em segurança, dados e QA. Crie [PROJETO] do zero até um estado implantável.

Resultado obrigatório: requisitos -> arquitetura -> stack -> modelo de dados -> backend -> frontend -> autenticação/autorização -> segurança -> testes -> infraestrutura -> CI/CD -> deploy -> observabilidade -> documentação.

Antes de propor tecnologia, transforme [OBJETIVO] e [CONTEXTO] em requisitos funcionais e não funcionais, hipóteses e restrições. Registre decisões e trade-offs. Priorize simplicidade e evolução incremental. Para cada fase, produza entregáveis, dependências, critérios de aceite, riscos e testes. Não declare algo como concluído sem evidência. Diferencie fato, inferência, decisão e pendência. No final entregue arquitetura, backlog P0/P1/P2, plano de implementação, critérios de release e próxima ação executável.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0002 — Auditoria Completa de Projeto

**ID:** 0002  
**Nome:** Auditoria Completa de Projeto  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Auditoria Completa de Projeto  
**Objetivo:** executar Auditoria Completa de Projeto com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria completa de projeto em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
Realize uma auditoria ponta a ponta de [PROJETO]/[REPOSITÓRIO]. Inspecione evidências antes de concluir. Cubra: estrutura, arquitetura, frontend, backend, APIs, banco, autenticação/autorização, multi-tenancy quando aplicável, dependências, segurança, testes, CI/CD, containers/IaC, ambientes, produção, observabilidade, backups, custos e documentação.

Classifique cada item como FUNCIONAL, PARCIAL, AUSENTE, QUEBRADO, NÃO VERIFICADO ou RISCO. Para achados, informe evidência, impacto, severidade, prioridade P0/P1/P2, correção proposta, dependências e forma de validação. Elimine duplicidades. Não confunda existência de arquivo com funcionalidade comprovada. Termine com matriz de gaps, sequência de correção e gate final.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0003 — Continuidade de Projeto

**ID:** 0003  
**Nome:** Continuidade de Projeto  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Continuidade de Projeto  
**Objetivo:** executar Continuidade de Projeto com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver continuidade de projeto em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
Continue [PROJETO] sem reiniciar nem reconstruir desnecessariamente. Primeiro identifique a fonte de verdade e o estado real: código, branch, PRs, issues, documentos, banco, deploys e testes disponíveis. Preserve decisões válidas.

Fluxo: (1) localizar estado atual; (2) detectar alterações não integradas; (3) listar pendências e bloqueios; (4) priorizar P0/P1/P2; (5) escolher a menor próxima unidade de trabalho que avance o projeto; (6) implementar; (7) testar; (8) validar regressões; (9) documentar o que mudou; (10) atualizar o próximo passo. Não reanalise tudo do zero se já houver evidência suficiente. Não marque como concluído sem teste ou evidência equivalente.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0004 — Diagnóstico de Problemas

**ID:** 0004  
**Nome:** Diagnóstico de Problemas  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Diagnóstico de Problemas  
**Objetivo:** executar Diagnóstico de Problemas com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver diagnóstico de problemas em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
Investigue [PROBLEMA] usando diagnóstico orientado por evidências. Estruture: sintoma -> impacto -> timeline -> contexto -> hipóteses ordenadas -> testes discriminantes -> resultados -> causa raiz -> correção -> validação -> prevenção.

Não salte diretamente para uma correção. Diferencie correlação de causalidade. Comece por verificações de baixo risco e alta informação. Para cada hipótese, diga qual evidência a confirma ou refuta. Evite mudanças irreversíveis até haver evidência suficiente. Se faltar dado, identifique exatamente o menor dado necessário. Termine com RCA, correção aplicada/proposta, teste de regressão e ação preventiva.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0005 — Refatoração Incremental Segura

**ID:** 0005  
**Nome:** Refatoração Incremental Segura  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Refatoração Incremental Segura  
**Objetivo:** executar Refatoração Incremental Segura com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver refatoração incremental segura em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
Refatore [PROJETO]/[ARQUIVO] de forma incremental e segura. Primeiro estabeleça baseline funcional e testes. Identifique smells, acoplamento, duplicação, complexidade, dívida técnica, risco e impacto. Separe mudanças estruturais de mudanças funcionais.

Crie etapas pequenas, reversíveis e verificáveis. Preserve comportamento público salvo quando a mudança estiver explicitamente no escopo. Após cada etapa, execute validações adequadas. Priorize P0/P1 antes de melhorias cosméticas. Entregue antes/depois, riscos, arquivos afetados, testes, métricas quando aplicável e itens deliberadamente não alterados.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0006 — Pesquisa Técnica Profunda

**ID:** 0006  
**Nome:** Pesquisa Técnica Profunda  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Pesquisa Técnica Profunda  
**Objetivo:** executar Pesquisa Técnica Profunda com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver pesquisa técnica profunda em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Pesquisa Técnica Profunda.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Pesquisa Técnica Profunda para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0007 — Comparação de Tecnologias

**ID:** 0007  
**Nome:** Comparação de Tecnologias  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Comparação de Tecnologias  
**Objetivo:** executar Comparação de Tecnologias com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver comparação de tecnologias em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Comparação de Tecnologias.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Comparação de Tecnologias para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0008 — Modernização de Sistema

**ID:** 0008  
**Nome:** Modernização de Sistema  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Modernização de Sistema  
**Objetivo:** executar Modernização de Sistema com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver modernização de sistema em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Modernização de Sistema.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Modernização de Sistema para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0009 — Migração Técnica

**ID:** 0009  
**Nome:** Migração Técnica  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Migração Técnica  
**Objetivo:** executar Migração Técnica com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver migração técnica em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Migração Técnica.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Migração Técnica para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0010 — Validação Final e Gate de Qualidade

**ID:** 0010  
**Nome:** Validação Final e Gate de Qualidade  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Validação Final e Gate de Qualidade  
**Objetivo:** executar Validação Final e Gate de Qualidade com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver validação final e gate de qualidade em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Validação Final e Gate de Qualidade.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Validação Final e Gate de Qualidade para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 0011 — Tomada de Decisão Técnica

**ID:** 0011  
**Nome:** Tomada de Decisão Técnica  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Tomada de Decisão Técnica  
**Objetivo:** executar Tomada de Decisão Técnica com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver tomada de decisão técnica em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Tomada de Decisão Técnica.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Tomada de Decisão Técnica para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0012 — Checklist Técnico Completo

**ID:** 0012  
**Nome:** Checklist Técnico Completo  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Checklist Técnico Completo  
**Objetivo:** executar Checklist Técnico Completo com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver checklist técnico completo em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Checklist Técnico Completo.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Checklist Técnico Completo para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0013 — Documentação Técnica Completa

**ID:** 0013  
**Nome:** Documentação Técnica Completa  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Documentação Técnica Completa  
**Objetivo:** executar Documentação Técnica Completa com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver documentação técnica completa em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Documentação Técnica Completa.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Documentação Técnica Completa para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0014 — Investigação de Incidente

**ID:** 0014  
**Nome:** Investigação de Incidente  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Investigação de Incidente  
**Objetivo:** executar Investigação de Incidente com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver investigação de incidente em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Investigação de Incidente.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Investigação de Incidente para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0015 — Auditoria Mestre de Segurança

**ID:** 0015  
**Nome:** Auditoria Mestre de Segurança  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Auditoria Mestre de Segurança  
**Objetivo:** executar Auditoria Mestre de Segurança com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria mestre de segurança em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Auditoria Mestre de Segurança.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria Mestre de Segurança para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0016 — Auditoria Mestre de Performance

**ID:** 0016  
**Nome:** Auditoria Mestre de Performance  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Auditoria Mestre de Performance  
**Objetivo:** executar Auditoria Mestre de Performance com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria mestre de performance em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Auditoria Mestre de Performance.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria Mestre de Performance para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0017 — Arquitetura Cloud Well-Architected

**ID:** 0017  
**Nome:** Arquitetura Cloud Well-Architected  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Arquitetura Cloud Well-Architected  
**Objetivo:** executar Arquitetura Cloud Well-Architected com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver arquitetura cloud well-architected em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Arquitetura Cloud Well-Architected.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Arquitetura Cloud Well-Architected para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0018 — Workflow Agentic com IA

**ID:** 0018  
**Nome:** Workflow Agentic com IA  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Workflow Agentic com IA  
**Objetivo:** executar Workflow Agentic com IA com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver workflow agentic com ia em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Workflow Agentic com IA.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Workflow Agentic com IA para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0019 — Onboarding de Repositório para IA

**ID:** 0019  
**Nome:** Onboarding de Repositório para IA  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Onboarding de Repositório para IA  
**Objetivo:** executar Onboarding de Repositório para IA com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver onboarding de repositório para ia em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Onboarding de Repositório para IA.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Onboarding de Repositório para IA para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0020 — Release Readiness / Go-No-Go

**ID:** 0020  
**Nome:** Release Readiness / Go-No-Go  
**Categoria:** Prompts Mestres e Universais  
**Subcategoria:** Release Readiness / Go-No-Go  
**Objetivo:** executar Release Readiness / Go-No-Go com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver release readiness / go-no-go em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Especialista multidisciplinar de TI, engenharia de prompts e auditoria técnica, com foco em Release Readiness / Go-No-Go.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Release Readiness / Go-No-Go para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos; estado atual; arquitetura; segurança; dados; testes; CI/CD; produção; observabilidade; documentação; riscos; evidências; prioridades P0/P1/P2.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0101 — Levantamento de Requisitos

**ID:** 0101  
**Nome:** Levantamento de Requisitos  
**Categoria:** Engenharia de Software  
**Subcategoria:** Levantamento de Requisitos  
**Objetivo:** executar Levantamento de Requisitos com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver levantamento de requisitos em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Intermediário  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Engenheiro de Software Sênior, com foco em Levantamento de Requisitos.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Levantamento de Requisitos para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: correção; legibilidade; coesão; acoplamento; SOLID; padrões; complexidade; testabilidade; manutenção; dívida técnica; segurança; performance.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0102 — Requisitos Funcionais

**ID:** 0102  
**Nome:** Requisitos Funcionais  
**Categoria:** Engenharia de Software  
**Subcategoria:** Requisitos Funcionais  
**Objetivo:** executar Requisitos Funcionais com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver requisitos funcionais em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Intermediário  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Engenheiro de Software Sênior, com foco em Requisitos Funcionais.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Requisitos Funcionais para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: correção; legibilidade; coesão; acoplamento; SOLID; padrões; complexidade; testabilidade; manutenção; dívida técnica; segurança; performance.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0103 — Requisitos Não Funcionais

**ID:** 0103  
**Nome:** Requisitos Não Funcionais  
**Categoria:** Engenharia de Software  
**Subcategoria:** Requisitos Não Funcionais  
**Objetivo:** executar Requisitos Não Funcionais com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver requisitos não funcionais em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Intermediário  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Engenheiro de Software Sênior, com foco em Requisitos Não Funcionais.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Requisitos Não Funcionais para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: correção; legibilidade; coesão; acoplamento; SOLID; padrões; complexidade; testabilidade; manutenção; dívida técnica; segurança; performance.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0104 — Critérios de Aceite

**ID:** 0104  
**Nome:** Critérios de Aceite  
**Categoria:** Engenharia de Software  
**Subcategoria:** Critérios de Aceite  
**Objetivo:** executar Critérios de Aceite com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver critérios de aceite em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Intermediário  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Engenheiro de Software Sênior, com foco em Critérios de Aceite.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Critérios de Aceite para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: correção; legibilidade; coesão; acoplamento; SOLID; padrões; complexidade; testabilidade; manutenção; dívida técnica; segurança; performance.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0105 — Análise de Sistemas

**ID:** 0105  
**Nome:** Análise de Sistemas  
**Categoria:** Engenharia de Software  
**Subcategoria:** Análise de Sistemas  
**Objetivo:** executar Análise de Sistemas com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver análise de sistemas em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Engenheiro de Software Sênior, com foco em Análise de Sistemas.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Análise de Sistemas para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: correção; legibilidade; coesão; acoplamento; SOLID; padrões; complexidade; testabilidade; manutenção; dívida técnica; segurança; performance.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0106 — Análise de Dívida Técnica

**ID:** 0106  
**Nome:** Análise de Dívida Técnica  
**Categoria:** Engenharia de Software  
**Subcategoria:** Análise de Dívida Técnica  
**Objetivo:** executar Análise de Dívida Técnica com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver análise de dívida técnica em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Engenheiro de Software Sênior, com foco em Análise de Dívida Técnica.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Análise de Dívida Técnica para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: correção; legibilidade; coesão; acoplamento; SOLID; padrões; complexidade; testabilidade; manutenção; dívida técnica; segurança; performance.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0107 — Análise de Dependências

**ID:** 0107  
**Nome:** Análise de Dependências  
**Categoria:** Engenharia de Software  
**Subcategoria:** Análise de Dependências  
**Objetivo:** executar Análise de Dependências com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver análise de dependências em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Engenheiro de Software Sênior, com foco em Análise de Dependências.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Análise de Dependências para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: correção; legibilidade; coesão; acoplamento; SOLID; padrões; complexidade; testabilidade; manutenção; dívida técnica; segurança; performance.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0108 — Code Review Profissional

**ID:** 0108  
**Nome:** Code Review Profissional  
**Categoria:** Engenharia de Software  
**Subcategoria:** Code Review Profissional  
**Objetivo:** executar Code Review Profissional com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver code review profissional em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Engenheiro de Software Sênior, com foco em Code Review Profissional.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Code Review Profissional para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: correção; legibilidade; coesão; acoplamento; SOLID; padrões; complexidade; testabilidade; manutenção; dívida técnica; segurança; performance.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0109 — Debugging de Código

**ID:** 0109  
**Nome:** Debugging de Código  
**Categoria:** Engenharia de Software  
**Subcategoria:** Debugging de Código  
**Objetivo:** executar Debugging de Código com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver debugging de código em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Engenheiro de Software Sênior, com foco em Debugging de Código.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Debugging de Código para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: correção; legibilidade; coesão; acoplamento; SOLID; padrões; complexidade; testabilidade; manutenção; dívida técnica; segurança; performance.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0110 — Clean Code, SOLID e Design Patterns

**ID:** 0110  
**Nome:** Clean Code, SOLID e Design Patterns  
**Categoria:** Engenharia de Software  
**Subcategoria:** Clean Code, SOLID e Design Patterns  
**Objetivo:** executar Clean Code, SOLID e Design Patterns com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver clean code, solid e design patterns em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Engenheiro de Software Sênior, com foco em Clean Code, SOLID e Design Patterns.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Clean Code, SOLID e Design Patterns para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: correção; legibilidade; coesão; acoplamento; SOLID; padrões; complexidade; testabilidade; manutenção; dívida técnica; segurança; performance.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0201 — Seleção de Estilo Arquitetural

**ID:** 0201  
**Nome:** Seleção de Estilo Arquitetural  
**Categoria:** Arquitetura de Sistemas  
**Subcategoria:** Seleção de Estilo Arquitetural  
**Objetivo:** executar Seleção de Estilo Arquitetural com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver seleção de estilo arquitetural em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Arquiteto de Software / Solutions Architect, com foco em Seleção de Estilo Arquitetural.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Seleção de Estilo Arquitetural para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos funcionais e não funcionais; trade-offs; fronteiras; integração; consistência; disponibilidade; escalabilidade; segurança; custo; operabilidade; DR.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0202 — Domain-Driven Design (DDD)

**ID:** 0202  
**Nome:** Domain-Driven Design (DDD)  
**Categoria:** Arquitetura de Sistemas  
**Subcategoria:** Domain-Driven Design (DDD)  
**Objetivo:** executar Domain-Driven Design (DDD) com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver domain-driven design (ddd) em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Arquiteto de Software / Solutions Architect, com foco em Domain-Driven Design (DDD).

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Domain-Driven Design (DDD) para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos funcionais e não funcionais; trade-offs; fronteiras; integração; consistência; disponibilidade; escalabilidade; segurança; custo; operabilidade; DR.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0203 — Clean Architecture

**ID:** 0203  
**Nome:** Clean Architecture  
**Categoria:** Arquitetura de Sistemas  
**Subcategoria:** Clean Architecture  
**Objetivo:** executar Clean Architecture com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver clean architecture em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Arquiteto de Software / Solutions Architect, com foco em Clean Architecture.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Clean Architecture para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos funcionais e não funcionais; trade-offs; fronteiras; integração; consistência; disponibilidade; escalabilidade; segurança; custo; operabilidade; DR.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0204 — Monólito Modular

**ID:** 0204  
**Nome:** Monólito Modular  
**Categoria:** Arquitetura de Sistemas  
**Subcategoria:** Monólito Modular  
**Objetivo:** executar Monólito Modular com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver monólito modular em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Arquiteto de Software / Solutions Architect, com foco em Monólito Modular.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Monólito Modular para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos funcionais e não funcionais; trade-offs; fronteiras; integração; consistência; disponibilidade; escalabilidade; segurança; custo; operabilidade; DR.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0205 — Microservices

**ID:** 0205  
**Nome:** Microservices  
**Categoria:** Arquitetura de Sistemas  
**Subcategoria:** Microservices  
**Objetivo:** executar Microservices com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver microservices em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Arquiteto de Software / Solutions Architect, com foco em Microservices.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Microservices para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos funcionais e não funcionais; trade-offs; fronteiras; integração; consistência; disponibilidade; escalabilidade; segurança; custo; operabilidade; DR.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0206 — Event-Driven Architecture

**ID:** 0206  
**Nome:** Event-Driven Architecture  
**Categoria:** Arquitetura de Sistemas  
**Subcategoria:** Event-Driven Architecture  
**Objetivo:** executar Event-Driven Architecture com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver event-driven architecture em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Arquiteto de Software / Solutions Architect, com foco em Event-Driven Architecture.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Event-Driven Architecture para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos funcionais e não funcionais; trade-offs; fronteiras; integração; consistência; disponibilidade; escalabilidade; segurança; custo; operabilidade; DR.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0207 — Serverless Architecture

**ID:** 0207  
**Nome:** Serverless Architecture  
**Categoria:** Arquitetura de Sistemas  
**Subcategoria:** Serverless Architecture  
**Objetivo:** executar Serverless Architecture com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver serverless architecture em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Arquiteto de Software / Solutions Architect, com foco em Serverless Architecture.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Serverless Architecture para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos funcionais e não funcionais; trade-offs; fronteiras; integração; consistência; disponibilidade; escalabilidade; segurança; custo; operabilidade; DR.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0208 — SaaS Multi-Tenant

**ID:** 0208  
**Nome:** SaaS Multi-Tenant  
**Categoria:** Arquitetura de Sistemas  
**Subcategoria:** SaaS Multi-Tenant  
**Objetivo:** executar SaaS Multi-Tenant com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver saas multi-tenant em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Arquiteto de Software / Solutions Architect, com foco em SaaS Multi-Tenant.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar SaaS Multi-Tenant para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos funcionais e não funcionais; trade-offs; fronteiras; integração; consistência; disponibilidade; escalabilidade; segurança; custo; operabilidade; DR.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0209 — Alta Disponibilidade e Disaster Recovery

**ID:** 0209  
**Nome:** Alta Disponibilidade e Disaster Recovery  
**Categoria:** Arquitetura de Sistemas  
**Subcategoria:** Alta Disponibilidade e Disaster Recovery  
**Objetivo:** executar Alta Disponibilidade e Disaster Recovery com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver alta disponibilidade e disaster recovery em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Arquiteto de Software / Solutions Architect, com foco em Alta Disponibilidade e Disaster Recovery.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Alta Disponibilidade e Disaster Recovery para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos funcionais e não funcionais; trade-offs; fronteiras; integração; consistência; disponibilidade; escalabilidade; segurança; custo; operabilidade; DR.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0210 — ADR — Architecture Decision Record

**ID:** 0210  
**Nome:** ADR — Architecture Decision Record  
**Categoria:** Arquitetura de Sistemas  
**Subcategoria:** ADR — Architecture Decision Record  
**Objetivo:** executar ADR — Architecture Decision Record com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver adr — architecture decision record em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Arquiteto de Software / Solutions Architect, com foco em ADR — Architecture Decision Record.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar ADR — Architecture Decision Record para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: requisitos funcionais e não funcionais; trade-offs; fronteiras; integração; consistência; disponibilidade; escalabilidade; segurança; custo; operabilidade; DR.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0301 — Node.js + NestJS

**ID:** 0301  
**Nome:** Node.js + NestJS  
**Categoria:** Desenvolvimento Backend  
**Subcategoria:** Node.js + NestJS  
**Objetivo:** executar Node.js + NestJS com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver node.js + nestjs em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Backend Engineer Sênior, com foco em Node.js + NestJS.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Node.js + NestJS para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contratos; validação; domínio; persistência; concorrência; erros; idempotência; segurança; observabilidade; performance; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0302 — Node.js + Express

**ID:** 0302  
**Nome:** Node.js + Express  
**Categoria:** Desenvolvimento Backend  
**Subcategoria:** Node.js + Express  
**Objetivo:** executar Node.js + Express com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver node.js + express em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Backend Engineer Sênior, com foco em Node.js + Express.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Node.js + Express para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contratos; validação; domínio; persistência; concorrência; erros; idempotência; segurança; observabilidade; performance; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0303 — Python + FastAPI

**ID:** 0303  
**Nome:** Python + FastAPI  
**Categoria:** Desenvolvimento Backend  
**Subcategoria:** Python + FastAPI  
**Objetivo:** executar Python + FastAPI com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver python + fastapi em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Backend Engineer Sênior, com foco em Python + FastAPI.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Python + FastAPI para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contratos; validação; domínio; persistência; concorrência; erros; idempotência; segurança; observabilidade; performance; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0304 — Python + Django

**ID:** 0304  
**Nome:** Python + Django  
**Categoria:** Desenvolvimento Backend  
**Subcategoria:** Python + Django  
**Objetivo:** executar Python + Django com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver python + django em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Backend Engineer Sênior, com foco em Python + Django.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Python + Django para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contratos; validação; domínio; persistência; concorrência; erros; idempotência; segurança; observabilidade; performance; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0305 — Java + Spring Boot

**ID:** 0305  
**Nome:** Java + Spring Boot  
**Categoria:** Desenvolvimento Backend  
**Subcategoria:** Java + Spring Boot  
**Objetivo:** executar Java + Spring Boot com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver java + spring boot em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Backend Engineer Sênior, com foco em Java + Spring Boot.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Java + Spring Boot para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contratos; validação; domínio; persistência; concorrência; erros; idempotência; segurança; observabilidade; performance; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0306 — .NET Backend

**ID:** 0306  
**Nome:** .NET Backend  
**Categoria:** Desenvolvimento Backend  
**Subcategoria:** .NET Backend  
**Objetivo:** executar .NET Backend com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver .net backend em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Backend Engineer Sênior, com foco em .NET Backend.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar .NET Backend para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contratos; validação; domínio; persistência; concorrência; erros; idempotência; segurança; observabilidade; performance; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0307 — Go Backend

**ID:** 0307  
**Nome:** Go Backend  
**Categoria:** Desenvolvimento Backend  
**Subcategoria:** Go Backend  
**Objetivo:** executar Go Backend com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver go backend em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Backend Engineer Sênior, com foco em Go Backend.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Go Backend para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contratos; validação; domínio; persistência; concorrência; erros; idempotência; segurança; observabilidade; performance; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0308 — PHP + Laravel

**ID:** 0308  
**Nome:** PHP + Laravel  
**Categoria:** Desenvolvimento Backend  
**Subcategoria:** PHP + Laravel  
**Objetivo:** executar PHP + Laravel com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver php + laravel em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Backend Engineer Sênior, com foco em PHP + Laravel.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar PHP + Laravel para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contratos; validação; domínio; persistência; concorrência; erros; idempotência; segurança; observabilidade; performance; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0309 — Autenticação, Autorização e RBAC

**ID:** 0309  
**Nome:** Autenticação, Autorização e RBAC  
**Categoria:** Desenvolvimento Backend  
**Subcategoria:** Autenticação, Autorização e RBAC  
**Objetivo:** executar Autenticação, Autorização e RBAC com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver autenticação, autorização e rbac em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Backend Engineer Sênior, com foco em Autenticação, Autorização e RBAC.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Autenticação, Autorização e RBAC para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contratos; validação; domínio; persistência; concorrência; erros; idempotência; segurança; observabilidade; performance; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0310 — Filas, Jobs, Webhooks e Cache

**ID:** 0310  
**Nome:** Filas, Jobs, Webhooks e Cache  
**Categoria:** Desenvolvimento Backend  
**Subcategoria:** Filas, Jobs, Webhooks e Cache  
**Objetivo:** executar Filas, Jobs, Webhooks e Cache com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver filas, jobs, webhooks e cache em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Backend Engineer Sênior, com foco em Filas, Jobs, Webhooks e Cache.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Filas, Jobs, Webhooks e Cache para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contratos; validação; domínio; persistência; concorrência; erros; idempotência; segurança; observabilidade; performance; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0401 — React

**ID:** 0401  
**Nome:** React  
**Categoria:** Desenvolvimento Frontend  
**Subcategoria:** React  
**Objetivo:** executar React com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver react em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Frontend Engineer Sênior, com foco em React.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar React para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: UX; acessibilidade; responsividade; estado; performance; erros; segurança; compatibilidade; SEO quando aplicável; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0402 — Next.js

**ID:** 0402  
**Nome:** Next.js  
**Categoria:** Desenvolvimento Frontend  
**Subcategoria:** Next.js  
**Objetivo:** executar Next.js com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver next.js em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Frontend Engineer Sênior, com foco em Next.js.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Next.js para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: UX; acessibilidade; responsividade; estado; performance; erros; segurança; compatibilidade; SEO quando aplicável; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0403 — Vue / Angular

**ID:** 0403  
**Nome:** Vue / Angular  
**Categoria:** Desenvolvimento Frontend  
**Subcategoria:** Vue / Angular  
**Objetivo:** executar Vue / Angular com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver vue / angular em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Frontend Engineer Sênior, com foco em Vue / Angular.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Vue / Angular para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: UX; acessibilidade; responsividade; estado; performance; erros; segurança; compatibilidade; SEO quando aplicável; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0404 — Design System e Componentização

**ID:** 0404  
**Nome:** Design System e Componentização  
**Categoria:** Desenvolvimento Frontend  
**Subcategoria:** Design System e Componentização  
**Objetivo:** executar Design System e Componentização com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver design system e componentização em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Frontend Engineer Sênior, com foco em Design System e Componentização.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Design System e Componentização para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: UX; acessibilidade; responsividade; estado; performance; erros; segurança; compatibilidade; SEO quando aplicável; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0405 — Acessibilidade Web

**ID:** 0405  
**Nome:** Acessibilidade Web  
**Categoria:** Desenvolvimento Frontend  
**Subcategoria:** Acessibilidade Web  
**Objetivo:** executar Acessibilidade Web com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver acessibilidade web em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Frontend Engineer Sênior, com foco em Acessibilidade Web.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Acessibilidade Web para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: UX; acessibilidade; responsividade; estado; performance; erros; segurança; compatibilidade; SEO quando aplicável; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0406 — Performance Frontend

**ID:** 0406  
**Nome:** Performance Frontend  
**Categoria:** Desenvolvimento Frontend  
**Subcategoria:** Performance Frontend  
**Objetivo:** executar Performance Frontend com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver performance frontend em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Frontend Engineer Sênior, com foco em Performance Frontend.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Performance Frontend para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: UX; acessibilidade; responsividade; estado; performance; erros; segurança; compatibilidade; SEO quando aplicável; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0407 — Formulários e Validação

**ID:** 0407  
**Nome:** Formulários e Validação  
**Categoria:** Desenvolvimento Frontend  
**Subcategoria:** Formulários e Validação  
**Objetivo:** executar Formulários e Validação com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver formulários e validação em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Frontend Engineer Sênior, com foco em Formulários e Validação.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Formulários e Validação para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: UX; acessibilidade; responsividade; estado; performance; erros; segurança; compatibilidade; SEO quando aplicável; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0408 — Gerenciamento de Estado

**ID:** 0408  
**Nome:** Gerenciamento de Estado  
**Categoria:** Desenvolvimento Frontend  
**Subcategoria:** Gerenciamento de Estado  
**Objetivo:** executar Gerenciamento de Estado com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver gerenciamento de estado em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Frontend Engineer Sênior, com foco em Gerenciamento de Estado.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Gerenciamento de Estado para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: UX; acessibilidade; responsividade; estado; performance; erros; segurança; compatibilidade; SEO quando aplicável; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0409 — Dashboards e Interfaces de Dados

**ID:** 0409  
**Nome:** Dashboards e Interfaces de Dados  
**Categoria:** Desenvolvimento Frontend  
**Subcategoria:** Dashboards e Interfaces de Dados  
**Objetivo:** executar Dashboards e Interfaces de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver dashboards e interfaces de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Frontend Engineer Sênior, com foco em Dashboards e Interfaces de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Dashboards e Interfaces de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: UX; acessibilidade; responsividade; estado; performance; erros; segurança; compatibilidade; SEO quando aplicável; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0410 — SEO Técnico

**ID:** 0410  
**Nome:** SEO Técnico  
**Categoria:** Desenvolvimento Frontend  
**Subcategoria:** SEO Técnico  
**Objetivo:** executar SEO Técnico com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver seo técnico em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Frontend Engineer Sênior, com foco em SEO Técnico.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar SEO Técnico para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: UX; acessibilidade; responsividade; estado; performance; erros; segurança; compatibilidade; SEO quando aplicável; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0501 — Arquitetura Full Stack

**ID:** 0501  
**Nome:** Arquitetura Full Stack  
**Categoria:** Full Stack e Mobile  
**Subcategoria:** Arquitetura Full Stack  
**Objetivo:** executar Arquitetura Full Stack com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver arquitetura full stack em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Full Stack Engineer Sênior, com foco em Arquitetura Full Stack.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Arquitetura Full Stack para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato ponta a ponta; autenticação; dados; UX; API; persistência; testes; deploy; telemetria; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0502 — Implementação de Feature Ponta a Ponta

**ID:** 0502  
**Nome:** Implementação de Feature Ponta a Ponta  
**Categoria:** Full Stack e Mobile  
**Subcategoria:** Implementação de Feature Ponta a Ponta  
**Objetivo:** executar Implementação de Feature Ponta a Ponta com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver implementação de feature ponta a ponta em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Full Stack Engineer Sênior, com foco em Implementação de Feature Ponta a Ponta.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Implementação de Feature Ponta a Ponta para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato ponta a ponta; autenticação; dados; UX; API; persistência; testes; deploy; telemetria; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0503 — Autenticação Full Stack

**ID:** 0503  
**Nome:** Autenticação Full Stack  
**Categoria:** Full Stack e Mobile  
**Subcategoria:** Autenticação Full Stack  
**Objetivo:** executar Autenticação Full Stack com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver autenticação full stack em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Full Stack Engineer Sênior, com foco em Autenticação Full Stack.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Autenticação Full Stack para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato ponta a ponta; autenticação; dados; UX; API; persistência; testes; deploy; telemetria; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0504 — Monorepo

**ID:** 0504  
**Nome:** Monorepo  
**Categoria:** Full Stack e Mobile  
**Subcategoria:** Monorepo  
**Objetivo:** executar Monorepo com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver monorepo em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Full Stack Engineer Sênior, com foco em Monorepo.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Monorepo para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato ponta a ponta; autenticação; dados; UX; API; persistência; testes; deploy; telemetria; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0505 — Aplicação Mobile

**ID:** 0505  
**Nome:** Aplicação Mobile  
**Categoria:** Full Stack e Mobile  
**Subcategoria:** Aplicação Mobile  
**Objetivo:** executar Aplicação Mobile com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver aplicação mobile em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Full Stack Engineer Sênior, com foco em Aplicação Mobile.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Aplicação Mobile para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato ponta a ponta; autenticação; dados; UX; API; persistência; testes; deploy; telemetria; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0506 — Deploy Full Stack

**ID:** 0506  
**Nome:** Deploy Full Stack  
**Categoria:** Full Stack e Mobile  
**Subcategoria:** Deploy Full Stack  
**Objetivo:** executar Deploy Full Stack com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver deploy full stack em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Full Stack Engineer Sênior, com foco em Deploy Full Stack.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Deploy Full Stack para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato ponta a ponta; autenticação; dados; UX; API; persistência; testes; deploy; telemetria; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0601 — Design de API REST

**ID:** 0601  
**Nome:** Design de API REST  
**Categoria:** APIs e Integrações  
**Subcategoria:** Design de API REST  
**Objetivo:** executar Design de API REST com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver design de api rest em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como API / Integration Architect, com foco em Design de API REST.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Design de API REST para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato; versionamento; autenticação; autorização; idempotência; rate limits; erros; observabilidade; compatibilidade; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0602 — OpenAPI / Swagger

**ID:** 0602  
**Nome:** OpenAPI / Swagger  
**Categoria:** APIs e Integrações  
**Subcategoria:** OpenAPI / Swagger  
**Objetivo:** executar OpenAPI / Swagger com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver openapi / swagger em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como API / Integration Architect, com foco em OpenAPI / Swagger.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar OpenAPI / Swagger para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato; versionamento; autenticação; autorização; idempotência; rate limits; erros; observabilidade; compatibilidade; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0603 — GraphQL

**ID:** 0603  
**Nome:** GraphQL  
**Categoria:** APIs e Integrações  
**Subcategoria:** GraphQL  
**Objetivo:** executar GraphQL com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver graphql em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como API / Integration Architect, com foco em GraphQL.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar GraphQL para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato; versionamento; autenticação; autorização; idempotência; rate limits; erros; observabilidade; compatibilidade; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0604 — OAuth 2.x / OIDC

**ID:** 0604  
**Nome:** OAuth 2.x / OIDC  
**Categoria:** APIs e Integrações  
**Subcategoria:** OAuth 2.x / OIDC  
**Objetivo:** executar OAuth 2.x / OIDC com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver oauth 2.x / oidc em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como API / Integration Architect, com foco em OAuth 2.x / OIDC.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar OAuth 2.x / OIDC para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato; versionamento; autenticação; autorização; idempotência; rate limits; erros; observabilidade; compatibilidade; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0605 — Webhooks Confiáveis

**ID:** 0605  
**Nome:** Webhooks Confiáveis  
**Categoria:** APIs e Integrações  
**Subcategoria:** Webhooks Confiáveis  
**Objetivo:** executar Webhooks Confiáveis com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver webhooks confiáveis em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como API / Integration Architect, com foco em Webhooks Confiáveis.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Webhooks Confiáveis para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato; versionamento; autenticação; autorização; idempotência; rate limits; erros; observabilidade; compatibilidade; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0606 — Integração com Sistema Externo

**ID:** 0606  
**Nome:** Integração com Sistema Externo  
**Categoria:** APIs e Integrações  
**Subcategoria:** Integração com Sistema Externo  
**Objetivo:** executar Integração com Sistema Externo com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver integração com sistema externo em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como API / Integration Architect, com foco em Integração com Sistema Externo.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Integração com Sistema Externo para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato; versionamento; autenticação; autorização; idempotência; rate limits; erros; observabilidade; compatibilidade; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0607 — Revisão de Contrato de API

**ID:** 0607  
**Nome:** Revisão de Contrato de API  
**Categoria:** APIs e Integrações  
**Subcategoria:** Revisão de Contrato de API  
**Objetivo:** executar Revisão de Contrato de API com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver revisão de contrato de api em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como API / Integration Architect, com foco em Revisão de Contrato de API.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Revisão de Contrato de API para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato; versionamento; autenticação; autorização; idempotência; rate limits; erros; observabilidade; compatibilidade; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0608 — Versionamento, Segurança e Testes de API

**ID:** 0608  
**Nome:** Versionamento, Segurança e Testes de API  
**Categoria:** APIs e Integrações  
**Subcategoria:** Versionamento, Segurança e Testes de API  
**Objetivo:** executar Versionamento, Segurança e Testes de API com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver versionamento, segurança e testes de api em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como API / Integration Architect, com foco em Versionamento, Segurança e Testes de API.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Versionamento, Segurança e Testes de API para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: contrato; versionamento; autenticação; autorização; idempotência; rate limits; erros; observabilidade; compatibilidade; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0701 — Modelagem Relacional

**ID:** 0701  
**Nome:** Modelagem Relacional  
**Categoria:** Banco de Dados  
**Subcategoria:** Modelagem Relacional  
**Objetivo:** executar Modelagem Relacional com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver modelagem relacional em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DBA / Database Engineer, com foco em Modelagem Relacional.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Modelagem Relacional para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: modelo; integridade; constraints; índices; plano de execução; concorrência; transações; segurança; backup; restore; HA; monitoramento.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0702 — PostgreSQL Schema Design

**ID:** 0702  
**Nome:** PostgreSQL Schema Design  
**Categoria:** Banco de Dados  
**Subcategoria:** PostgreSQL Schema Design  
**Objetivo:** executar PostgreSQL Schema Design com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver postgresql schema design em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DBA / Database Engineer, com foco em PostgreSQL Schema Design.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar PostgreSQL Schema Design para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: modelo; integridade; constraints; índices; plano de execução; concorrência; transações; segurança; backup; restore; HA; monitoramento.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0703 — Otimização de Queries SQL

**ID:** 0703  
**Nome:** Otimização de Queries SQL  
**Categoria:** Banco de Dados  
**Subcategoria:** Otimização de Queries SQL  
**Objetivo:** executar Otimização de Queries SQL com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver otimização de queries sql em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DBA / Database Engineer, com foco em Otimização de Queries SQL.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Otimização de Queries SQL para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: modelo; integridade; constraints; índices; plano de execução; concorrência; transações; segurança; backup; restore; HA; monitoramento.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0704 — Estratégia de Índices

**ID:** 0704  
**Nome:** Estratégia de Índices  
**Categoria:** Banco de Dados  
**Subcategoria:** Estratégia de Índices  
**Objetivo:** executar Estratégia de Índices com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver estratégia de índices em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DBA / Database Engineer, com foco em Estratégia de Índices.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Estratégia de Índices para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: modelo; integridade; constraints; índices; plano de execução; concorrência; transações; segurança; backup; restore; HA; monitoramento.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0705 — Migrations Seguras

**ID:** 0705  
**Nome:** Migrations Seguras  
**Categoria:** Banco de Dados  
**Subcategoria:** Migrations Seguras  
**Objetivo:** executar Migrations Seguras com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver migrations seguras em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DBA / Database Engineer, com foco em Migrations Seguras.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Migrations Seguras para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: modelo; integridade; constraints; índices; plano de execução; concorrência; transações; segurança; backup; restore; HA; monitoramento.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0706 — Backup, Restore e PITR

**ID:** 0706  
**Nome:** Backup, Restore e PITR  
**Categoria:** Banco de Dados  
**Subcategoria:** Backup, Restore e PITR  
**Objetivo:** executar Backup, Restore e PITR com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver backup, restore e pitr em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DBA / Database Engineer, com foco em Backup, Restore e PITR.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Backup, Restore e PITR para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: modelo; integridade; constraints; índices; plano de execução; concorrência; transações; segurança; backup; restore; HA; monitoramento.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0707 — Replicação e Alta Disponibilidade

**ID:** 0707  
**Nome:** Replicação e Alta Disponibilidade  
**Categoria:** Banco de Dados  
**Subcategoria:** Replicação e Alta Disponibilidade  
**Objetivo:** executar Replicação e Alta Disponibilidade com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver replicação e alta disponibilidade em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DBA / Database Engineer, com foco em Replicação e Alta Disponibilidade.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Replicação e Alta Disponibilidade para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: modelo; integridade; constraints; índices; plano de execução; concorrência; transações; segurança; backup; restore; HA; monitoramento.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0708 — Segurança de Banco de Dados

**ID:** 0708  
**Nome:** Segurança de Banco de Dados  
**Categoria:** Banco de Dados  
**Subcategoria:** Segurança de Banco de Dados  
**Objetivo:** executar Segurança de Banco de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver segurança de banco de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DBA / Database Engineer, com foco em Segurança de Banco de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Segurança de Banco de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: modelo; integridade; constraints; índices; plano de execução; concorrência; transações; segurança; backup; restore; HA; monitoramento.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0709 — MySQL / SQL Server / Oracle

**ID:** 0709  
**Nome:** MySQL / SQL Server / Oracle  
**Categoria:** Banco de Dados  
**Subcategoria:** MySQL / SQL Server / Oracle  
**Objetivo:** executar MySQL / SQL Server / Oracle com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver mysql / sql server / oracle em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DBA / Database Engineer, com foco em MySQL / SQL Server / Oracle.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar MySQL / SQL Server / Oracle para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: modelo; integridade; constraints; índices; plano de execução; concorrência; transações; segurança; backup; restore; HA; monitoramento.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0710 — MongoDB, Redis e NoSQL

**ID:** 0710  
**Nome:** MongoDB, Redis e NoSQL  
**Categoria:** Banco de Dados  
**Subcategoria:** MongoDB, Redis e NoSQL  
**Objetivo:** executar MongoDB, Redis e NoSQL com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver mongodb, redis e nosql em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DBA / Database Engineer, com foco em MongoDB, Redis e NoSQL.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar MongoDB, Redis e NoSQL para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: modelo; integridade; constraints; índices; plano de execução; concorrência; transações; segurança; backup; restore; HA; monitoramento.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0801 — ETL / ELT

**ID:** 0801  
**Nome:** ETL / ELT  
**Categoria:** Data Engineering  
**Subcategoria:** ETL / ELT  
**Objetivo:** executar ETL / ELT com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver etl / elt em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Engineer Sênior, com foco em ETL / ELT.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar ETL / ELT para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: origem; esquema; qualidade; lineage; idempotência; backfill; latência; custo; observabilidade; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0802 — Pipeline de Dados

**ID:** 0802  
**Nome:** Pipeline de Dados  
**Categoria:** Data Engineering  
**Subcategoria:** Pipeline de Dados  
**Objetivo:** executar Pipeline de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver pipeline de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Engineer Sênior, com foco em Pipeline de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Pipeline de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: origem; esquema; qualidade; lineage; idempotência; backfill; latência; custo; observabilidade; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0803 — Qualidade de Dados

**ID:** 0803  
**Nome:** Qualidade de Dados  
**Categoria:** Data Engineering  
**Subcategoria:** Qualidade de Dados  
**Objetivo:** executar Qualidade de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver qualidade de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Engineer Sênior, com foco em Qualidade de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Qualidade de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: origem; esquema; qualidade; lineage; idempotência; backfill; latência; custo; observabilidade; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0804 — Data Lake / Data Warehouse

**ID:** 0804  
**Nome:** Data Lake / Data Warehouse  
**Categoria:** Data Engineering  
**Subcategoria:** Data Lake / Data Warehouse  
**Objetivo:** executar Data Lake / Data Warehouse com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver data lake / data warehouse em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Engineer Sênior, com foco em Data Lake / Data Warehouse.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Data Lake / Data Warehouse para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: origem; esquema; qualidade; lineage; idempotência; backfill; latência; custo; observabilidade; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0805 — Governança e Linhagem

**ID:** 0805  
**Nome:** Governança e Linhagem  
**Categoria:** Data Engineering  
**Subcategoria:** Governança e Linhagem  
**Objetivo:** executar Governança e Linhagem com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver governança e linhagem em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Engineer Sênior, com foco em Governança e Linhagem.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Governança e Linhagem para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: origem; esquema; qualidade; lineage; idempotência; backfill; latência; custo; observabilidade; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0806 — Observabilidade de Dados

**ID:** 0806  
**Nome:** Observabilidade de Dados  
**Categoria:** Data Engineering  
**Subcategoria:** Observabilidade de Dados  
**Objetivo:** executar Observabilidade de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver observabilidade de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Engineer Sênior, com foco em Observabilidade de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Observabilidade de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: origem; esquema; qualidade; lineage; idempotência; backfill; latência; custo; observabilidade; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0901 — Análise Exploratória de Dados

**ID:** 0901  
**Nome:** Análise Exploratória de Dados  
**Categoria:** Data Science e Machine Learning  
**Subcategoria:** Análise Exploratória de Dados  
**Objetivo:** executar Análise Exploratória de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver análise exploratória de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Scientist / ML Engineer, com foco em Análise Exploratória de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Análise Exploratória de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: problema; dados; leakage; split; baseline; métricas; validação; explicabilidade; viés; reproducibilidade; serving; drift.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0902 — Feature Engineering

**ID:** 0902  
**Nome:** Feature Engineering  
**Categoria:** Data Science e Machine Learning  
**Subcategoria:** Feature Engineering  
**Objetivo:** executar Feature Engineering com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver feature engineering em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Scientist / ML Engineer, com foco em Feature Engineering.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Feature Engineering para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: problema; dados; leakage; split; baseline; métricas; validação; explicabilidade; viés; reproducibilidade; serving; drift.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0903 — Seleção de Modelo

**ID:** 0903  
**Nome:** Seleção de Modelo  
**Categoria:** Data Science e Machine Learning  
**Subcategoria:** Seleção de Modelo  
**Objetivo:** executar Seleção de Modelo com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver seleção de modelo em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Scientist / ML Engineer, com foco em Seleção de Modelo.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Seleção de Modelo para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: problema; dados; leakage; split; baseline; métricas; validação; explicabilidade; viés; reproducibilidade; serving; drift.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0904 — Treinamento e Validação

**ID:** 0904  
**Nome:** Treinamento e Validação  
**Categoria:** Data Science e Machine Learning  
**Subcategoria:** Treinamento e Validação  
**Objetivo:** executar Treinamento e Validação com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver treinamento e validação em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Scientist / ML Engineer, com foco em Treinamento e Validação.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Treinamento e Validação para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: problema; dados; leakage; split; baseline; métricas; validação; explicabilidade; viés; reproducibilidade; serving; drift.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0905 — Métricas e Avaliação

**ID:** 0905  
**Nome:** Métricas e Avaliação  
**Categoria:** Data Science e Machine Learning  
**Subcategoria:** Métricas e Avaliação  
**Objetivo:** executar Métricas e Avaliação com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver métricas e avaliação em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Scientist / ML Engineer, com foco em Métricas e Avaliação.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Métricas e Avaliação para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: problema; dados; leakage; split; baseline; métricas; validação; explicabilidade; viés; reproducibilidade; serving; drift.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0906 — NLP

**ID:** 0906  
**Nome:** NLP  
**Categoria:** Data Science e Machine Learning  
**Subcategoria:** NLP  
**Objetivo:** executar NLP com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver nlp em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Scientist / ML Engineer, com foco em NLP.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar NLP para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: problema; dados; leakage; split; baseline; métricas; validação; explicabilidade; viés; reproducibilidade; serving; drift.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0907 — Visão Computacional

**ID:** 0907  
**Nome:** Visão Computacional  
**Categoria:** Data Science e Machine Learning  
**Subcategoria:** Visão Computacional  
**Objetivo:** executar Visão Computacional com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver visão computacional em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Scientist / ML Engineer, com foco em Visão Computacional.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Visão Computacional para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: problema; dados; leakage; split; baseline; métricas; validação; explicabilidade; viés; reproducibilidade; serving; drift.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 0908 — MLOps

**ID:** 0908  
**Nome:** MLOps  
**Categoria:** Data Science e Machine Learning  
**Subcategoria:** MLOps  
**Objetivo:** executar MLOps com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver mlops em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Data Scientist / ML Engineer, com foco em MLOps.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar MLOps para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: problema; dados; leakage; split; baseline; métricas; validação; explicabilidade; viés; reproducibilidade; serving; drift.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1001 — Power BI

**ID:** 1001  
**Nome:** Power BI  
**Categoria:** Business Intelligence  
**Subcategoria:** Power BI  
**Objetivo:** executar Power BI com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver power bi em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como BI / Analytics Engineer, com foco em Power BI.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Power BI para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo de negócio; semântica; métricas; granularidade; fonte; qualidade; filtros; UX; performance; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1002 — KPIs e Métricas

**ID:** 1002  
**Nome:** KPIs e Métricas  
**Categoria:** Business Intelligence  
**Subcategoria:** KPIs e Métricas  
**Objetivo:** executar KPIs e Métricas com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver kpis e métricas em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Intermediário  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como BI / Analytics Engineer, com foco em KPIs e Métricas.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar KPIs e Métricas para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo de negócio; semântica; métricas; granularidade; fonte; qualidade; filtros; UX; performance; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1003 — SQL Analítico

**ID:** 1003  
**Nome:** SQL Analítico  
**Categoria:** Business Intelligence  
**Subcategoria:** SQL Analítico  
**Objetivo:** executar SQL Analítico com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver sql analítico em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como BI / Analytics Engineer, com foco em SQL Analítico.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar SQL Analítico para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo de negócio; semântica; métricas; granularidade; fonte; qualidade; filtros; UX; performance; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1004 — Dashboard Executivo

**ID:** 1004  
**Nome:** Dashboard Executivo  
**Categoria:** Business Intelligence  
**Subcategoria:** Dashboard Executivo  
**Objetivo:** executar Dashboard Executivo com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver dashboard executivo em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como BI / Analytics Engineer, com foco em Dashboard Executivo.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Dashboard Executivo para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo de negócio; semântica; métricas; granularidade; fonte; qualidade; filtros; UX; performance; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1005 — Qualidade e Governança de BI

**ID:** 1005  
**Nome:** Qualidade e Governança de BI  
**Categoria:** Business Intelligence  
**Subcategoria:** Qualidade e Governança de BI  
**Objetivo:** executar Qualidade e Governança de BI com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver qualidade e governança de bi em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como BI / Analytics Engineer, com foco em Qualidade e Governança de BI.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Qualidade e Governança de BI para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo de negócio; semântica; métricas; granularidade; fonte; qualidade; filtros; UX; performance; governança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1101 — Estratégia CI/CD

**ID:** 1101  
**Nome:** Estratégia CI/CD  
**Categoria:** DevOps e CI/CD  
**Subcategoria:** Estratégia CI/CD  
**Objetivo:** executar Estratégia CI/CD com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver estratégia ci/cd em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DevOps Engineer Sênior, com foco em Estratégia CI/CD.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Estratégia CI/CD para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: build; test gates; artefatos; ambientes; secrets; supply chain; deploy; rollback; approvals; logs; confiabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1102 — GitHub Actions

**ID:** 1102  
**Nome:** GitHub Actions  
**Categoria:** DevOps e CI/CD  
**Subcategoria:** GitHub Actions  
**Objetivo:** executar GitHub Actions com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver github actions em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DevOps Engineer Sênior, com foco em GitHub Actions.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar GitHub Actions para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: build; test gates; artefatos; ambientes; secrets; supply chain; deploy; rollback; approvals; logs; confiabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1103 — GitLab CI

**ID:** 1103  
**Nome:** GitLab CI  
**Categoria:** DevOps e CI/CD  
**Subcategoria:** GitLab CI  
**Objetivo:** executar GitLab CI com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver gitlab ci em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DevOps Engineer Sênior, com foco em GitLab CI.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar GitLab CI para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: build; test gates; artefatos; ambientes; secrets; supply chain; deploy; rollback; approvals; logs; confiabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1104 — Ambientes, Secrets e Variáveis

**ID:** 1104  
**Nome:** Ambientes, Secrets e Variáveis  
**Categoria:** DevOps e CI/CD  
**Subcategoria:** Ambientes, Secrets e Variáveis  
**Objetivo:** executar Ambientes, Secrets e Variáveis com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver ambientes, secrets e variáveis em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DevOps Engineer Sênior, com foco em Ambientes, Secrets e Variáveis.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Ambientes, Secrets e Variáveis para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: build; test gates; artefatos; ambientes; secrets; supply chain; deploy; rollback; approvals; logs; confiabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1105 — Deploy e Rollback

**ID:** 1105  
**Nome:** Deploy e Rollback  
**Categoria:** DevOps e CI/CD  
**Subcategoria:** Deploy e Rollback  
**Objetivo:** executar Deploy e Rollback com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver deploy e rollback em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DevOps Engineer Sênior, com foco em Deploy e Rollback.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Deploy e Rollback para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: build; test gates; artefatos; ambientes; secrets; supply chain; deploy; rollback; approvals; logs; confiabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1106 — Estratégia de Release

**ID:** 1106  
**Nome:** Estratégia de Release  
**Categoria:** DevOps e CI/CD  
**Subcategoria:** Estratégia de Release  
**Objetivo:** executar Estratégia de Release com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver estratégia de release em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DevOps Engineer Sênior, com foco em Estratégia de Release.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Estratégia de Release para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: build; test gates; artefatos; ambientes; secrets; supply chain; deploy; rollback; approvals; logs; confiabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1107 — Segurança de Pipeline

**ID:** 1107  
**Nome:** Segurança de Pipeline  
**Categoria:** DevOps e CI/CD  
**Subcategoria:** Segurança de Pipeline  
**Objetivo:** executar Segurança de Pipeline com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver segurança de pipeline em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DevOps Engineer Sênior, com foco em Segurança de Pipeline.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Segurança de Pipeline para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: build; test gates; artefatos; ambientes; secrets; supply chain; deploy; rollback; approvals; logs; confiabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1108 — Troubleshooting de Pipeline

**ID:** 1108  
**Nome:** Troubleshooting de Pipeline  
**Categoria:** DevOps e CI/CD  
**Subcategoria:** Troubleshooting de Pipeline  
**Objetivo:** executar Troubleshooting de Pipeline com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver troubleshooting de pipeline em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como DevOps Engineer Sênior, com foco em Troubleshooting de Pipeline.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Troubleshooting de Pipeline para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: build; test gates; artefatos; ambientes; secrets; supply chain; deploy; rollback; approvals; logs; confiabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1201 — Dockerfile de Produção

**ID:** 1201  
**Nome:** Dockerfile de Produção  
**Categoria:** Containers e Kubernetes  
**Subcategoria:** Dockerfile de Produção  
**Objetivo:** executar Dockerfile de Produção com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver dockerfile de produção em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform / Kubernetes Engineer, com foco em Dockerfile de Produção.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Dockerfile de Produção para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: imagem; least privilege; recursos; probes; networking; secrets; RBAC; policies; HA; scaling; observabilidade; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1202 — Docker Compose

**ID:** 1202  
**Nome:** Docker Compose  
**Categoria:** Containers e Kubernetes  
**Subcategoria:** Docker Compose  
**Objetivo:** executar Docker Compose com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver docker compose em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform / Kubernetes Engineer, com foco em Docker Compose.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Docker Compose para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: imagem; least privilege; recursos; probes; networking; secrets; RBAC; policies; HA; scaling; observabilidade; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1203 — Segurança Docker

**ID:** 1203  
**Nome:** Segurança Docker  
**Categoria:** Containers e Kubernetes  
**Subcategoria:** Segurança Docker  
**Objetivo:** executar Segurança Docker com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver segurança docker em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform / Kubernetes Engineer, com foco em Segurança Docker.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Segurança Docker para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: imagem; least privilege; recursos; probes; networking; secrets; RBAC; policies; HA; scaling; observabilidade; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1204 — Deployment Kubernetes

**ID:** 1204  
**Nome:** Deployment Kubernetes  
**Categoria:** Containers e Kubernetes  
**Subcategoria:** Deployment Kubernetes  
**Objetivo:** executar Deployment Kubernetes com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver deployment kubernetes em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform / Kubernetes Engineer, com foco em Deployment Kubernetes.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Deployment Kubernetes para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: imagem; least privilege; recursos; probes; networking; secrets; RBAC; policies; HA; scaling; observabilidade; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1205 — Segurança Kubernetes

**ID:** 1205  
**Nome:** Segurança Kubernetes  
**Categoria:** Containers e Kubernetes  
**Subcategoria:** Segurança Kubernetes  
**Objetivo:** executar Segurança Kubernetes com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver segurança kubernetes em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform / Kubernetes Engineer, com foco em Segurança Kubernetes.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Segurança Kubernetes para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: imagem; least privilege; recursos; probes; networking; secrets; RBAC; policies; HA; scaling; observabilidade; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1206 — Helm

**ID:** 1206  
**Nome:** Helm  
**Categoria:** Containers e Kubernetes  
**Subcategoria:** Helm  
**Objetivo:** executar Helm com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver helm em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform / Kubernetes Engineer, com foco em Helm.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Helm para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: imagem; least privilege; recursos; probes; networking; secrets; RBAC; policies; HA; scaling; observabilidade; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1207 — Observabilidade Kubernetes

**ID:** 1207  
**Nome:** Observabilidade Kubernetes  
**Categoria:** Containers e Kubernetes  
**Subcategoria:** Observabilidade Kubernetes  
**Objetivo:** executar Observabilidade Kubernetes com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver observabilidade kubernetes em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform / Kubernetes Engineer, com foco em Observabilidade Kubernetes.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Observabilidade Kubernetes para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: imagem; least privilege; recursos; probes; networking; secrets; RBAC; policies; HA; scaling; observabilidade; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1208 — Escalabilidade e Resiliência Kubernetes

**ID:** 1208  
**Nome:** Escalabilidade e Resiliência Kubernetes  
**Categoria:** Containers e Kubernetes  
**Subcategoria:** Escalabilidade e Resiliência Kubernetes  
**Objetivo:** executar Escalabilidade e Resiliência Kubernetes com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver escalabilidade e resiliência kubernetes em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform / Kubernetes Engineer, com foco em Escalabilidade e Resiliência Kubernetes.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Escalabilidade e Resiliência Kubernetes para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: imagem; least privilege; recursos; probes; networking; secrets; RBAC; policies; HA; scaling; observabilidade; rollback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1301 — Terraform

**ID:** 1301  
**Nome:** Terraform  
**Categoria:** IaC e Automação  
**Subcategoria:** Terraform  
**Objetivo:** executar Terraform com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver terraform em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Infrastructure Automation Engineer, com foco em Terraform.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Terraform para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: idempotência; estado; módulos; inputs; secrets; validação; drift; rollback; logs; segurança; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1302 — Auditoria de Infrastructure as Code

**ID:** 1302  
**Nome:** Auditoria de Infrastructure as Code  
**Categoria:** IaC e Automação  
**Subcategoria:** Auditoria de Infrastructure as Code  
**Objetivo:** executar Auditoria de Infrastructure as Code com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de infrastructure as code em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Infrastructure Automation Engineer, com foco em Auditoria de Infrastructure as Code.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Infrastructure as Code para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: idempotência; estado; módulos; inputs; secrets; validação; drift; rollback; logs; segurança; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1303 — Automação Bash

**ID:** 1303  
**Nome:** Automação Bash  
**Categoria:** IaC e Automação  
**Subcategoria:** Automação Bash  
**Objetivo:** executar Automação Bash com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver automação bash em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Infrastructure Automation Engineer, com foco em Automação Bash.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Automação Bash para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: idempotência; estado; módulos; inputs; secrets; validação; drift; rollback; logs; segurança; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1304 — Automação PowerShell

**ID:** 1304  
**Nome:** Automação PowerShell  
**Categoria:** IaC e Automação  
**Subcategoria:** Automação PowerShell  
**Objetivo:** executar Automação PowerShell com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver automação powershell em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Infrastructure Automation Engineer, com foco em Automação PowerShell.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Automação PowerShell para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: idempotência; estado; módulos; inputs; secrets; validação; drift; rollback; logs; segurança; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1305 — Cron e Jobs Agendados

**ID:** 1305  
**Nome:** Cron e Jobs Agendados  
**Categoria:** IaC e Automação  
**Subcategoria:** Cron e Jobs Agendados  
**Objetivo:** executar Cron e Jobs Agendados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver cron e jobs agendados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Infrastructure Automation Engineer, com foco em Cron e Jobs Agendados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Cron e Jobs Agendados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: idempotência; estado; módulos; inputs; secrets; validação; drift; rollback; logs; segurança; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1306 — RPA

**ID:** 1306  
**Nome:** RPA  
**Categoria:** IaC e Automação  
**Subcategoria:** RPA  
**Objetivo:** executar RPA com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver rpa em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Infrastructure Automation Engineer, com foco em RPA.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar RPA para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: idempotência; estado; módulos; inputs; secrets; validação; drift; rollback; logs; segurança; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1307 — Workflow de Automação

**ID:** 1307  
**Nome:** Workflow de Automação  
**Categoria:** IaC e Automação  
**Subcategoria:** Workflow de Automação  
**Objetivo:** executar Workflow de Automação com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver workflow de automação em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Infrastructure Automation Engineer, com foco em Workflow de Automação.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Workflow de Automação para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: idempotência; estado; módulos; inputs; secrets; validação; drift; rollback; logs; segurança; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1308 — Automação com Agentes de IA

**ID:** 1308  
**Nome:** Automação com Agentes de IA  
**Categoria:** IaC e Automação  
**Subcategoria:** Automação com Agentes de IA  
**Objetivo:** executar Automação com Agentes de IA com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver automação com agentes de ia em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Infrastructure Automation Engineer, com foco em Automação com Agentes de IA.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Automação com Agentes de IA para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: idempotência; estado; módulos; inputs; secrets; validação; drift; rollback; logs; segurança; testes.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1401 — Comparação AWS vs Azure vs GCP

**ID:** 1401  
**Nome:** Comparação AWS vs Azure vs GCP  
**Categoria:** Cloud Computing  
**Subcategoria:** Comparação AWS vs Azure vs GCP  
**Objetivo:** executar Comparação AWS vs Azure vs GCP com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver comparação aws vs azure vs gcp em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Cloud Architect, com foco em Comparação AWS vs Azure vs GCP.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Comparação AWS vs Azure vs GCP para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: reliability; security; performance; cost; operational excellence; sustentabilidade quando aplicável; HA; DR; observabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1402 — Arquitetura AWS

**ID:** 1402  
**Nome:** Arquitetura AWS  
**Categoria:** Cloud Computing  
**Subcategoria:** Arquitetura AWS  
**Objetivo:** executar Arquitetura AWS com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver arquitetura aws em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Cloud Architect, com foco em Arquitetura AWS.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Arquitetura AWS para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: reliability; security; performance; cost; operational excellence; sustentabilidade quando aplicável; HA; DR; observabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1403 — Arquitetura Azure

**ID:** 1403  
**Nome:** Arquitetura Azure  
**Categoria:** Cloud Computing  
**Subcategoria:** Arquitetura Azure  
**Objetivo:** executar Arquitetura Azure com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver arquitetura azure em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Cloud Architect, com foco em Arquitetura Azure.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Arquitetura Azure para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: reliability; security; performance; cost; operational excellence; sustentabilidade quando aplicável; HA; DR; observabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1404 — Arquitetura Google Cloud

**ID:** 1404  
**Nome:** Arquitetura Google Cloud  
**Categoria:** Cloud Computing  
**Subcategoria:** Arquitetura Google Cloud  
**Objetivo:** executar Arquitetura Google Cloud com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver arquitetura google cloud em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Cloud Architect, com foco em Arquitetura Google Cloud.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Arquitetura Google Cloud para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: reliability; security; performance; cost; operational excellence; sustentabilidade quando aplicável; HA; DR; observabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1405 — Vercel

**ID:** 1405  
**Nome:** Vercel  
**Categoria:** Cloud Computing  
**Subcategoria:** Vercel  
**Objetivo:** executar Vercel com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver vercel em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Cloud Architect, com foco em Vercel.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Vercel para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: reliability; security; performance; cost; operational excellence; sustentabilidade quando aplicável; HA; DR; observabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1406 — Cloudflare

**ID:** 1406  
**Nome:** Cloudflare  
**Categoria:** Cloud Computing  
**Subcategoria:** Cloudflare  
**Objetivo:** executar Cloudflare com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver cloudflare em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Cloud Architect, com foco em Cloudflare.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Cloudflare para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: reliability; security; performance; cost; operational excellence; sustentabilidade quando aplicável; HA; DR; observabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1407 — Netlify / Render / Railway

**ID:** 1407  
**Nome:** Netlify / Render / Railway  
**Categoria:** Cloud Computing  
**Subcategoria:** Netlify / Render / Railway  
**Objetivo:** executar Netlify / Render / Railway com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver netlify / render / railway em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Cloud Architect, com foco em Netlify / Render / Railway.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Netlify / Render / Railway para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: reliability; security; performance; cost; operational excellence; sustentabilidade quando aplicável; HA; DR; observabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1408 — Neon / Supabase

**ID:** 1408  
**Nome:** Neon / Supabase  
**Categoria:** Cloud Computing  
**Subcategoria:** Neon / Supabase  
**Objetivo:** executar Neon / Supabase com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver neon / supabase em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Cloud Architect, com foco em Neon / Supabase.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Neon / Supabase para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: reliability; security; performance; cost; operational excellence; sustentabilidade quando aplicável; HA; DR; observabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1501 — Auditoria AppSec

**ID:** 1501  
**Nome:** Auditoria AppSec  
**Categoria:** Segurança da Informação  
**Subcategoria:** Auditoria AppSec  
**Objetivo:** executar Auditoria AppSec com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria appsec em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Security Engineer / AppSec / DevSecOps, com foco em Auditoria AppSec.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria AppSec para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: threat model; least privilege; autenticação; autorização; secrets; criptografia; validação; logging; supply chain; incident response; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1502 — Threat Modeling e OWASP

**ID:** 1502  
**Nome:** Threat Modeling e OWASP  
**Categoria:** Segurança da Informação  
**Subcategoria:** Threat Modeling e OWASP  
**Objetivo:** executar Threat Modeling e OWASP com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver threat modeling e owasp em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Security Engineer / AppSec / DevSecOps, com foco em Threat Modeling e OWASP.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Threat Modeling e OWASP para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: threat model; least privilege; autenticação; autorização; secrets; criptografia; validação; logging; supply chain; incident response; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1503 — Gestão de Secrets

**ID:** 1503  
**Nome:** Gestão de Secrets  
**Categoria:** Segurança da Informação  
**Subcategoria:** Gestão de Secrets  
**Objetivo:** executar Gestão de Secrets com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver gestão de secrets em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Security Engineer / AppSec / DevSecOps, com foco em Gestão de Secrets.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Gestão de Secrets para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: threat model; least privilege; autenticação; autorização; secrets; criptografia; validação; logging; supply chain; incident response; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1504 — IAM e Least Privilege

**ID:** 1504  
**Nome:** IAM e Least Privilege  
**Categoria:** Segurança da Informação  
**Subcategoria:** IAM e Least Privilege  
**Objetivo:** executar IAM e Least Privilege com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver iam e least privilege em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Security Engineer / AppSec / DevSecOps, com foco em IAM e Least Privilege.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar IAM e Least Privilege para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: threat model; least privilege; autenticação; autorização; secrets; criptografia; validação; logging; supply chain; incident response; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1505 — Segurança de APIs

**ID:** 1505  
**Nome:** Segurança de APIs  
**Categoria:** Segurança da Informação  
**Subcategoria:** Segurança de APIs  
**Objetivo:** executar Segurança de APIs com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver segurança de apis em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Security Engineer / AppSec / DevSecOps, com foco em Segurança de APIs.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Segurança de APIs para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: threat model; least privilege; autenticação; autorização; secrets; criptografia; validação; logging; supply chain; incident response; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1506 — Segurança de Banco de Dados

**ID:** 1506  
**Nome:** Segurança de Banco de Dados  
**Categoria:** Segurança da Informação  
**Subcategoria:** Segurança de Banco de Dados  
**Objetivo:** executar Segurança de Banco de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver segurança de banco de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Security Engineer / AppSec / DevSecOps, com foco em Segurança de Banco de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Segurança de Banco de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: threat model; least privilege; autenticação; autorização; secrets; criptografia; validação; logging; supply chain; incident response; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1507 — Hardening de Infraestrutura

**ID:** 1507  
**Nome:** Hardening de Infraestrutura  
**Categoria:** Segurança da Informação  
**Subcategoria:** Hardening de Infraestrutura  
**Objetivo:** executar Hardening de Infraestrutura com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver hardening de infraestrutura em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Security Engineer / AppSec / DevSecOps, com foco em Hardening de Infraestrutura.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Hardening de Infraestrutura para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: threat model; least privilege; autenticação; autorização; secrets; criptografia; validação; logging; supply chain; incident response; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1508 — Resposta a Incidentes de Segurança

**ID:** 1508  
**Nome:** Resposta a Incidentes de Segurança  
**Categoria:** Segurança da Informação  
**Subcategoria:** Resposta a Incidentes de Segurança  
**Objetivo:** executar Resposta a Incidentes de Segurança com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver resposta a incidentes de segurança em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Security Engineer / AppSec / DevSecOps, com foco em Resposta a Incidentes de Segurança.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Resposta a Incidentes de Segurança para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: threat model; least privilege; autenticação; autorização; secrets; criptografia; validação; logging; supply chain; incident response; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1509 — Secure Code Review

**ID:** 1509  
**Nome:** Secure Code Review  
**Categoria:** Segurança da Informação  
**Subcategoria:** Secure Code Review  
**Objetivo:** executar Secure Code Review com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver secure code review em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Security Engineer / AppSec / DevSecOps, com foco em Secure Code Review.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Secure Code Review para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: threat model; least privilege; autenticação; autorização; secrets; criptografia; validação; logging; supply chain; incident response; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1510 — Dependências e Software Supply Chain

**ID:** 1510  
**Nome:** Dependências e Software Supply Chain  
**Categoria:** Segurança da Informação  
**Subcategoria:** Dependências e Software Supply Chain  
**Objetivo:** executar Dependências e Software Supply Chain com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver dependências e software supply chain em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Security Engineer / AppSec / DevSecOps, com foco em Dependências e Software Supply Chain.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Dependências e Software Supply Chain para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: threat model; least privilege; autenticação; autorização; secrets; criptografia; validação; logging; supply chain; incident response; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1601 — Estratégia de Testes

**ID:** 1601  
**Nome:** Estratégia de Testes  
**Categoria:** QA e Testes  
**Subcategoria:** Estratégia de Testes  
**Objetivo:** executar Estratégia de Testes com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver estratégia de testes em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como QA / Test Automation Engineer, com foco em Estratégia de Testes.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Estratégia de Testes para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: risco; pirâmide de testes; isolamento; determinismo; dados de teste; cobertura útil; casos negativos; flakiness; CI; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 1602 — Testes Unitários

**ID:** 1602  
**Nome:** Testes Unitários  
**Categoria:** QA e Testes  
**Subcategoria:** Testes Unitários  
**Objetivo:** executar Testes Unitários com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver testes unitários em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como QA / Test Automation Engineer, com foco em Testes Unitários.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Testes Unitários para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: risco; pirâmide de testes; isolamento; determinismo; dados de teste; cobertura útil; casos negativos; flakiness; CI; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 1603 — Testes de Integração

**ID:** 1603  
**Nome:** Testes de Integração  
**Categoria:** QA e Testes  
**Subcategoria:** Testes de Integração  
**Objetivo:** executar Testes de Integração com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver testes de integração em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como QA / Test Automation Engineer, com foco em Testes de Integração.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Testes de Integração para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: risco; pirâmide de testes; isolamento; determinismo; dados de teste; cobertura útil; casos negativos; flakiness; CI; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 1604 — E2E com Playwright

**ID:** 1604  
**Nome:** E2E com Playwright  
**Categoria:** QA e Testes  
**Subcategoria:** E2E com Playwright  
**Objetivo:** executar E2E com Playwright com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver e2e com playwright em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como QA / Test Automation Engineer, com foco em E2E com Playwright.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar E2E com Playwright para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: risco; pirâmide de testes; isolamento; determinismo; dados de teste; cobertura útil; casos negativos; flakiness; CI; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 1605 — E2E com Cypress

**ID:** 1605  
**Nome:** E2E com Cypress  
**Categoria:** QA e Testes  
**Subcategoria:** E2E com Cypress  
**Objetivo:** executar E2E com Cypress com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver e2e com cypress em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como QA / Test Automation Engineer, com foco em E2E com Cypress.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar E2E com Cypress para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: risco; pirâmide de testes; isolamento; determinismo; dados de teste; cobertura útil; casos negativos; flakiness; CI; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 1606 — Testes de API / Postman

**ID:** 1606  
**Nome:** Testes de API / Postman  
**Categoria:** QA e Testes  
**Subcategoria:** Testes de API / Postman  
**Objetivo:** executar Testes de API / Postman com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver testes de api / postman em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como QA / Test Automation Engineer, com foco em Testes de API / Postman.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Testes de API / Postman para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: risco; pirâmide de testes; isolamento; determinismo; dados de teste; cobertura útil; casos negativos; flakiness; CI; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 1607 — Carga e Performance

**ID:** 1607  
**Nome:** Carga e Performance  
**Categoria:** QA e Testes  
**Subcategoria:** Carga e Performance  
**Objetivo:** executar Carga e Performance com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver carga e performance em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como QA / Test Automation Engineer, com foco em Carga e Performance.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Carga e Performance para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: risco; pirâmide de testes; isolamento; determinismo; dados de teste; cobertura útil; casos negativos; flakiness; CI; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 1608 — Testes de Segurança

**ID:** 1608  
**Nome:** Testes de Segurança  
**Categoria:** QA e Testes  
**Subcategoria:** Testes de Segurança  
**Objetivo:** executar Testes de Segurança com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver testes de segurança em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como QA / Test Automation Engineer, com foco em Testes de Segurança.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Testes de Segurança para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: risco; pirâmide de testes; isolamento; determinismo; dados de teste; cobertura útil; casos negativos; flakiness; CI; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 1609 — Cobertura e Qualidade

**ID:** 1609  
**Nome:** Cobertura e Qualidade  
**Categoria:** QA e Testes  
**Subcategoria:** Cobertura e Qualidade  
**Objetivo:** executar Cobertura e Qualidade com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver cobertura e qualidade em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como QA / Test Automation Engineer, com foco em Cobertura e Qualidade.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Cobertura e Qualidade para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: risco; pirâmide de testes; isolamento; determinismo; dados de teste; cobertura útil; casos negativos; flakiness; CI; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 1610 — Edge Cases e Testes Negativos

**ID:** 1610  
**Nome:** Edge Cases e Testes Negativos  
**Categoria:** QA e Testes  
**Subcategoria:** Edge Cases e Testes Negativos  
**Objetivo:** executar Edge Cases e Testes Negativos com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver edge cases e testes negativos em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como QA / Test Automation Engineer, com foco em Edge Cases e Testes Negativos.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Edge Cases e Testes Negativos para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: risco; pirâmide de testes; isolamento; determinismo; dados de teste; cobertura útil; casos negativos; flakiness; CI; evidências.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0020 — Release Readiness / Go-No-Go.

---

### PROMPT 1701 — Engenharia de Prompts Profissional

**ID:** 1701  
**Nome:** Engenharia de Prompts Profissional  
**Categoria:** Inteligência Artificial e LLM  
**Subcategoria:** Engenharia de Prompts Profissional  
**Objetivo:** executar Engenharia de Prompts Profissional com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver engenharia de prompts profissional em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como AI Engineer / Prompt Engineer, com foco em Engenharia de Prompts Profissional.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Engenharia de Prompts Profissional para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; contexto; instruções; ferramentas; grounding; segurança; prompt injection; evals; observabilidade; custo; fallback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 1710 — Evals e Regressão de LLM.

---

### PROMPT 1702 — Avaliação e Otimização de Prompt

**ID:** 1702  
**Nome:** Avaliação e Otimização de Prompt  
**Categoria:** Inteligência Artificial e LLM  
**Subcategoria:** Avaliação e Otimização de Prompt  
**Objetivo:** executar Avaliação e Otimização de Prompt com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver avaliação e otimização de prompt em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como AI Engineer / Prompt Engineer, com foco em Avaliação e Otimização de Prompt.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Avaliação e Otimização de Prompt para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; contexto; instruções; ferramentas; grounding; segurança; prompt injection; evals; observabilidade; custo; fallback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 1710 — Evals e Regressão de LLM.

---

### PROMPT 1703 — RAG

**ID:** 1703  
**Nome:** RAG  
**Categoria:** Inteligência Artificial e LLM  
**Subcategoria:** RAG  
**Objetivo:** executar RAG com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver rag em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como AI Engineer / Prompt Engineer, com foco em RAG.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar RAG para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; contexto; instruções; ferramentas; grounding; segurança; prompt injection; evals; observabilidade; custo; fallback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 1710 — Evals e Regressão de LLM.

---

### PROMPT 1704 — Agentes de IA

**ID:** 1704  
**Nome:** Agentes de IA  
**Categoria:** Inteligência Artificial e LLM  
**Subcategoria:** Agentes de IA  
**Objetivo:** executar Agentes de IA com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver agentes de ia em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como AI Engineer / Prompt Engineer, com foco em Agentes de IA.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Agentes de IA para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; contexto; instruções; ferramentas; grounding; segurança; prompt injection; evals; observabilidade; custo; fallback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 1710 — Evals e Regressão de LLM.

---

### PROMPT 1705 — Function Calling / Tool Calling

**ID:** 1705  
**Nome:** Function Calling / Tool Calling  
**Categoria:** Inteligência Artificial e LLM  
**Subcategoria:** Function Calling / Tool Calling  
**Objetivo:** executar Function Calling / Tool Calling com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver function calling / tool calling em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como AI Engineer / Prompt Engineer, com foco em Function Calling / Tool Calling.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Function Calling / Tool Calling para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; contexto; instruções; ferramentas; grounding; segurança; prompt injection; evals; observabilidade; custo; fallback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 1710 — Evals e Regressão de LLM.

---

### PROMPT 1706 — Embeddings e Vector Databases

**ID:** 1706  
**Nome:** Embeddings e Vector Databases  
**Categoria:** Inteligência Artificial e LLM  
**Subcategoria:** Embeddings e Vector Databases  
**Objetivo:** executar Embeddings e Vector Databases com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver embeddings e vector databases em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como AI Engineer / Prompt Engineer, com foco em Embeddings e Vector Databases.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Embeddings e Vector Databases para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; contexto; instruções; ferramentas; grounding; segurança; prompt injection; evals; observabilidade; custo; fallback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 1710 — Evals e Regressão de LLM.

---

### PROMPT 1707 — Análise de Documentos com IA

**ID:** 1707  
**Nome:** Análise de Documentos com IA  
**Categoria:** Inteligência Artificial e LLM  
**Subcategoria:** Análise de Documentos com IA  
**Objetivo:** executar Análise de Documentos com IA com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver análise de documentos com ia em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como AI Engineer / Prompt Engineer, com foco em Análise de Documentos com IA.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Análise de Documentos com IA para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; contexto; instruções; ferramentas; grounding; segurança; prompt injection; evals; observabilidade; custo; fallback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 1710 — Evals e Regressão de LLM.

---

### PROMPT 1708 — Classificação e Extração de Dados

**ID:** 1708  
**Nome:** Classificação e Extração de Dados  
**Categoria:** Inteligência Artificial e LLM  
**Subcategoria:** Classificação e Extração de Dados  
**Objetivo:** executar Classificação e Extração de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver classificação e extração de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como AI Engineer / Prompt Engineer, com foco em Classificação e Extração de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Classificação e Extração de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; contexto; instruções; ferramentas; grounding; segurança; prompt injection; evals; observabilidade; custo; fallback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 1710 — Evals e Regressão de LLM.

---

### PROMPT 1709 — Segurança contra Prompt Injection

**ID:** 1709  
**Nome:** Segurança contra Prompt Injection  
**Categoria:** Inteligência Artificial e LLM  
**Subcategoria:** Segurança contra Prompt Injection  
**Objetivo:** executar Segurança contra Prompt Injection com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver segurança contra prompt injection em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como AI Engineer / Prompt Engineer, com foco em Segurança contra Prompt Injection.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Segurança contra Prompt Injection para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; contexto; instruções; ferramentas; grounding; segurança; prompt injection; evals; observabilidade; custo; fallback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 1710 — Evals e Regressão de LLM.

---

### PROMPT 1710 — Evals e Regressão de LLM

**ID:** 1710  
**Nome:** Evals e Regressão de LLM  
**Categoria:** Inteligência Artificial e LLM  
**Subcategoria:** Evals e Regressão de LLM  
**Objetivo:** executar Evals e Regressão de LLM com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver evals e regressão de llm em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como AI Engineer / Prompt Engineer, com foco em Evals e Regressão de LLM.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Evals e Regressão de LLM para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; contexto; instruções; ferramentas; grounding; segurança; prompt injection; evals; observabilidade; custo; fallback.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 1710 — Evals e Regressão de LLM.

---

### PROMPT 1801 — Troubleshooting TCP/IP

**ID:** 1801  
**Nome:** Troubleshooting TCP/IP  
**Categoria:** Redes  
**Subcategoria:** Troubleshooting TCP/IP  
**Objetivo:** executar Troubleshooting TCP/IP com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver troubleshooting tcp/ip em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Network Engineer, com foco em Troubleshooting TCP/IP.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Troubleshooting TCP/IP para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: camadas; DNS; rotas; ACL/firewall; TLS; MTU; latência; perda; captura de evidências; mudanças reversíveis.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1802 — DNS

**ID:** 1802  
**Nome:** DNS  
**Categoria:** Redes  
**Subcategoria:** DNS  
**Objetivo:** executar DNS com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver dns em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Network Engineer, com foco em DNS.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar DNS para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: camadas; DNS; rotas; ACL/firewall; TLS; MTU; latência; perda; captura de evidências; mudanças reversíveis.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1803 — DHCP

**ID:** 1803  
**Nome:** DHCP  
**Categoria:** Redes  
**Subcategoria:** DHCP  
**Objetivo:** executar DHCP com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver dhcp em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Network Engineer, com foco em DHCP.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar DHCP para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: camadas; DNS; rotas; ACL/firewall; TLS; MTU; latência; perda; captura de evidências; mudanças reversíveis.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1804 — VPN

**ID:** 1804  
**Nome:** VPN  
**Categoria:** Redes  
**Subcategoria:** VPN  
**Objetivo:** executar VPN com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver vpn em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Network Engineer, com foco em VPN.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar VPN para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: camadas; DNS; rotas; ACL/firewall; TLS; MTU; latência; perda; captura de evidências; mudanças reversíveis.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1805 — Firewall e Proxy

**ID:** 1805  
**Nome:** Firewall e Proxy  
**Categoria:** Redes  
**Subcategoria:** Firewall e Proxy  
**Objetivo:** executar Firewall e Proxy com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver firewall e proxy em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Network Engineer, com foco em Firewall e Proxy.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Firewall e Proxy para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: camadas; DNS; rotas; ACL/firewall; TLS; MTU; latência; perda; captura de evidências; mudanças reversíveis.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1806 — Routing e Switching

**ID:** 1806  
**Nome:** Routing e Switching  
**Categoria:** Redes  
**Subcategoria:** Routing e Switching  
**Objetivo:** executar Routing e Switching com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver routing e switching em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Network Engineer, com foco em Routing e Switching.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Routing e Switching para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: camadas; DNS; rotas; ACL/firewall; TLS; MTU; latência; perda; captura de evidências; mudanças reversíveis.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1807 — Latência e Conectividade

**ID:** 1807  
**Nome:** Latência e Conectividade  
**Categoria:** Redes  
**Subcategoria:** Latência e Conectividade  
**Objetivo:** executar Latência e Conectividade com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver latência e conectividade em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Network Engineer, com foco em Latência e Conectividade.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Latência e Conectividade para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: camadas; DNS; rotas; ACL/firewall; TLS; MTU; latência; perda; captura de evidências; mudanças reversíveis.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1808 — Segurança de Rede

**ID:** 1808  
**Nome:** Segurança de Rede  
**Categoria:** Redes  
**Subcategoria:** Segurança de Rede  
**Objetivo:** executar Segurança de Rede com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver segurança de rede em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Network Engineer, com foco em Segurança de Rede.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Segurança de Rede para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: camadas; DNS; rotas; ACL/firewall; TLS; MTU; latência; perda; captura de evidências; mudanças reversíveis.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1901 — Auditoria Linux

**ID:** 1901  
**Nome:** Auditoria Linux  
**Categoria:** Administração de Sistemas  
**Subcategoria:** Auditoria Linux  
**Objetivo:** executar Auditoria Linux com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria linux em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como System Administrator, com foco em Auditoria Linux.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria Linux para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: processos; serviços; permissões; storage; rede; logs; patches; backup; hardening; capacidade; automação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1902 — Windows Server

**ID:** 1902  
**Nome:** Windows Server  
**Categoria:** Administração de Sistemas  
**Subcategoria:** Windows Server  
**Objetivo:** executar Windows Server com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver windows server em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como System Administrator, com foco em Windows Server.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Windows Server para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: processos; serviços; permissões; storage; rede; logs; patches; backup; hardening; capacidade; automação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1903 — Usuários e Permissões

**ID:** 1903  
**Nome:** Usuários e Permissões  
**Categoria:** Administração de Sistemas  
**Subcategoria:** Usuários e Permissões  
**Objetivo:** executar Usuários e Permissões com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver usuários e permissões em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como System Administrator, com foco em Usuários e Permissões.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Usuários e Permissões para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: processos; serviços; permissões; storage; rede; logs; patches; backup; hardening; capacidade; automação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1904 — Serviços e Processos

**ID:** 1904  
**Nome:** Serviços e Processos  
**Categoria:** Administração de Sistemas  
**Subcategoria:** Serviços e Processos  
**Objetivo:** executar Serviços e Processos com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver serviços e processos em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como System Administrator, com foco em Serviços e Processos.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Serviços e Processos para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: processos; serviços; permissões; storage; rede; logs; patches; backup; hardening; capacidade; automação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1905 — Análise de Logs de Sistema

**ID:** 1905  
**Nome:** Análise de Logs de Sistema  
**Categoria:** Administração de Sistemas  
**Subcategoria:** Análise de Logs de Sistema  
**Objetivo:** executar Análise de Logs de Sistema com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver análise de logs de sistema em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como System Administrator, com foco em Análise de Logs de Sistema.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Análise de Logs de Sistema para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: processos; serviços; permissões; storage; rede; logs; patches; backup; hardening; capacidade; automação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1906 — Storage e Filesystems

**ID:** 1906  
**Nome:** Storage e Filesystems  
**Categoria:** Administração de Sistemas  
**Subcategoria:** Storage e Filesystems  
**Objetivo:** executar Storage e Filesystems com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver storage e filesystems em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como System Administrator, com foco em Storage e Filesystems.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Storage e Filesystems para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: processos; serviços; permissões; storage; rede; logs; patches; backup; hardening; capacidade; automação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1907 — Backup de Sistemas

**ID:** 1907  
**Nome:** Backup de Sistemas  
**Categoria:** Administração de Sistemas  
**Subcategoria:** Backup de Sistemas  
**Objetivo:** executar Backup de Sistemas com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver backup de sistemas em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como System Administrator, com foco em Backup de Sistemas.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Backup de Sistemas para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: processos; serviços; permissões; storage; rede; logs; patches; backup; hardening; capacidade; automação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 1908 — Automação de SysAdmin

**ID:** 1908  
**Nome:** Automação de SysAdmin  
**Categoria:** Administração de Sistemas  
**Subcategoria:** Automação de SysAdmin  
**Objetivo:** executar Automação de SysAdmin com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver automação de sysadmin em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como System Administrator, com foco em Automação de SysAdmin.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Automação de SysAdmin para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: processos; serviços; permissões; storage; rede; logs; patches; backup; hardening; capacidade; automação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2001 — Auditoria de Repositório GitHub

**ID:** 2001  
**Nome:** Auditoria de Repositório GitHub  
**Categoria:** Git e GitHub  
**Subcategoria:** Auditoria de Repositório GitHub  
**Objetivo:** executar Auditoria de Repositório GitHub com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de repositório github em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Git / GitHub Maintainer, com foco em Auditoria de Repositório GitHub.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Repositório GitHub para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: histórico; branches; PRs; proteção; Actions; secrets; dependências; releases; rastreabilidade; segurança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2002 — Estratégia de Branches

**ID:** 2002  
**Nome:** Estratégia de Branches  
**Categoria:** Git e GitHub  
**Subcategoria:** Estratégia de Branches  
**Objetivo:** executar Estratégia de Branches com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver estratégia de branches em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Git / GitHub Maintainer, com foco em Estratégia de Branches.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Estratégia de Branches para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: histórico; branches; PRs; proteção; Actions; secrets; dependências; releases; rastreabilidade; segurança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2003 — Commits Profissionais

**ID:** 2003  
**Nome:** Commits Profissionais  
**Categoria:** Git e GitHub  
**Subcategoria:** Commits Profissionais  
**Objetivo:** executar Commits Profissionais com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver commits profissionais em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Git / GitHub Maintainer, com foco em Commits Profissionais.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Commits Profissionais para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: histórico; branches; PRs; proteção; Actions; secrets; dependências; releases; rastreabilidade; segurança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2004 — Pull Request

**ID:** 2004  
**Nome:** Pull Request  
**Categoria:** Git e GitHub  
**Subcategoria:** Pull Request  
**Objetivo:** executar Pull Request com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver pull request em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Git / GitHub Maintainer, com foco em Pull Request.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Pull Request para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: histórico; branches; PRs; proteção; Actions; secrets; dependências; releases; rastreabilidade; segurança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2005 — Code Review de PR

**ID:** 2005  
**Nome:** Code Review de PR  
**Categoria:** Git e GitHub  
**Subcategoria:** Code Review de PR  
**Objetivo:** executar Code Review de PR com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver code review de pr em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Git / GitHub Maintainer, com foco em Code Review de PR.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Code Review de PR para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: histórico; branches; PRs; proteção; Actions; secrets; dependências; releases; rastreabilidade; segurança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2006 — Merge, Rebase e Conflitos

**ID:** 2006  
**Nome:** Merge, Rebase e Conflitos  
**Categoria:** Git e GitHub  
**Subcategoria:** Merge, Rebase e Conflitos  
**Objetivo:** executar Merge, Rebase e Conflitos com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver merge, rebase e conflitos em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Git / GitHub Maintainer, com foco em Merge, Rebase e Conflitos.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Merge, Rebase e Conflitos para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: histórico; branches; PRs; proteção; Actions; secrets; dependências; releases; rastreabilidade; segurança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2007 — Tags e Releases

**ID:** 2007  
**Nome:** Tags e Releases  
**Categoria:** Git e GitHub  
**Subcategoria:** Tags e Releases  
**Objetivo:** executar Tags e Releases com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver tags e releases em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Git / GitHub Maintainer, com foco em Tags e Releases.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Tags e Releases para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: histórico; branches; PRs; proteção; Actions; secrets; dependências; releases; rastreabilidade; segurança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2008 — Issues e GitHub Projects

**ID:** 2008  
**Nome:** Issues e GitHub Projects  
**Categoria:** Git e GitHub  
**Subcategoria:** Issues e GitHub Projects  
**Objetivo:** executar Issues e GitHub Projects com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver issues e github projects em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Git / GitHub Maintainer, com foco em Issues e GitHub Projects.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Issues e GitHub Projects para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: histórico; branches; PRs; proteção; Actions; secrets; dependências; releases; rastreabilidade; segurança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2009 — GitHub Actions

**ID:** 2009  
**Nome:** GitHub Actions  
**Categoria:** Git e GitHub  
**Subcategoria:** GitHub Actions  
**Objetivo:** executar GitHub Actions com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver github actions em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Git / GitHub Maintainer, com foco em GitHub Actions.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar GitHub Actions para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: histórico; branches; PRs; proteção; Actions; secrets; dependências; releases; rastreabilidade; segurança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2010 — Segurança de Repositório

**ID:** 2010  
**Nome:** Segurança de Repositório  
**Categoria:** Git e GitHub  
**Subcategoria:** Segurança de Repositório  
**Objetivo:** executar Segurança de Repositório com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver segurança de repositório em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Git / GitHub Maintainer, com foco em Segurança de Repositório.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Segurança de Repositório para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: histórico; branches; PRs; proteção; Actions; secrets; dependências; releases; rastreabilidade; segurança.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2101 — SLI, SLO e SLA

**ID:** 2101  
**Nome:** SLI, SLO e SLA  
**Categoria:** SRE e Observabilidade  
**Subcategoria:** SLI, SLO e SLA  
**Objetivo:** executar SLI, SLO e SLA com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver sli, slo e sla em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Site Reliability Engineer, com foco em SLI, SLO e SLA.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar SLI, SLO e SLA para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: SLI/SLO; sintomas; impacto; métricas; logs; traces; alertas; error budget; capacidade; resposta; aprendizado.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2109 — Reliability Review.

---

### PROMPT 2102 — Arquitetura de Observabilidade

**ID:** 2102  
**Nome:** Arquitetura de Observabilidade  
**Categoria:** SRE e Observabilidade  
**Subcategoria:** Arquitetura de Observabilidade  
**Objetivo:** executar Arquitetura de Observabilidade com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver arquitetura de observabilidade em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Site Reliability Engineer, com foco em Arquitetura de Observabilidade.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Arquitetura de Observabilidade para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: SLI/SLO; sintomas; impacto; métricas; logs; traces; alertas; error budget; capacidade; resposta; aprendizado.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2109 — Reliability Review.

---

### PROMPT 2103 — Estratégia de Logs

**ID:** 2103  
**Nome:** Estratégia de Logs  
**Categoria:** SRE e Observabilidade  
**Subcategoria:** Estratégia de Logs  
**Objetivo:** executar Estratégia de Logs com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver estratégia de logs em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Site Reliability Engineer, com foco em Estratégia de Logs.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Estratégia de Logs para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: SLI/SLO; sintomas; impacto; métricas; logs; traces; alertas; error budget; capacidade; resposta; aprendizado.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2109 — Reliability Review.

---

### PROMPT 2104 — Métricas e Traces

**ID:** 2104  
**Nome:** Métricas e Traces  
**Categoria:** SRE e Observabilidade  
**Subcategoria:** Métricas e Traces  
**Objetivo:** executar Métricas e Traces com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver métricas e traces em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Site Reliability Engineer, com foco em Métricas e Traces.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Métricas e Traces para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: SLI/SLO; sintomas; impacto; métricas; logs; traces; alertas; error budget; capacidade; resposta; aprendizado.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2109 — Reliability Review.

---

### PROMPT 2105 — Alertas Acionáveis

**ID:** 2105  
**Nome:** Alertas Acionáveis  
**Categoria:** SRE e Observabilidade  
**Subcategoria:** Alertas Acionáveis  
**Objetivo:** executar Alertas Acionáveis com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver alertas acionáveis em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Site Reliability Engineer, com foco em Alertas Acionáveis.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Alertas Acionáveis para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: SLI/SLO; sintomas; impacto; métricas; logs; traces; alertas; error budget; capacidade; resposta; aprendizado.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2109 — Reliability Review.

---

### PROMPT 2106 — Resposta a Incidentes SRE

**ID:** 2106  
**Nome:** Resposta a Incidentes SRE  
**Categoria:** SRE e Observabilidade  
**Subcategoria:** Resposta a Incidentes SRE  
**Objetivo:** executar Resposta a Incidentes SRE com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver resposta a incidentes sre em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Site Reliability Engineer, com foco em Resposta a Incidentes SRE.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Resposta a Incidentes SRE para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: SLI/SLO; sintomas; impacto; métricas; logs; traces; alertas; error budget; capacidade; resposta; aprendizado.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2109 — Reliability Review.

---

### PROMPT 2107 — Postmortem Sem Culpa

**ID:** 2107  
**Nome:** Postmortem Sem Culpa  
**Categoria:** SRE e Observabilidade  
**Subcategoria:** Postmortem Sem Culpa  
**Objetivo:** executar Postmortem Sem Culpa com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver postmortem sem culpa em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Site Reliability Engineer, com foco em Postmortem Sem Culpa.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Postmortem Sem Culpa para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: SLI/SLO; sintomas; impacto; métricas; logs; traces; alertas; error budget; capacidade; resposta; aprendizado.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2109 — Reliability Review.

---

### PROMPT 2108 — Capacity Planning

**ID:** 2108  
**Nome:** Capacity Planning  
**Categoria:** SRE e Observabilidade  
**Subcategoria:** Capacity Planning  
**Objetivo:** executar Capacity Planning com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver capacity planning em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Site Reliability Engineer, com foco em Capacity Planning.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Capacity Planning para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: SLI/SLO; sintomas; impacto; métricas; logs; traces; alertas; error budget; capacidade; resposta; aprendizado.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2109 — Reliability Review.

---

### PROMPT 2109 — Reliability Review

**ID:** 2109  
**Nome:** Reliability Review  
**Categoria:** SRE e Observabilidade  
**Subcategoria:** Reliability Review  
**Objetivo:** executar Reliability Review com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver reliability review em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Site Reliability Engineer, com foco em Reliability Review.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Reliability Review para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: SLI/SLO; sintomas; impacto; métricas; logs; traces; alertas; error budget; capacidade; resposta; aprendizado.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2109 — Reliability Review.

---

### PROMPT 2110 — Game Day / Chaos / Recovery Drill

**ID:** 2110  
**Nome:** Game Day / Chaos / Recovery Drill  
**Categoria:** SRE e Observabilidade  
**Subcategoria:** Game Day / Chaos / Recovery Drill  
**Objetivo:** executar Game Day / Chaos / Recovery Drill com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver game day / chaos / recovery drill em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Site Reliability Engineer, com foco em Game Day / Chaos / Recovery Drill.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Game Day / Chaos / Recovery Drill para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: SLI/SLO; sintomas; impacto; métricas; logs; traces; alertas; error budget; capacidade; resposta; aprendizado.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2109 — Reliability Review.

---

### PROMPT 2201 — Triagem de Chamado

**ID:** 2201  
**Nome:** Triagem de Chamado  
**Categoria:** Suporte Técnico e Help Desk  
**Subcategoria:** Triagem de Chamado  
**Objetivo:** executar Triagem de Chamado com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver triagem de chamado em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Intermediário  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Support Engineer / Help Desk Lead, com foco em Triagem de Chamado.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Triagem de Chamado para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: impacto; escopo; reprodução; evidência; diagnóstico; workaround; escalonamento; resolução; KB.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2202 — Reprodução de Erro

**ID:** 2202  
**Nome:** Reprodução de Erro  
**Categoria:** Suporte Técnico e Help Desk  
**Subcategoria:** Reprodução de Erro  
**Objetivo:** executar Reprodução de Erro com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver reprodução de erro em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Support Engineer / Help Desk Lead, com foco em Reprodução de Erro.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Reprodução de Erro para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: impacto; escopo; reprodução; evidência; diagnóstico; workaround; escalonamento; resolução; KB.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2203 — Análise de Logs para Suporte

**ID:** 2203  
**Nome:** Análise de Logs para Suporte  
**Categoria:** Suporte Técnico e Help Desk  
**Subcategoria:** Análise de Logs para Suporte  
**Objetivo:** executar Análise de Logs para Suporte com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver análise de logs para suporte em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Support Engineer / Help Desk Lead, com foco em Análise de Logs para Suporte.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Análise de Logs para Suporte para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: impacto; escopo; reprodução; evidência; diagnóstico; workaround; escalonamento; resolução; KB.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2204 — Base de Conhecimento

**ID:** 2204  
**Nome:** Base de Conhecimento  
**Categoria:** Suporte Técnico e Help Desk  
**Subcategoria:** Base de Conhecimento  
**Objetivo:** executar Base de Conhecimento com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver base de conhecimento em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Support Engineer / Help Desk Lead, com foco em Base de Conhecimento.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Base de Conhecimento para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: impacto; escopo; reprodução; evidência; diagnóstico; workaround; escalonamento; resolução; KB.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2205 — Escalonamento Técnico

**ID:** 2205  
**Nome:** Escalonamento Técnico  
**Categoria:** Suporte Técnico e Help Desk  
**Subcategoria:** Escalonamento Técnico  
**Objetivo:** executar Escalonamento Técnico com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver escalonamento técnico em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Support Engineer / Help Desk Lead, com foco em Escalonamento Técnico.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Escalonamento Técnico para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: impacto; escopo; reprodução; evidência; diagnóstico; workaround; escalonamento; resolução; KB.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2206 — Resolução e Encerramento

**ID:** 2206  
**Nome:** Resolução e Encerramento  
**Categoria:** Suporte Técnico e Help Desk  
**Subcategoria:** Resolução e Encerramento  
**Objetivo:** executar Resolução e Encerramento com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver resolução e encerramento em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Support Engineer / Help Desk Lead, com foco em Resolução e Encerramento.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Resolução e Encerramento para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: impacto; escopo; reprodução; evidência; diagnóstico; workaround; escalonamento; resolução; KB.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2301 — Plano de Projeto de TI

**ID:** 2301  
**Nome:** Plano de Projeto de TI  
**Categoria:** Gestão de Projetos de TI  
**Subcategoria:** Plano de Projeto de TI  
**Objetivo:** executar Plano de Projeto de TI com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver plano de projeto de ti em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Project Manager / Product Manager, com foco em Plano de Projeto de TI.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Plano de Projeto de TI para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; valor; escopo; backlog; dependências; riscos; capacidade; critérios de aceite; roadmap; comunicação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2302 — Escopo e Controle de Mudanças

**ID:** 2302  
**Nome:** Escopo e Controle de Mudanças  
**Categoria:** Gestão de Projetos de TI  
**Subcategoria:** Escopo e Controle de Mudanças  
**Objetivo:** executar Escopo e Controle de Mudanças com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver escopo e controle de mudanças em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Project Manager / Product Manager, com foco em Escopo e Controle de Mudanças.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Escopo e Controle de Mudanças para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; valor; escopo; backlog; dependências; riscos; capacidade; critérios de aceite; roadmap; comunicação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2303 — Backlog Priorizado

**ID:** 2303  
**Nome:** Backlog Priorizado  
**Categoria:** Gestão de Projetos de TI  
**Subcategoria:** Backlog Priorizado  
**Objetivo:** executar Backlog Priorizado com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver backlog priorizado em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Intermediário  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Project Manager / Product Manager, com foco em Backlog Priorizado.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Backlog Priorizado para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; valor; escopo; backlog; dependências; riscos; capacidade; critérios de aceite; roadmap; comunicação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2304 — Planejamento de Sprint Scrum

**ID:** 2304  
**Nome:** Planejamento de Sprint Scrum  
**Categoria:** Gestão de Projetos de TI  
**Subcategoria:** Planejamento de Sprint Scrum  
**Objetivo:** executar Planejamento de Sprint Scrum com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver planejamento de sprint scrum em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Project Manager / Product Manager, com foco em Planejamento de Sprint Scrum.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Planejamento de Sprint Scrum para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; valor; escopo; backlog; dependências; riscos; capacidade; critérios de aceite; roadmap; comunicação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2305 — Fluxo Kanban

**ID:** 2305  
**Nome:** Fluxo Kanban  
**Categoria:** Gestão de Projetos de TI  
**Subcategoria:** Fluxo Kanban  
**Objetivo:** executar Fluxo Kanban com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver fluxo kanban em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Project Manager / Product Manager, com foco em Fluxo Kanban.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Fluxo Kanban para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; valor; escopo; backlog; dependências; riscos; capacidade; critérios de aceite; roadmap; comunicação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2306 — Roadmap

**ID:** 2306  
**Nome:** Roadmap  
**Categoria:** Gestão de Projetos de TI  
**Subcategoria:** Roadmap  
**Objetivo:** executar Roadmap com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver roadmap em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Project Manager / Product Manager, com foco em Roadmap.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Roadmap para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; valor; escopo; backlog; dependências; riscos; capacidade; critérios de aceite; roadmap; comunicação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2307 — Épicos, Histórias e Tarefas

**ID:** 2307  
**Nome:** Épicos, Histórias e Tarefas  
**Categoria:** Gestão de Projetos de TI  
**Subcategoria:** Épicos, Histórias e Tarefas  
**Objetivo:** executar Épicos, Histórias e Tarefas com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver épicos, histórias e tarefas em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Project Manager / Product Manager, com foco em Épicos, Histórias e Tarefas.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Épicos, Histórias e Tarefas para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; valor; escopo; backlog; dependências; riscos; capacidade; critérios de aceite; roadmap; comunicação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2308 — Riscos e Dependências

**ID:** 2308  
**Nome:** Riscos e Dependências  
**Categoria:** Gestão de Projetos de TI  
**Subcategoria:** Riscos e Dependências  
**Objetivo:** executar Riscos e Dependências com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver riscos e dependências em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Project Manager / Product Manager, com foco em Riscos e Dependências.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Riscos e Dependências para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; valor; escopo; backlog; dependências; riscos; capacidade; critérios de aceite; roadmap; comunicação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2309 — Estimativas e Priorização

**ID:** 2309  
**Nome:** Estimativas e Priorização  
**Categoria:** Gestão de Projetos de TI  
**Subcategoria:** Estimativas e Priorização  
**Objetivo:** executar Estimativas e Priorização com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver estimativas e priorização em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Project Manager / Product Manager, com foco em Estimativas e Priorização.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Estimativas e Priorização para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; valor; escopo; backlog; dependências; riscos; capacidade; critérios de aceite; roadmap; comunicação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2310 — Jira + Confluence

**ID:** 2310  
**Nome:** Jira + Confluence  
**Categoria:** Gestão de Projetos de TI  
**Subcategoria:** Jira + Confluence  
**Objetivo:** executar Jira + Confluence com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver jira + confluence em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Project Manager / Product Manager, com foco em Jira + Confluence.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Jira + Confluence para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: objetivo; valor; escopo; backlog; dependências; riscos; capacidade; critérios de aceite; roadmap; comunicação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2401 — README Profissional

**ID:** 2401  
**Nome:** README Profissional  
**Categoria:** Documentação Técnica  
**Subcategoria:** README Profissional  
**Objetivo:** executar README Profissional com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver readme profissional em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Intermediário  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Writer / Staff Engineer, com foco em README Profissional.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar README Profissional para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: audiência; fonte de verdade; pré-requisitos; passos verificáveis; exemplos; troubleshooting; ownership; atualização.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2402 — ADR

**ID:** 2402  
**Nome:** ADR  
**Categoria:** Documentação Técnica  
**Subcategoria:** ADR  
**Objetivo:** executar ADR com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver adr em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Writer / Staff Engineer, com foco em ADR.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar ADR para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: audiência; fonte de verdade; pré-requisitos; passos verificáveis; exemplos; troubleshooting; ownership; atualização.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2403 — Documentação de API

**ID:** 2403  
**Nome:** Documentação de API  
**Categoria:** Documentação Técnica  
**Subcategoria:** Documentação de API  
**Objetivo:** executar Documentação de API com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver documentação de api em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Writer / Staff Engineer, com foco em Documentação de API.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Documentação de API para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: audiência; fonte de verdade; pré-requisitos; passos verificáveis; exemplos; troubleshooting; ownership; atualização.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2404 — Documentação de Banco

**ID:** 2404  
**Nome:** Documentação de Banco  
**Categoria:** Documentação Técnica  
**Subcategoria:** Documentação de Banco  
**Objetivo:** executar Documentação de Banco com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver documentação de banco em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Writer / Staff Engineer, com foco em Documentação de Banco.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Documentação de Banco para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: audiência; fonte de verdade; pré-requisitos; passos verificáveis; exemplos; troubleshooting; ownership; atualização.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2405 — Documentação de Infraestrutura

**ID:** 2405  
**Nome:** Documentação de Infraestrutura  
**Categoria:** Documentação Técnica  
**Subcategoria:** Documentação de Infraestrutura  
**Objetivo:** executar Documentação de Infraestrutura com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver documentação de infraestrutura em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Writer / Staff Engineer, com foco em Documentação de Infraestrutura.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Documentação de Infraestrutura para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: audiência; fonte de verdade; pré-requisitos; passos verificáveis; exemplos; troubleshooting; ownership; atualização.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2406 — Runbook

**ID:** 2406  
**Nome:** Runbook  
**Categoria:** Documentação Técnica  
**Subcategoria:** Runbook  
**Objetivo:** executar Runbook com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver runbook em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Writer / Staff Engineer, com foco em Runbook.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Runbook para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: audiência; fonte de verdade; pré-requisitos; passos verificáveis; exemplos; troubleshooting; ownership; atualização.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2407 — Playbook / SOP

**ID:** 2407  
**Nome:** Playbook / SOP  
**Categoria:** Documentação Técnica  
**Subcategoria:** Playbook / SOP  
**Objetivo:** executar Playbook / SOP com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver playbook / sop em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Writer / Staff Engineer, com foco em Playbook / SOP.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Playbook / SOP para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: audiência; fonte de verdade; pré-requisitos; passos verificáveis; exemplos; troubleshooting; ownership; atualização.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2408 — Changelog e Release Notes

**ID:** 2408  
**Nome:** Changelog e Release Notes  
**Categoria:** Documentação Técnica  
**Subcategoria:** Changelog e Release Notes  
**Objetivo:** executar Changelog e Release Notes com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver changelog e release notes em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Writer / Staff Engineer, com foco em Changelog e Release Notes.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Changelog e Release Notes para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: audiência; fonte de verdade; pré-requisitos; passos verificáveis; exemplos; troubleshooting; ownership; atualização.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2409 — Diagramas de Arquitetura

**ID:** 2409  
**Nome:** Diagramas de Arquitetura  
**Categoria:** Documentação Técnica  
**Subcategoria:** Diagramas de Arquitetura  
**Objetivo:** executar Diagramas de Arquitetura com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver diagramas de arquitetura em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Writer / Staff Engineer, com foco em Diagramas de Arquitetura.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Diagramas de Arquitetura para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: audiência; fonte de verdade; pré-requisitos; passos verificáveis; exemplos; troubleshooting; ownership; atualização.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2410 — Manual Técnico

**ID:** 2410  
**Nome:** Manual Técnico  
**Categoria:** Documentação Técnica  
**Subcategoria:** Manual Técnico  
**Objetivo:** executar Manual Técnico com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver manual técnico em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Writer / Staff Engineer, com foco em Manual Técnico.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Manual Técnico para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: audiência; fonte de verdade; pré-requisitos; passos verificáveis; exemplos; troubleshooting; ownership; atualização.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2501 — Auditoria de Repositório

**ID:** 2501  
**Nome:** Auditoria de Repositório  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Repositório  
**Objetivo:** executar Auditoria de Repositório com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de repositório em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Repositório.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Repositório para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2502 — Auditoria de Código

**ID:** 2502  
**Nome:** Auditoria de Código  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Código  
**Objetivo:** executar Auditoria de Código com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de código em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Código.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Código para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2503 — Auditoria de Arquitetura

**ID:** 2503  
**Nome:** Auditoria de Arquitetura  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Arquitetura  
**Objetivo:** executar Auditoria de Arquitetura com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de arquitetura em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Arquitetura.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Arquitetura para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2504 — Auditoria de Frontend

**ID:** 2504  
**Nome:** Auditoria de Frontend  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Frontend  
**Objetivo:** executar Auditoria de Frontend com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de frontend em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Frontend.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Frontend para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2505 — Auditoria de Backend

**ID:** 2505  
**Nome:** Auditoria de Backend  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Backend  
**Objetivo:** executar Auditoria de Backend com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de backend em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Backend.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Backend para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2506 — Auditoria de Banco de Dados

**ID:** 2506  
**Nome:** Auditoria de Banco de Dados  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Banco de Dados  
**Objetivo:** executar Auditoria de Banco de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de banco de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Banco de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Banco de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2507 — Auditoria de Infraestrutura

**ID:** 2507  
**Nome:** Auditoria de Infraestrutura  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Infraestrutura  
**Objetivo:** executar Auditoria de Infraestrutura com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de infraestrutura em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Infraestrutura.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Infraestrutura para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2508 — Auditoria de CI/CD

**ID:** 2508  
**Nome:** Auditoria de CI/CD  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de CI/CD  
**Objetivo:** executar Auditoria de CI/CD com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de ci/cd em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de CI/CD.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de CI/CD para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2509 — Auditoria de Segurança

**ID:** 2509  
**Nome:** Auditoria de Segurança  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Segurança  
**Objetivo:** executar Auditoria de Segurança com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de segurança em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Segurança.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Segurança para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2510 — Auditoria de Testes

**ID:** 2510  
**Nome:** Auditoria de Testes  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Testes  
**Objetivo:** executar Auditoria de Testes com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de testes em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Testes.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Testes para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2511 — Auditoria de Documentação

**ID:** 2511  
**Nome:** Auditoria de Documentação  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Documentação  
**Objetivo:** executar Auditoria de Documentação com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de documentação em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Documentação.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Documentação para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2512 — Auditoria de Produção, Custos e Performance

**ID:** 2512  
**Nome:** Auditoria de Produção, Custos e Performance  
**Categoria:** Auditoria Técnica  
**Subcategoria:** Auditoria de Produção, Custos e Performance  
**Objetivo:** executar Auditoria de Produção, Custos e Performance com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria de produção, custos e performance em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technical Auditor / Principal Engineer, com foco em Auditoria de Produção, Custos e Performance.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria de Produção, Custos e Performance para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: escopo; evidências; conformidade; gaps; severidade; impacto; prioridade; recomendação; validação; rastreabilidade.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0002 — Auditoria Completa de Projeto.

---

### PROMPT 2601 — Diagnóstico de Bug

**ID:** 2601  
**Nome:** Diagnóstico de Bug  
**Categoria:** Diagnóstico e Troubleshooting  
**Subcategoria:** Diagnóstico de Bug  
**Objetivo:** executar Diagnóstico de Bug com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver diagnóstico de bug em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Troubleshooting Lead / Senior Incident Engineer, com foco em Diagnóstico de Bug.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Diagnóstico de Bug para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: sintoma; timeline; evidências; hipóteses; testes discriminantes; causa raiz; correção; validação; prevenção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2610 — Root Cause Analysis (RCA).

---

### PROMPT 2602 — Falha de Deploy

**ID:** 2602  
**Nome:** Falha de Deploy  
**Categoria:** Diagnóstico e Troubleshooting  
**Subcategoria:** Falha de Deploy  
**Objetivo:** executar Falha de Deploy com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver falha de deploy em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Troubleshooting Lead / Senior Incident Engineer, com foco em Falha de Deploy.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Falha de Deploy para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: sintoma; timeline; evidências; hipóteses; testes discriminantes; causa raiz; correção; validação; prevenção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2610 — Root Cause Analysis (RCA).

---

### PROMPT 2603 — Problema de Banco de Dados

**ID:** 2603  
**Nome:** Problema de Banco de Dados  
**Categoria:** Diagnóstico e Troubleshooting  
**Subcategoria:** Problema de Banco de Dados  
**Objetivo:** executar Problema de Banco de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver problema de banco de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Troubleshooting Lead / Senior Incident Engineer, com foco em Problema de Banco de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Problema de Banco de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: sintoma; timeline; evidências; hipóteses; testes discriminantes; causa raiz; correção; validação; prevenção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2610 — Root Cause Analysis (RCA).

---

### PROMPT 2604 — Problema de API

**ID:** 2604  
**Nome:** Problema de API  
**Categoria:** Diagnóstico e Troubleshooting  
**Subcategoria:** Problema de API  
**Objetivo:** executar Problema de API com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver problema de api em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Troubleshooting Lead / Senior Incident Engineer, com foco em Problema de API.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Problema de API para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: sintoma; timeline; evidências; hipóteses; testes discriminantes; causa raiz; correção; validação; prevenção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2610 — Root Cause Analysis (RCA).

---

### PROMPT 2605 — Problema de Autenticação

**ID:** 2605  
**Nome:** Problema de Autenticação  
**Categoria:** Diagnóstico e Troubleshooting  
**Subcategoria:** Problema de Autenticação  
**Objetivo:** executar Problema de Autenticação com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver problema de autenticação em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Troubleshooting Lead / Senior Incident Engineer, com foco em Problema de Autenticação.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Problema de Autenticação para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: sintoma; timeline; evidências; hipóteses; testes discriminantes; causa raiz; correção; validação; prevenção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2610 — Root Cause Analysis (RCA).

---

### PROMPT 2606 — Problema de Rede

**ID:** 2606  
**Nome:** Problema de Rede  
**Categoria:** Diagnóstico e Troubleshooting  
**Subcategoria:** Problema de Rede  
**Objetivo:** executar Problema de Rede com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver problema de rede em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Troubleshooting Lead / Senior Incident Engineer, com foco em Problema de Rede.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Problema de Rede para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: sintoma; timeline; evidências; hipóteses; testes discriminantes; causa raiz; correção; validação; prevenção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2610 — Root Cause Analysis (RCA).

---

### PROMPT 2607 — Problema de Infraestrutura

**ID:** 2607  
**Nome:** Problema de Infraestrutura  
**Categoria:** Diagnóstico e Troubleshooting  
**Subcategoria:** Problema de Infraestrutura  
**Objetivo:** executar Problema de Infraestrutura com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver problema de infraestrutura em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Troubleshooting Lead / Senior Incident Engineer, com foco em Problema de Infraestrutura.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Problema de Infraestrutura para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: sintoma; timeline; evidências; hipóteses; testes discriminantes; causa raiz; correção; validação; prevenção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2610 — Root Cause Analysis (RCA).

---

### PROMPT 2608 — Problema de Performance

**ID:** 2608  
**Nome:** Problema de Performance  
**Categoria:** Diagnóstico e Troubleshooting  
**Subcategoria:** Problema de Performance  
**Objetivo:** executar Problema de Performance com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver problema de performance em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Troubleshooting Lead / Senior Incident Engineer, com foco em Problema de Performance.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Problema de Performance para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: sintoma; timeline; evidências; hipóteses; testes discriminantes; causa raiz; correção; validação; prevenção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2610 — Root Cause Analysis (RCA).

---

### PROMPT 2609 — Problema em Produção

**ID:** 2609  
**Nome:** Problema em Produção  
**Categoria:** Diagnóstico e Troubleshooting  
**Subcategoria:** Problema em Produção  
**Objetivo:** executar Problema em Produção com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver problema em produção em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Troubleshooting Lead / Senior Incident Engineer, com foco em Problema em Produção.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Problema em Produção para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: sintoma; timeline; evidências; hipóteses; testes discriminantes; causa raiz; correção; validação; prevenção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2610 — Root Cause Analysis (RCA).

---

### PROMPT 2610 — Root Cause Analysis (RCA)

**ID:** 2610  
**Nome:** Root Cause Analysis (RCA)  
**Categoria:** Diagnóstico e Troubleshooting  
**Subcategoria:** Root Cause Analysis (RCA)  
**Objetivo:** executar Root Cause Analysis (RCA) com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver root cause analysis (rca) em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Avançado  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Troubleshooting Lead / Senior Incident Engineer, com foco em Root Cause Analysis (RCA).

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Root Cause Analysis (RCA) para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: sintoma; timeline; evidências; hipóteses; testes discriminantes; causa raiz; correção; validação; prevenção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 2610 — Root Cause Analysis (RCA).

---

### PROMPT 2701 — Baseline de Performance

**ID:** 2701  
**Nome:** Baseline de Performance  
**Categoria:** Performance, Escalabilidade e Resiliência  
**Subcategoria:** Baseline de Performance  
**Objetivo:** executar Baseline de Performance com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver baseline de performance em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Performance / Reliability Engineer, com foco em Baseline de Performance.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Baseline de Performance para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: baseline; carga; p95/p99; throughput; saturação; gargalos; capacidade; degradação; testes; custo.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2702 — Plano de Escalabilidade

**ID:** 2702  
**Nome:** Plano de Escalabilidade  
**Categoria:** Performance, Escalabilidade e Resiliência  
**Subcategoria:** Plano de Escalabilidade  
**Objetivo:** executar Plano de Escalabilidade com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver plano de escalabilidade em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Performance / Reliability Engineer, com foco em Plano de Escalabilidade.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Plano de Escalabilidade para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: baseline; carga; p95/p99; throughput; saturação; gargalos; capacidade; degradação; testes; custo.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2703 — Resiliência e Fault Tolerance

**ID:** 2703  
**Nome:** Resiliência e Fault Tolerance  
**Categoria:** Performance, Escalabilidade e Resiliência  
**Subcategoria:** Resiliência e Fault Tolerance  
**Objetivo:** executar Resiliência e Fault Tolerance com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver resiliência e fault tolerance em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Performance / Reliability Engineer, com foco em Resiliência e Fault Tolerance.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Resiliência e Fault Tolerance para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: baseline; carga; p95/p99; throughput; saturação; gargalos; capacidade; degradação; testes; custo.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2704 — Capacity Planning Técnico

**ID:** 2704  
**Nome:** Capacity Planning Técnico  
**Categoria:** Performance, Escalabilidade e Resiliência  
**Subcategoria:** Capacity Planning Técnico  
**Objetivo:** executar Capacity Planning Técnico com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver capacity planning técnico em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Performance / Reliability Engineer, com foco em Capacity Planning Técnico.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Capacity Planning Técnico para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: baseline; carga; p95/p99; throughput; saturação; gargalos; capacidade; degradação; testes; custo.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2705 — Otimização de Custos e Recursos

**ID:** 2705  
**Nome:** Otimização de Custos e Recursos  
**Categoria:** Performance, Escalabilidade e Resiliência  
**Subcategoria:** Otimização de Custos e Recursos  
**Objetivo:** executar Otimização de Custos e Recursos com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver otimização de custos e recursos em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Performance / Reliability Engineer, com foco em Otimização de Custos e Recursos.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Otimização de Custos e Recursos para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: baseline; carga; p95/p99; throughput; saturação; gargalos; capacidade; degradação; testes; custo.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2706 — Análise de Gargalos

**ID:** 2706  
**Nome:** Análise de Gargalos  
**Categoria:** Performance, Escalabilidade e Resiliência  
**Subcategoria:** Análise de Gargalos  
**Objetivo:** executar Análise de Gargalos com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver análise de gargalos em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Performance / Reliability Engineer, com foco em Análise de Gargalos.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Análise de Gargalos para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: baseline; carga; p95/p99; throughput; saturação; gargalos; capacidade; degradação; testes; custo.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2801 — Modernização de Legado

**ID:** 2801  
**Nome:** Modernização de Legado  
**Categoria:** Modernização e Migração  
**Subcategoria:** Modernização de Legado  
**Objetivo:** executar Modernização de Legado com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver modernização de legado em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Modernization Architect, com foco em Modernização de Legado.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Modernização de Legado para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: inventário; compatibilidade; dependências; dados; risco; estratégia incremental; coexistência; cutover; rollback; validação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2802 — Estratégia de Migração

**ID:** 2802  
**Nome:** Estratégia de Migração  
**Categoria:** Modernização e Migração  
**Subcategoria:** Estratégia de Migração  
**Objetivo:** executar Estratégia de Migração com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver estratégia de migração em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Modernization Architect, com foco em Estratégia de Migração.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Estratégia de Migração para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: inventário; compatibilidade; dependências; dados; risco; estratégia incremental; coexistência; cutover; rollback; validação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2803 — Upgrade de Dependências

**ID:** 2803  
**Nome:** Upgrade de Dependências  
**Categoria:** Modernização e Migração  
**Subcategoria:** Upgrade de Dependências  
**Objetivo:** executar Upgrade de Dependências com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver upgrade de dependências em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Modernization Architect, com foco em Upgrade de Dependências.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Upgrade de Dependências para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: inventário; compatibilidade; dependências; dados; risco; estratégia incremental; coexistência; cutover; rollback; validação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2804 — Upgrade de Framework

**ID:** 2804  
**Nome:** Upgrade de Framework  
**Categoria:** Modernização e Migração  
**Subcategoria:** Upgrade de Framework  
**Objetivo:** executar Upgrade de Framework com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver upgrade de framework em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Modernization Architect, com foco em Upgrade de Framework.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Upgrade de Framework para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: inventário; compatibilidade; dependências; dados; risco; estratégia incremental; coexistência; cutover; rollback; validação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2805 — Migração de Banco de Dados

**ID:** 2805  
**Nome:** Migração de Banco de Dados  
**Categoria:** Modernização e Migração  
**Subcategoria:** Migração de Banco de Dados  
**Objetivo:** executar Migração de Banco de Dados com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver migração de banco de dados em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Modernization Architect, com foco em Migração de Banco de Dados.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Migração de Banco de Dados para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: inventário; compatibilidade; dependências; dados; risco; estratégia incremental; coexistência; cutover; rollback; validação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2806 — Migração para Cloud

**ID:** 2806  
**Nome:** Migração para Cloud  
**Categoria:** Modernização e Migração  
**Subcategoria:** Migração para Cloud  
**Objetivo:** executar Migração para Cloud com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver migração para cloud em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Modernization Architect, com foco em Migração para Cloud.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Migração para Cloud para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: inventário; compatibilidade; dependências; dados; risco; estratégia incremental; coexistência; cutover; rollback; validação.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2901 — Developer Experience Audit

**ID:** 2901  
**Nome:** Developer Experience Audit  
**Categoria:** Platform Engineering e Developer Experience  
**Subcategoria:** Developer Experience Audit  
**Objetivo:** executar Developer Experience Audit com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver developer experience audit em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform Engineer / Developer Experience Lead, com foco em Developer Experience Audit.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Developer Experience Audit para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: jornada do dev; tempo de setup; golden paths; self-service; guardrails; observabilidade; feedback; adoção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2902 — Platform Engineering

**ID:** 2902  
**Nome:** Platform Engineering  
**Categoria:** Platform Engineering e Developer Experience  
**Subcategoria:** Platform Engineering  
**Objetivo:** executar Platform Engineering com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver platform engineering em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform Engineer / Developer Experience Lead, com foco em Platform Engineering.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Platform Engineering para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: jornada do dev; tempo de setup; golden paths; self-service; guardrails; observabilidade; feedback; adoção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2903 — Golden Path

**ID:** 2903  
**Nome:** Golden Path  
**Categoria:** Platform Engineering e Developer Experience  
**Subcategoria:** Golden Path  
**Objetivo:** executar Golden Path com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver golden path em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform Engineer / Developer Experience Lead, com foco em Golden Path.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Golden Path para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: jornada do dev; tempo de setup; golden paths; self-service; guardrails; observabilidade; feedback; adoção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 2904 — Self-Service para Desenvolvedores

**ID:** 2904  
**Nome:** Self-Service para Desenvolvedores  
**Categoria:** Platform Engineering e Developer Experience  
**Subcategoria:** Self-Service para Desenvolvedores  
**Objetivo:** executar Self-Service para Desenvolvedores com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver self-service para desenvolvedores em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Platform Engineer / Developer Experience Lead, com foco em Self-Service para Desenvolvedores.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Self-Service para Desenvolvedores para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: jornada do dev; tempo de setup; golden paths; self-service; guardrails; observabilidade; feedback; adoção.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 3001 — Auditoria FinOps

**ID:** 3001  
**Nome:** Auditoria FinOps  
**Categoria:** FinOps e Custos  
**Subcategoria:** Auditoria FinOps  
**Objetivo:** executar Auditoria FinOps com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver auditoria finops em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como FinOps / Cloud Cost Engineer, com foco em Auditoria FinOps.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Auditoria FinOps para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: alocação; utilização; desperdício; compromissos; unit economics; orçamento; forecast; anomalias; trade-offs.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 3002 — Otimização de Custos Cloud

**ID:** 3002  
**Nome:** Otimização de Custos Cloud  
**Categoria:** FinOps e Custos  
**Subcategoria:** Otimização de Custos Cloud  
**Objetivo:** executar Otimização de Custos Cloud com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver otimização de custos cloud em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como FinOps / Cloud Cost Engineer, com foco em Otimização de Custos Cloud.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Otimização de Custos Cloud para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: alocação; utilização; desperdício; compromissos; unit economics; orçamento; forecast; anomalias; trade-offs.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 3003 — Unit Economics de Infraestrutura

**ID:** 3003  
**Nome:** Unit Economics de Infraestrutura  
**Categoria:** FinOps e Custos  
**Subcategoria:** Unit Economics de Infraestrutura  
**Objetivo:** executar Unit Economics de Infraestrutura com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver unit economics de infraestrutura em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como FinOps / Cloud Cost Engineer, com foco em Unit Economics de Infraestrutura.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Unit Economics de Infraestrutura para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: alocação; utilização; desperdício; compromissos; unit economics; orçamento; forecast; anomalias; trade-offs.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 3004 — Budget, Forecast e Anomalias

**ID:** 3004  
**Nome:** Budget, Forecast e Anomalias  
**Categoria:** FinOps e Custos  
**Subcategoria:** Budget, Forecast e Anomalias  
**Objetivo:** executar Budget, Forecast e Anomalias com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver budget, forecast e anomalias em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como FinOps / Cloud Cost Engineer, com foco em Budget, Forecast e Anomalias.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Budget, Forecast e Anomalias para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: alocação; utilização; desperdício; compromissos; unit economics; orçamento; forecast; anomalias; trade-offs.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 3101 — Governança Técnica

**ID:** 3101  
**Nome:** Governança Técnica  
**Categoria:** Governança, Risco e Privacidade  
**Subcategoria:** Governança Técnica  
**Objetivo:** executar Governança Técnica com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver governança técnica em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technology Governance / GRC Specialist, com foco em Governança Técnica.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Governança Técnica para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: políticas; controles; ownership; evidências; riscos; dados; retenção; acesso; auditoria; exceções; revisão periódica.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 3102 — Mapeamento de Compliance

**ID:** 3102  
**Nome:** Mapeamento de Compliance  
**Categoria:** Governança, Risco e Privacidade  
**Subcategoria:** Mapeamento de Compliance  
**Objetivo:** executar Mapeamento de Compliance com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver mapeamento de compliance em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technology Governance / GRC Specialist, com foco em Mapeamento de Compliance.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Mapeamento de Compliance para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: políticas; controles; ownership; evidências; riscos; dados; retenção; acesso; auditoria; exceções; revisão periódica.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 3103 — Privacidade e Data Protection

**ID:** 3103  
**Nome:** Privacidade e Data Protection  
**Categoria:** Governança, Risco e Privacidade  
**Subcategoria:** Privacidade e Data Protection  
**Objetivo:** executar Privacidade e Data Protection com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver privacidade e data protection em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technology Governance / GRC Specialist, com foco em Privacidade e Data Protection.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Privacidade e Data Protection para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: políticas; controles; ownership; evidências; riscos; dados; retenção; acesso; auditoria; exceções; revisão periódica.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

### PROMPT 3104 — Registro de Riscos Técnicos

**ID:** 3104  
**Nome:** Registro de Riscos Técnicos  
**Categoria:** Governança, Risco e Privacidade  
**Subcategoria:** Registro de Riscos Técnicos  
**Objetivo:** executar Registro de Riscos Técnicos com método profissional, evidências e critérios verificáveis.  
**Quando utilizar:** quando o trabalho envolver registro de riscos técnicos em projeto, sistema, repositório, ambiente ou incidente real.  
**Nível:** Especialista  
**Entradas necessárias:** [PROJETO], [OBJETIVO] e, conforme aplicável, [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [ERRO], [REPOSITÓRIO], [URL], [BANCO_DE_DADOS], [VERSÃO], restrições e evidências disponíveis.  

**Prompt completo:**

```text
PAPEL
Atue como Technology Governance / GRC Specialist, com foco em Registro de Riscos Técnicos.

CONTEXTO
Trabalhe sobre [PROJETO], [TECNOLOGIA], [AMBIENTE], [ARQUIVO], [REPOSITÓRIO], [URL] e/ou [ERRO] fornecidos. Considere versões reais e documentação oficial quando a versão puder alterar a resposta.

OBJETIVO
Executar Registro de Riscos Técnicos para alcançar [OBJETIVO] com resultado tecnicamente verificável, seguro e reutilizável.

PROCESSO
1. Identifique o estado atual e as evidências disponíveis.
2. Explicite hipóteses, lacunas e restrições relevantes; não invente fatos ausentes.
3. Analise, quando aplicável: políticas; controles; ownership; evidências; riscos; dados; retenção; acesso; auditoria; exceções; revisão periódica.
4. Proponha a alternativa principal e explique trade-offs importantes.
5. Converta a análise em ações priorizadas P0/P1/P2.
6. Inclua comandos, código, configuração, testes ou exemplos somente quando ajudam a executar ou validar a solução.
7. Para ações destrutivas, irreversíveis ou de produção, inclua pré-condições, backup/rollback e verificação posterior.
8. Não trate "arquivo existe", "pipeline iniciou" ou "deploy retornou 200" como prova suficiente de correção funcional sem validação compatível.

FORMATO DA RESPOSTA
- Resumo executivo
- Estado/evidências
- Análise técnica
- Achados ou proposta
- Plano priorizado
- Implementação/exemplos (se aplicável)
- Testes e validação
- Riscos e rollback
- Pendências e próxima ação

VALIDAÇÃO
Considere a tarefa concluída somente quando os critérios de sucesso estiverem demonstrados por evidência, teste, comparação ou checagem objetiva. Diferencie claramente: confirmado, inferido, recomendado e não verificado.
```

**Variáveis:** `[PROJETO]` `[TECNOLOGIA]` `[PROBLEMA]` `[OBJETIVO]` `[AMBIENTE]` `[ARQUIVO]` `[ERRO]` `[REPOSITÓRIO]` `[URL]` `[BANCO_DE_DADOS]` `[VERSÃO]`

**Saída esperada:** análise/proposta executável, decisões e trade-offs, ações priorizadas, evidências, testes/validação, riscos e próxima ação.

**Critérios de validação:** escopo atendido; fatos não inventados; riscos relevantes tratados; critérios de sucesso demonstrados; mudanças críticas com rollback; resultado reproduzível ou auditável.

**Prompt complementar:** 0010 — Validação Final e Gate de Qualidade.

---

## 9. WORKFLOWS PROFISSIONAIS PRONTOS

- **Projeto do zero:** 0001 Criar Projeto de Software do Zero → 0101 Levantamento de Requisitos → 0201 Seleção de Estilo Arquitetural → 0701 Modelagem Relacional → 0301 Node.js + NestJS → 0401 React → 1601 Estratégia de Testes → 1101 Estratégia CI/CD → 0020 Release Readiness / Go-No-Go → 0013 Documentação Técnica Completa
- **Auditoria e recuperação de projeto:** 0002 Auditoria Completa de Projeto → 2501 Auditoria de Repositório → 2502 Auditoria de Código → 2509 Auditoria de Segurança → 2308 Riscos e Dependências → 0003 Continuidade de Projeto → 0010 Validação Final e Gate de Qualidade
- **Bug crítico em produção:** 0004 Diagnóstico de Problemas → 2609 Problema em Produção → 2106 Resposta a Incidentes SRE → 2610 Root Cause Analysis (RCA) → 1603 Testes de Integração → 2107 Postmortem Sem Culpa
- **Refatoração segura:** 0005 Refatoração Incremental Segura → 0106 Análise de Dívida Técnica → 0108 Code Review Profissional → 1602 Testes Unitários → 1603 Testes de Integração → 0010 Validação Final e Gate de Qualidade
- **API pronta para produção:** 0601 Design de API REST → 0602 OpenAPI / Swagger → 0608 Versionamento, Segurança e Testes de API → 1505 Segurança de APIs → 1606 Testes de API / Postman → 2102 Arquitetura de Observabilidade → 0020 Release Readiness / Go-No-Go
- **Kubernetes produção:** 1204 Deployment Kubernetes → 1205 Segurança Kubernetes → 1207 Observabilidade Kubernetes → 1208 Escalabilidade e Resiliência Kubernetes → 2101 SLI, SLO e SLA → 2110 Game Day / Chaos / Recovery Drill
- **LLM/RAG produção:** 1703 RAG → 1709 Segurança contra Prompt Injection → 1710 Evals e Regressão de LLM → 2102 Arquitetura de Observabilidade → 3002 Otimização de Custos Cloud
- **Migração para cloud:** 2802 Estratégia de Migração → 1401 Comparação AWS vs Azure vs GCP → 0017 Arquitetura Cloud Well-Architected → 2806 Migração para Cloud → 1105 Deploy e Rollback → 2110 Game Day / Chaos / Recovery Drill

## 10. CONTROLE DE DUPLICIDADES E EVOLUÇÃO

Antes de registrar novo prompt: comparar finalidade, entradas, processo, saída e validação. Classificar a proposta como **NOVO, COMPLEMENTAR, VARIANTE, DUPLICADO, SUBSTITUÍDO ou CONSOLIDADO**. DUPLICADO é fundido; SUBSTITUÍDO preserva o ID antigo como tombstone; VARIANTE só recebe ID próprio quando altera materialmente contexto, risco ou resultado.

### Política de versões
- `v1.x`: melhoria editorial, exemplos, critérios de validação e atualização de boas práticas sem mudar a finalidade do ID.
- `v2.x` do conteúdo do prompt: mudanças internas maiores, mas finalidade e contrato permanecem compatíveis.
- Mudança incompatível de finalidade: **novo ID**, independentemente do número da versão.

## 11. FONTES PRINCIPAIS DA PESQUISA

As fontes abaixo orientaram os princípios e critérios técnicos. Recomendações específicas da biblioteca são síntese própria, salvo quando explicitamente atribuídas.

| Fonte | Tipo | Referência |
|---|---|---|
| OpenAI Academy — Prompting | Oficial | https://academy.openai.com/en/public/clubs/work-users-ynjqu/resources/prompting |
| OpenAI Help — Prompt engineering best practices for ChatGPT | Oficial | https://help.openai.com/en/articles/10032626-how-do-i-prompt-chatgpt-effectively |
| OpenAI API — Model guidance (GPT-5.6) | Oficial | https://developers.openai.com/api/docs/guides/latest-model |
| Microsoft Learn — Prompt engineering techniques | Oficial | https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering |
| Microsoft Learn — System message design | Oficial | https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/advanced-prompt-engineering |
| Google AI — Prompt design strategies | Oficial | https://ai.google.dev/gemini-api/docs/prompting-strategies |
| GitHub Docs — Prompt engineering for Copilot Chat | Oficial | https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering |
| GitHub Docs — Prompt files/custom instructions | Oficial | https://docs.github.com/en/copilot/reference/customization-cheat-sheet |
| AWS Well-Architected Framework | Oficial | https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html |
| Azure Well-Architected Framework | Oficial | https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework |
| Google Cloud Well-Architected Framework | Oficial | https://docs.cloud.google.com/architecture/framework |
| NIST SSDF | Oficial | https://csrc.nist.gov/projects/ssdf |
| OWASP ASVS | Oficial/projeto OWASP | https://owasp.org/www-project-application-security-verification-standard/ |
| OWASP GenAI — Prompt Injection | Oficial/projeto OWASP | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ |
| Docker — Building best practices | Oficial | https://docs.docker.com/build/building/best-practices/ |
| Docker — Build secrets | Oficial | https://docs.docker.com/build/building/secrets/ |
| Kubernetes — Production environment | Oficial | https://kubernetes.io/docs/setup/production-environment/ |
| Kubernetes — Application Security Checklist | Oficial | https://kubernetes.io/docs/concepts/security/application-security-checklist/ |
| PostgreSQL 18 — Current Documentation | Oficial | https://www.postgresql.org/docs/current/ |
| Playwright — Best Practices | Oficial | https://playwright.dev/docs/best-practices |
| Atlassian — Agile project management | Oficial | https://www.atlassian.com/agile/project-management |
| Atlassian Rovo — Prompt Rovo Chat | Oficial | https://support.atlassian.com/rovo/docs/using-rovo-chat/ |
| The Prompt Report — systematic survey | Acadêmica | https://arxiv.org/abs/2406.06608 |
| DAIR.AI Prompt Engineering Guide | Comunidade técnica | https://github.com/dair-ai/Prompt-Engineering-Guide |
| prompts.chat / Awesome ChatGPT Prompts | Comunidade / biblioteca pública | https://github.com/f/awesome-chatgpt-prompts |

## 12. NOTAS DE ATUALIDADE (23/08/2026)

- A documentação da OpenAI já apresenta orientação específica para a família GPT-5.6 e recomenda prompts mais enxutos, sem repetição desnecessária, com validação em evals representativos.
- O GitHub documenta prompt files reutilizáveis (`.github/prompts/*.prompt.md`), custom instructions e `AGENTS.md`, reforçando a viabilidade de versionar esta biblioteca como código.
- A documentação corrente do PostgreSQL está na série 18; otimização e operação devem considerar a versão real usada no ambiente.
- O NIST SSDF 1.1 continua referência final publicada; a revisão 1.2 apareceu como draft, portanto não deve ser tratada automaticamente como baseline final sem verificar seu status atual.
- Para LLMs, prompt injection não é resolvida apenas com RAG ou fine-tuning; exige controles em camadas, validação, autorização e desenho seguro de ferramentas.

## 13. RESERVA PARA EXPANSÃO

As faixas até 9999 permanecem disponíveis. A inclusão futura de novas tecnologias, especializações ou variantes não exige renumerar nenhum prompt existente. A biblioteca deve crescer por lacunas reais de cobertura, não por meta artificial de quantidade.