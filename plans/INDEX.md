# Seleção e execução controlada dos prompts PEOS

A seleção principal feita pelo motor para **criar projeto** foi `PMU-002 / WF-002` com dependências canônicas `0001`, `0101`, `0201`, `0502`, `1601`, `0020`. Os demais planos foram escolhidos explicitamente para frentes especializadas.

| PMU | Especialidade | Uso no Knowledge Hub |
|---|---|---|
| `PMU-001` | Prompt Universal PEOS | Governança e orquestração inicial |
| `PMU-002` | Criação de Projeto 360° | Arquitetura, backlog e implementação inicial |
| `PMU-003` | Auditoria Integral 360° | Auditoria da origem e regressões |
| `PMU-004` | Continuidade Autônoma Controlada | Continuidade limitada por gates |
| `PMU-006` | UX/UI e Design System | Portal de busca e UX acessível |
| `PMU-007` | Segurança e Compliance | Segurança, proveniência e compliance |
| `PMU-009` | DevOps, SRE e Release | GitHub Actions, testes e release |

**Prompts canônicos de apoio:** `0001` Criação de Projeto; `0101` Requisitos; `0201` Arquitetura; `0502` (dependência definida no PMU-002); `1601` Estratégia de Testes; `0010` Gate de Qualidade; `0020` Release Go/No-Go.

**Importante:** composições são artefatos `PLAN_ONLY`, com gates `NOT_EVALUATED`. Elas não são execuções nem substituem evidências técnicas.

Planos JSON gerados:
- `PEOS-KNOWLEDGE-HUB-PMU-001.json` — Classificar escopo, projeto, fontes, riscos, restrições e dependências do PEOS Knowledge Hub
- `PEOS-KNOWLEDGE-HUB-PMU-002.json` — Criar Projeto PEOS Knowledge Hub open-source com biblioteca versionada, taxonomia, governança, validação, workflows, agentes especializados, CI GitHub e portal de busca
- `PEOS-KNOWLEDGE-HUB-PMU-003.json` — Auditar integralmente os ZIPs, manifestos, hashes, IDs e regressão da Biblioteca Mestre TI v2.1
- `PEOS-KNOWLEDGE-HUB-PMU-004.json` — Continuar PEOS Knowledge Hub sem ultrapassar gate de licença, revisão ou publicação
- `PEOS-KNOWLEDGE-HUB-PMU-006.json` — Projetar UX de catálogo, navegação e busca acessível da biblioteca PEOS Knowledge Hub
- `PEOS-KNOWLEDGE-HUB-PMU-007.json` — Validar segurança, proveniência, direitos de redistribuição, controle de execução e gates do PEOS Knowledge Hub
- `PEOS-KNOWLEDGE-HUB-PMU-009.json` — Planejar DevOps GitHub Actions, CI estática, quality gates e release verificável do PEOS Knowledge Hub
