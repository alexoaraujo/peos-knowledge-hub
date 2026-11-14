# Governança da v2.1

## Compatibilidade

Os 659 IDs, nomes, categorias e hashes da v2.0 permanecem inalterados. A v2.1 adiciona exclusivamente os namespaces PMU e WF. Os 128 itens BPD mantêm seus IDs locais.

## Status de conteúdo

- `SOURCE_EXTRACTED`: herdado da fonte, sem revisão humana presumida.
- `CURATED`: criado editorialmente, aprovação externa não registrada.
- `PROPOSED`: novo PMU/workflow não homologado.

## Gate de publicação

Executar auditoria histórica, validação do catálogo, verificação da coleção BPD, hashes PMU, referências, testes e compilação. Publicação em GitHub exige execução de CI no repositório real.

## Evolução futura

Nunca reciclar IDs. Versionar cada alteração; exigir motivação, evidência, testes de regressão e revisão independente para mudanças de semântica.
