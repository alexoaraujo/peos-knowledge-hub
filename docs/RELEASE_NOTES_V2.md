# Release Notes — Biblioteca Mestre de Prompts TI v2.0.0

**Tipo:** evolução maior da taxonomia e da governança. **Data editorial da revisão:** 14/11/2026.

## Totais confirmados

- 273 IDs originais v1.0 preservados; 374 da v1.1 preservados; **647 IDs históricos intactos**.
- **12 IDs novos:** `3601`–`3612` na categoria **Design de Produto e UX/UI**.
- **659 IDs canônicos**, dos quais 647 são conteúdo histórico e 12 são novos contratos de UX/UI.
- **128 itens BPD** mantidos em namespace próprio, sem renumeração.
- **787 entradas consultáveis** (não significa 787 finalidades semânticas únicas).
- **9 grupos**, **23 setores técnicos**, **37 categorias**, **95 subcategorias classificadas**.

## Novos prompts de UX/UI

| ID | Nova finalidade canônica | Referências à coleção BPD |
|---|---|---|
| `3601` | Pesquisa UX e Descoberta de Necessidades | BPD-051 |
| `3602` | Arquitetura da Informação e Fluxos de Usuário | BPD-051 |
| `3603` | Wireframes Funcionais e Especificação de Telas | BPD-052 |
| `3604` | Composição Visual, Layout e Hierarquia UX | BPD-053, BPD-055 |
| `3605` | Redesign de Produto com Preservação Funcional | BPD-054 |
| `3606` | Prototipação Interativa e Contratos de Interação | BPD-052, BPD-051 |
| `3607` | Design Responsivo Mobile-First por Tarefa | BPD-061, BPD-062 |
| `3608` | Design de Tabelas e Dados Densos Responsivos | BPD-063 |
| `3609` | Padrões de Navegação Responsiva e Menus | BPD-064 |
| `3610` | Pesquisa de Usabilidade e Avaliação de Fluxos | BPD-051, BPD-054 |
| `3611` | Handoff UX/UI para Engenharia e Critérios de Aceite | BPD-056, BPD-059 |
| `3612` | UX Inclusiva e Acessibilidade de Jornadas | BPD-065, BPD-066, BPD-067 |

## Escopo da revisão

- A curadoria dos novos prompts foi feita editorialmente nesta entrega; **não existe aprovação independente humana registrada**.
- Os contratos dos 647 prompts legados são `SOURCE_EXTRACTED`, não revisão semântica individual.
- A coleção BPD é preservada tal como enviada; links entre registros indicam proximidade temática, não equivalência integral.
- 11 candidatos históricos BPD foram revisados; decisões explícitas constam em `catalog/ux_curadoria_v2.json` e `catalog/bpd_crosswalk_v2.csv`.
- Novos conteúdos de pesquisa UX, prototipação, avaliação de usabilidade e handoff são **especializações editoriais**, não reprodução literal da fonte.

## Gates

Executar `python3 tools/library.py audit`, `python3 tools/library.py validate`, `python3 tools/v2_contracts.py`, `python3 -m unittest discover -s tests -v`, `python3 tools/library.py index --check`, `python3 tools/library.py compile --check` e `python3 tools/collections_integration.py check`.

**Limitações:** a execução da CI no GitHub requer publicação do repositório, e a aprovação semântica externa de cada contrato permanece separada da validação automatizada.
