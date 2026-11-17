# PEOS — Browser E2E & Search Performance Gate (BPD-065/066, BPD-088..095)

## Contexto
Esta feature deriva da branch `feat/hub-advanced-faceted-search` (PR #9), que deriva de `feat/hub-portal-accessibility-ux` (PR #7). A revisão deve respeitar a ordem **#7 → #9 → PR E2E**, sem rebase de `main` sobre uma base ainda não aprovada.

## Aplicação dos prompts
- **BPD-088/089/090/091/092**: estratégia e testes automatizados E2E reais em Chromium, além dos testes unitários existentes
- **BPD-093/094**: medição repetível do motor de busca puro, com p95, média e quantidade de consultas
- **BPD-065/066**: testes automatizados de nomes de controles, skip link por teclado e responsividade, sem declarar certificação WCAG
- **BPD-110/111/113/118**: evidência no SHA, funcionalidade verificada, testes com falha real e gates explícitos

## O que os testes cobrem
1. Carregamento efetivo dos 797 prompts via servidor HTTP local e navegador Chromium
2. Paginação 40 → 80, mantendo resultado total acessível
3. Interseção dos filtros namespace, categoria, grupo, tag e ID em dados reais
4. Limpeza dos filtros, estados sem resultados e busca insensível a acentos
5. Navegação por teclado/skip link, rótulos visíveis e ausência de overflow a 375/320px
6. Falha de rede simulada **apenas no teste** e recuperação via botão Retry
7. Benchmark de 500 consultas repetíveis com publicação de média e p95; limite de 2000ms é somente proteção contra travamento, não SLA de produção

## Comandos
```bash
npm install --no-save --package-lock=false --ignore-scripts @playwright/test@1.56.1
npx playwright install chromium
npx playwright test --config=playwright.config.cjs
node --test tests/portal_search_benchmark.test.cjs
python3 -m unittest discover -s tests -v
python3 tools/build_hub_index.py --check
```

## Gates
- [ ] E2E Chromium PASS no SHA do GitHub Actions
- [ ] Benchmark com métricas registradas e resultados consistentes
- [ ] Regressão Python e validação do catálogo PASS
- [ ] Revisão pelo mantenedor; teste manual com leitor de tela/contraste antes da homologação de acessibilidade (issue #8)
- [ ] Direitos/licenciamento das fontes (issue #2) antes de release

**Não modifique a biblioteca canônica, os manifests de versões ou os hashes para fazer testes passarem.** Testes negativos com falhas de rede são isolados no browser e não alteram dados de origem.
