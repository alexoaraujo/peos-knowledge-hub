# Importação integral v0.1 — plano PEOS

**Status:** aguardando upload do conteúdo integral do ZIP para esta branch. Este documento não é evidência de importação concluída.

## Baseline

- Biblioteca Mestre TI v2.1 como fonte canônica.
- 659 prompts canônicos, 128 BPD, 10 PMUs PROPOSED e 10 workflows versionados.
- Pacote integral local: `PEOS_Knowledge_Hub_v0.1.0.zip`.

## Execução

1. Extrair ZIP e copiar arquivos para clone da branch `feat/peos-knowledge-hub-v0.1`.
2. Executar `python3 -m unittest discover -s tests -v`.
3. Executar `python3 tools/library.py validate`.
4. Executar `python3 tools/peos_engine.py validate`.
5. Executar `python3 tools/build_hub_index.py --check`.
6. Conferir os 797 registros, IDs, hashes, workflows, ausência de segredos e diff.
7. Executar GitHub Actions no SHA da PR; revisar resultados e direitos de redistribuição.
8. Somente após gates PASS, aprovar merge e release.

## Critérios de bloqueio

CI ausente ou falhando, divergência de SHA, direitos de distribuição não comprovados, agentes com execução externa não autorizada ou testes comportamentais insuficientes.

Referências: issues #1, #2 e #3.
