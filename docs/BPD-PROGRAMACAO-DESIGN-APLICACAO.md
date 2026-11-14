# Plano aplicado — Programação e Design (BPD) no PEOS Knowledge Hub

**Origem verificada:** `colecoes/programacao-design/INDEX.md` na `main`, porque a branch informada `feat/v21-real-llm-evidence-pilot` não foi encontrada. Coleção: 128 IDs locais em 30 seções; vínculos com IDs canônicos são **afinidade temática**, não equivalência. Conteúdo da coleção preservado.

## Matriz de aplicação de prompts (BPD-126 coordena, não executa ações externas)

| Frente | BPD fonte | Artefato/uso no Hub | Gate de conclusão |
| --- | --- | --- | --- |
| Arquitetura | 016, 026, 114, 117 | Rever módulos existentes de catálogo, CLI, portal e validação; preservar a stack Python stdlib | Decisão registrada e sem recriação desnecessária |
| Produto/UX | 051, 056, 065 | Evoluir busca, navegação, estados do portal e acessibilidade | Testes reais de teclado, foco, contraste e leitura; ainda PENDENTE |
| Segurança | 071, 073, 118 | Sem credenciais nos prompts; agentes PLAN_ONLY e gates fail-closed | Auditoria de segredos e privilégios documentada |
| Revisão de código | 075, 077, 110, 111 | Confrontar README, implementação e testes; distinguir prova de simulação | Matriz código versus documentação revisada |
| Qualidade | 088, 089, 092, 099 | Validador do índice BPD com testes de mutação e CI dedicada | Validação local + CI no SHA da PR |
| Execução | 113, 115, 116, 118 | Mudanças incrementais verificáveis, sem modificar canônicos | PASS somente com evidências, revisão e aceite |

## Implementado nesta PR

1. Validador read-only do índice BPD: 128 entradas ordenadas e únicas, 30 seções, links e arquivos presentes, aviso obrigatório de afinidade.
2. Quatro testes comportamentais (caso íntegro, ID duplicado, arquivo ausente e aviso de afinidade apagado).
3. GitHub Actions `bpd-collection-gate.yml`, executado em PRs relevantes e manualmente.
4. Nenhuma mutação em `catalog/manifest.json`, `colecoes/programacao-design/INDEX.md`, `prompts/BPD-*.md` ou conteúdo canônico.

## Auditoria de implementação vs documentação — BPD-110 e BPD-111

| Componente | Evidência | Estado |
| --- | --- | --- |
| Catálogo e CLI | `hub/catalog.py`, `hub/cli.py`, testes existentes | Implementação identificada; aceite condicionado aos testes |
| Índice estático | `tools/build_hub_index.py`, `hub-portal/catalog.json` | Reproduzível localmente |
| Portal | `hub-portal/` | Implementação estática; UX e acessibilidade ainda sem auditoria completa |
| Agentes | `agents/manifest.json` com PLAN_ONLY | Planejamento; **não** agentes externos autônomos |
| Evidências LLM reais | Não demonstradas por esta PR | **NÃO VERIFICADO** |
| Licença open-source de fontes | Sem licença nos três ZIPs | **BLOCKED** — issue #2 |

## Critérios para avanço (BPD-113/118)

- [ ] Check BPD CI PASS no SHA de revisão
- [ ] Testes completos do Hub PASS no SHA de revisão
- [ ] Revisão independente do código e da matriz de riscos
- [ ] Nenhum conteúdo canônico ou manifesto alterado silenciosamente
- [ ] UX/acessibilidade verificados antes de afirmar o portal pronto para produção
- [ ] Revisão de licença anterior ao release

**Não promova esta PR automaticamente.** A ausência da branch piloto solicitada não autoriza declarar os resultados experimentais dessa branch como revisados.
