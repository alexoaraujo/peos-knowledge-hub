# UX, Design System e Acessibilidade — ciclo PEOS BPD-051..067

## Escopo e proveniência

Aplicado sobre o portal estático existente em `hub-portal/index.html` da `main`. Referência editorial: `colecoes/programacao-design/INDEX.md`. Os prompts BPD são referências locais, **não** substituem os 659 prompts canônicos.

## Prompts executados como metodologia

| BPD | Necessidade | Mudança verificável |
| --- | --- | --- |
| BPD-051 — UX completo | Busca intuitiva e orientação | Labels visíveis, estado vazio e mensagem de erro |
| BPD-055 — Hierarquia visual | Organização dos filtros/resultados | Títulos de seção, controles agrupados e resultados separados |
| BPD-056/058 — Design system/tokens | Consistência com tema original | Folha `enhancements.css` incremental, sem reescrever o tema existente |
| BPD-059 — Estados de componentes | Estados disabled, loading, erro e vazio | Botão de limpar inativo quando filtros vazios; aviso e retry |
| BPD-061/062 — Responsividade/mobile-first | Utilização em telas pequenas | Grid de filtros em coluna e cartões de largura fluida até 640px |
| BPD-065/066 — Auditoria e correção de acessibilidade | Teclado, foco, nomes acessíveis | Skip link, labels explícitos, status `aria-live`, foco visível e redução de movimento |
| BPD-075/088/092 — Review e regressão | Evitar quebra de comportamento existente | Contratos estáticos e testes completos do Hub |
| BPD-111/113/118 — Evidência e conclusão | Não simular funcionalidades | CI valida sintaxe JS e contratos; auditoria manual de leitor de tela ainda pendente |

## Implementação

- Portal permanece read-only; a composição de prompts segue `PLAN_ONLY`.
- Novos controles: ordenação de resultados, limpar filtros, paginação incremental de 40 itens e retry de carregamento.
- Links construídos por segmentos relativos permitidos e codificados; dados do catálogo são exibidos apenas por `textContent`, sem interpolação de HTML.
- Nenhuma dependência nova de pacote, conta externa ou serviço pago.
- Manifests, catálogo gerado e prompts BPD/canônicos não foram alterados.

## Gates

- [ ] Python: `python3 -m unittest discover -s tests -v`
- [ ] JavaScript: `node --check hub-portal/app.js`
- [ ] `python3 tools/build_hub_index.py --check`
- [ ] GitHub Actions no SHA da PR e revisão independente
- [ ] Auditoria manual de uso por teclado, leitor de tela e contraste
- [ ] Revisão de licença das fontes anterior a release público (issue #2)

**Estado:** implementação candidata, não afirma conformidade WCAG nem prontidão para Production até auditoria humana e evidências.
