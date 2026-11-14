# Catálogo e proveniência

Namespaces: `0001` etc (canônico), `BPD-001` etc (complementar), `PMU-001` etc (orquestrador), `WF-001` etc (workflow, não texto de prompt). IDs são permanentes, não recicláveis. Metadados preservados como fonte de verdade em `catalog/`, `colecoes/programacao-design/`, `pmu/` e `workflows/`.

Os arquivos `contracts/*.json` são contratos v2 gerados e os manifests contêm hashes SHA-256 dos conteúdos. `provenance/sources.json` registra os ZIPs de origem sem incorporá-los. O novo índice estático `hub-portal/catalog.json` é **derivado e reconstruível**; alterações manuais não são aceitas.

**Vínculos**: BPD têm `related_canonical_ids`, relação **não necessariamente equivalente**; PMUs `refs` vinculam prompts canônicos; workflows declaram `pmu_id`. Uma curadoria humana deve aprovar equivalências e PMUs. Não colapsar namespaces, nem alterar hashes em nome da compatibilidade.

**Consulta**: `python3 -m hub.cli search --query 'PostgreSQL' --namespace canonical --limit 10`. A busca usa tokens normalizados (não embeddings); nenhuma alegação de precisão semântica.
