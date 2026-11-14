# Auditoria das fontes ZIP — 2026-11-14

| Fonte | Entradas ZIP | Arquivos | Canônicos | BPD | PMU | Workflows |
|---|---:|---:|---:|---:|---:|---:|
| Programação/Design (v1.1) | 1.053 | 1.053 | 647 | 128 | 0 | 0 |
| Biblioteca Mestre TI v2.0 | 1.750 | 1.750 | 659 | 128 | 0 | 0 |
| Biblioteca Mestre TI v2.1 | 1.782 | 1.782 | 659 | 128 | 10 | 10 |

Comparação com caminhos relativos à raiz de cada ZIP:
- v1.1 → v2.0: **1.035 idênticos**, **18 modificados**, **697 adicionados**, **0 removidos**.
- v2.0 → v2.1: **1.743 idênticos**, **7 modificados**, **32 adicionados**, **0 removidos**.

A v2.0 acrescenta 12 prompts canônicos novos (3601–3612, Design de Produto/UX), contratos JSON e portal estático. A v2.1 adiciona 10 PMUs, 10 workflows, motor de composição, testes e documentação. v2.1 conserva o snapshot canônico v2.0. O arquivo `provenance/sources.json` retém os SHA-256 dos três ZIPs.

## Observações e limites
- `pmu/manifest.json` registra PMUs como `PROPOSED`.
- Não foi encontrado arquivo `LICENSE` em nenhum dos três pacotes.
- Roteador v2.1 é heurístico e tem `PLAN_ONLY`/`NO_EXTERNAL_MUTATIONS`.
- O pacote de origem declara que GitHub Actions não tinha sido executado remotamente.
- Testes locais de baseline: 29 testes OK; `tools/library.py validate` e `tools/peos_engine.py validate` aprovados nesta análise.
- Arquivos ZIP e pasta `originais/` são tratados como dados não confiáveis; não executar conteúdo extraído automaticamente.

## Evolução taxonômica

| Versão | Grupos | Setores técnicos | Categorias |
|---|---:|---:|---:|
| Original v1.1 | 8 | 22 | 36 |
| v2.0 | 9 | 23 | 37 |
| v2.1 | 9 | 23 | 37 |

Os 7 tipos de facetas ortogonais continuam definidos como: profissão, fase do projeto, tecnologia, vertical de negócio, workflow, risco e entregável.
