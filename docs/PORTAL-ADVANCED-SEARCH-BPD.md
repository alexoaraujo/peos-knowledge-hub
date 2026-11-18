# Pesquisa avançada do PEOS Knowledge Hub — execução BPD

## Dependência
Dependência atendida: a PR #7 foi integrada à `main` pelo commit `3755bdc2b1a9221cccef1ed7be0bb410e64e0394`. Esta PR #9 foi sincronizada com a `main`, preservando o diff restrito à pesquisa avançada. A integração exige novos checks no HEAD atual.

## Prompts aplicados
- **BPD-046, 047, 048, 049, 050**: evolução incremental do frontend estático, filtro e estado
- **BPD-084, 085, 086**: redução de lógica duplicada de busca e separação de funções puras
- **BPD-088, 089, 092**: testes comportamentais e de regressão
- **BPD-093, 094**: mensuração básica de consistência de consulta, com otimizações de normalização pré-computada
- **BPD-110, 111, 113, 118**: auditoria de código versus documentação e gate de conclusão

## Entregáveis verificáveis
1. `hub-portal/search.js`: motor puro de busca, com normalização Unicode, índice pré-calculado, facets e ordenação estável. Sem dependências, requisições externas ou mutações
2. `hub-portal/app.js`: interface que combina busca textual com namespace, categoria, grupo e tags, preservando paginação incremental, foco e estado vazio
3. `hub-portal/index.html`: selects rotulados para novas facets, scripts locais em ordem
4. `tests/portal_search.test.cjs`: testes com o catálogo real de 797 entradas (659 canônicas, 128 BPD, 10 PMUs)
5. `.github/workflows/portal-search-gate.yml`: `node --check`, `node --test`, regressão Python e integridade do catálogo
6. Compatibilidade ajustada em `tests/test_portal_accessibility.py`

## Política de segurança e proveniência
- A busca opera apenas sobre os campos existentes: ID, título/finalidade, categoria, grupo, tags e namespace
- Filtros combinados por interseção, sem modificar `catalog.json`
- Nenhum campo ausente é inventado para o catálogo
- Renderização de dados em DOM apenas via `textContent` e validação de caminhos herdada da PR #7
- Nenhuma credencial ou API externa, nenhuma execução de agente; motores PEOS continuam `PLAN_ONLY`

## Gates de conclusão
- [ ] Testes Node e Python PASS no SHA da PR
- [ ] Índice determinístico preservado
- [ ] Verificação manual de filtros, resultados e navegação com teclado
- [ ] Revisão do código e do comportamento pelo mantenedor (revisão externa opcional no modo solo)
- [ ] Revisão de licenciamento antes de release (issue #2)

**Status:** implementação de pesquisa avançada proposta, não homologada para produção.
