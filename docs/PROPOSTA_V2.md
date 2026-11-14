# Proposta especializada — Biblioteca Mestre TI 2.0

Esta é uma **proposta de roadmap**. Não confundir com funcionalidades já implementadas no pacote v1.1.0 estruturado.

## Modelo de ficha de prompt v2

Cada ID deve ter contrato estruturado adicional ao Markdown completo:

| Dimensão | Campos propostos | Objetivo |
|---|---|---|
| Identidade | `id`, `slug`, `title`, `version`, `status` | Endereçamento estável |
| Taxonomia | `group`, `sector`, `category`, `subcategory`, `tags` | Busca sem ambiguidade |
| Escopo | `goal`, `when_to_use`, `when_not_to_use`, `preconditions` | Prevenir uso equivocado |
| Contexto | `inputs`, `environment`, `dependencies` | Tornar o prompt executável |
| Contrato | `output_schema`, `artifacts`, `acceptance_criteria` | Saídas reproduzíveis |
| Execução | `procedure`, `tool_permissions`, `human_approval` | Controle operacional |
| Segurança | `risk_level`, `secrets_policy`, `rollback`, `production_guard` | Reduzir risco |
| Evidência | `source_urls`, `source_version`, `verified_at`, `evidence` | Proveniência e atualidade |
| Qualidade | `tests`, `examples`, `edge_cases`, `evaluation_results` | Evals e regressão |
| Relacionamentos | `requires`, `related`, `replaces`, `workflows` | Composições e dependências |
| Governança | `owner`, `reviewer`, `reviewed_at`, `change_reason` | Responsabilidade editorial |

**Recomendação:** diferenciar `source_subcategory` (legado) de `subcategory` (classificação nova); nunca reescrever a ficha original apenas para alterar uma classificação.

## Camadas lógicas recomendadas

1. **Evidence & Provenance**: fontes e recortes verificáveis, datas e hashes.
2. **Context**: projeto, repositório, branch, stack, ambiente e restrições.
3. **Governance**: IDs, versões, ownership, status e approvals.
4. **Prompt Registry**: 647+ unidades com contratos padronizados.
5. **Workflows & Dependencies**: composição de prompts, fases e pré-condições.
6. **Execution Gates**: testes, avaliação, security, rollback e release.
7. **Discovery & Search**: filtros por hierarquia, profissão, tecnologia, trabalho e evidência.
8. **Evaluation & Feedback**: casos positivos, negativos, regressões, avaliação de utilidade e atualidade.

## Índices e navegação futuros

Além dos existentes (31 profissões, 20 fases, 14 workflows e 20 tags), recomendar:

- **Por resultado/entregável**: ADR, OpenAPI, migration SQL, runbook, documento de segurança, plano de release.
- **Por nível e criticidade**: iniciante, intermediário, avançado, especialista, impacto, risco e ambiente.
- **Por setor de negócio**: transportes/logística, saúde, financeiro, indústria, educação, setor público — **somente após classificação manual baseada em conteúdo**.
- **Por tecnologia/fornecedor**: GitHub, Vercel, Neon, Auth0, PostgreSQL, Kubernetes etc. (tags do legado são preliminares e extraídas do título).
- **Por governança**: promessas de segurança, fontes oficiais e necessidade de aprovação humana.
- **Por cenário e workflow**: projeto do zero, auditoria, incidentes, release, migração, integração e autenticação.

## Backlog sugerido

| Prioridade | Trabalho | Aceite objetivo |
|---|---|---|
| P0 | Versionar este pacote em GitHub com branch protegida | Workflow verde em PR e main; mínimo de revisores conforme disponibilidade do plano |
| P0 | Auditar editorialmente 90 subcategorias | 647 fichas revisadas; sem rótulos indevidos |
| P0 | Implementar schema validation completa (Draft 2020-12) | Manifesto inválido bloqueado por schema e testes |
| P0 | Implementar depreciação formal/tombstones | Testes de referências, replacements e histórico sem remoção |
| P1 | Metadados de entrada e saída tipados | 100% dos prompts com contrato de entrada/saída verificável |
| P1 | Evals por prompt e segurança de ferramentas | Relatórios de regressão versionados e risco documentado |
| P1 | Gerador de release notes e comparação por versão | PR gera diff categorizado (novos, revisados, depreciados) |
| P1 | Portal de busca estático open source | Filtros, pesquisa full-text e links por ID sem backend pago |
| P1 | Modelo de workflow tipado e gates | Pré-condições, passos, dependências e evidências verificáveis |
| P2 | Facetas de setor de negócio e compliance | Classificação supervisionada; zero atribuições presumidas |
| P2 | Detecção de duplicidade semântica assistida | Similaridade por intenção com decisão humana |
| P2 | Distribuição como catálogo/API versionada | Consumo via JSON e pacote estático, com testes de compatibilidade |

## Gate de transição para v2.0

A v2.0 só deve ser declarada como conteúdo oficialmente revisado quando taxonomia, contratos, owners, testes e evidências estiverem validados. A versão atual mantém o conteúdo integral da v1.1, sem alegar revisão semântica dos 647 prompts.
