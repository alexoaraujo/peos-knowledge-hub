# PEOS — Auditoria automática WCAG (axe-core)

## Objetivo e metodologia
BPD-065/066 (auditar e corrigir acessibilidade), BPD-088/091/092 (testes E2E), BPD-113/118 (aceite baseado em evidência). A análise automatizada é executada em Chromium real com axe-core, com regras etiquetadas WCAG 2.0 A/AA, 2.1 A/AA e 2.2 AA.

## Estados avaliados
- Portal carregado com 797 registros e paginação inicial de 40
- Resultados de busca por texto, com filtro ativo
- Estado sem resultados em viewport mobile 375px

## Execução
A mesma CI da PR #10 instala `@playwright/test@1.56.1` e `@axe-core/playwright@4.14.0`, ambos gratuitos, e realiza `npx playwright test --config=playwright.config.cjs` em `ubuntu-24.04`.

## Gates
- [ ] Zero violações detectadas nas regras automatizadas selecionadas
- [ ] Sem desabilitar regras ou colocar exceções sem justificativa e revisão
- [ ] Teste manual por leitor de tela, contraste e navegação real — issue #8
- [ ] Revisão independente e licença das fontes — issue #2

**A ausência de violações detectadas automaticamente não equivale à certificação ou conformidade integral WCAG.** Sem mutações externas, sem alteração do catálogo e sem licença atribuída às fontes.
