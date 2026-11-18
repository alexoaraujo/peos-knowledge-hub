# PEOS — Qualidade do roteamento heurístico (PMU)

## Problema verificado na análise do código

A versão inicial do roteador `tools/peos_engine.py` usava `norm(keyword) in norm(query)`. Isso localizava **substrings dentro de palavras sem relação semântica**, por exemplo a palavra `api` dentro de `capivara` ou `apicultura`, selecionando indevidamente PMU-005 (Full Stack).

## Correção candidata

- Usar limites de palavra Unicode para palavras-chave, preservando busca de expressões com espaços (inclusive espaços repetidos).
- Manter a priorização existente por pontuação `3` para expressões e `1` para termos simples, com desempate por ID.
- Manter o fallback `PMU-001` quando não houver correspondência.
- Reconhecer explicitamente `Auth0` no vocabulário de segurança para não depender de correspondência por prefixo `auth`.
- Preservar `PLAN_ONLY`, `NO_EXTERNAL_MUTATIONS` e a política de gates não avaliados; não modificar textos originais, hashes ou PMUs.

## Casos cobertos por testes

| Consulta | Comportamento esperado |
| --- | --- |
| `capivara` ou `apicultura` | Sem match de `api`; fallback PMU-001 |
| `Criar API REST` | PMU-005 |
| `API-rest` | PMU-005 |
| `Configurar Auth0 com RBAC` | PMU-007 |
| `Integração full   stack` | PMU-005 |
| `auditoria integral do projeto` | PMU-003 |
| `wireframe UX e design` | PMU-006 |

## Limitações

Esta é uma correção de **falsos positivos lexicais**. Não é validação semântica da escolha de PMU; não assegura precisão de roteamento em linguagem livre nem substitui avaliação humana. A abrangência lexical depende de termos/expressões cadastrados. A homologação editorial dos dez PMUs continua pendente na [issue #17](https://github.com/alexoaraujo/peos-knowledge-hub/issues/17); direitos de publicação continuam bloqueados pela [issue #2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2).

Um rollback seguro é reverter o commit desta mudança por uma nova PR, sem alterar manifestos ou dados do catálogo.
