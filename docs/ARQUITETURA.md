# Arquitetura técnica da biblioteca mestre

## Hierarquia editorial e facetas

```text
Biblioteca Mestre TI
  ├── Grupo estratégico (8)
  │     └── Setor técnico (22)
  │           └── Categoria legada (36)
  │                 └── Subcategoria editorial (90)
  │                       └── Prompt (647 IDs imutáveis)
  └── Facetas transversais
        ├── Profissão (31 perfis no índice original)
        ├── Fase do projeto (20 fases)
        ├── Workflow (14 composições)
        ├── Tags de tecnologia (20 tags por detecção em título)
        ├── Status de ciclo de vida
        └── Segmento/vertical de negócio (opcional; não inferido do legado)
```

**Decisão arquitetural ADR-001:** persistir cada prompt no caminho baseado exclusivamente no ID (ex.: `prompts/0700-0799/0711.md`) e armazenar classificação no manifesto. O arquivo não muda de localização quando uma classificação editorial evolui. Assim, referências de longa duração não quebram.

**Decisão ADR-002:** o conteúdo da ficha é a fonte textual canônica; o manifesto é a fonte de verdade dos metadados de integridade e da classificação. Índices e compilados são derivados e não devem ser editados manualmente.

**Decisão ADR-003:** somente usar biblioteca padrão Python no gate básico (sem dependência paga ou serviço externo). Versionamento semântico e revisão humana em PR; CI não executa alterações nem publica conteúdo automaticamente.

## Estrutura principal

```text
biblioteca-mestre-ti-automatizada/
├── README.md
├── catalog/
│   ├── manifest.json              # 647 registros, checksum por ficha
│   ├── manifest.schema.json       # contrato de metadados
│   ├── taxonomy.json              # grupos, setores, categorias, subcategorias
│   ├── relations.json             # perfis, fases e workflows
│   ├── history.json               # diff histórico 1.0 → 1.1
│   └── events.jsonl               # trilha de eventos append-only em Git
├── prompts/NN00-NN99/NNNN.md      # 647 fichas canônicas
├── releases/v1.0.0.json           # snapshot legado
├── releases/v1.1.0.json           # snapshot consolidado
├── indices/                       # filtros automáticos + CSV
├── dist/                          # biblioteca completa compilada
├── originais/                     # v1.0 e v1.1, imutáveis
├── tools/library.py               # import, audit, validate, index, compile, stage
├── tools/build_taxonomy.py        # bootstrap editorial da taxonomia
├── tests/test_library.py          # testes positivos e negativos
├── docs/                          # decisões e governança
└── .github/workflows/             # gate CI automático
```

## Mapa de grupos

| Grupo | Propósito |
|---|---|
| G01 | Estratégia, gestão e governança |
| G02 | Engenharia e arquitetura |
| G03 | Desenvolvimento e integrações |
| G04 | Dados, analytics e IA |
| G05 | Plataforma e operações |
| G06 | Segurança e identidade |
| G07 | Qualidade, auditoria e suporte |
| G08 | Documentação e coding agents |

## Eixos que não devem ser confundidos

**Setor técnico** é uma divisão dentro do catálogo de TI (ex.: Automação e entrega). **Setor de negócio** é uma vertical aplicável aos processos (ex.: logística, saúde, indústria, setor público), portanto uma faceta distinta e opcional. **Grupo** é um domínio editorial macro; **categoria** mantém a classificação da biblioteca v1.1; **subcategoria** é a nova classificação editorial a ser revisada.

## Política de verificação

O validador verifica a integridade de arquivos contra SHA-256, IDs únicos, metadados em fichas, vinculação taxonômica, integridade do ledger, snapshots versionados, integridade das fontes originais, referências existentes em papéis/fases/workflows e índices reproduzíveis. `audit` recalcula os deltas v1.0 → v1.1 para não depender de contagens manuais no changelog.
