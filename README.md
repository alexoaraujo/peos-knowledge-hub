# PEOS Knowledge Hub

**Prompt Engineering Operating System — Knowledge Hub**

Plataforma open-source planejada para engenharia de prompts para TI: biblioteca versionada, taxonomia, governança, busca, validação automatizada, workflows e agentes especializados. O núcleo funcional inicial utiliza apenas **Python 3 (biblioteca padrão)** e um portal estático, sem serviços pagos obrigatórios.

> **Maturidade: MVP técnico em avaliação, não release de produção.** O motor compõe **planos**: não executa ações externas nem concede gates automaticamente. Os 10 PMUs originais estão marcados `PROPOSED` e exigem homologação editorial. Os arquivos de origem não contêm licença explícita; é necessária revisão de titularidade/licenciamento antes de promover uma distribuição pública com licença open-source.

## Base auditada

| Namespace | Quantidade | Origem |
| --- | ---: | --- |
| Numérico canônico | 659 | Biblioteca Mestre TI v2.1.0 |
| BPD | 128 | Programação e Design |
| PMU | 10 | Prompts Mestres Unificados, propostos |
| WF (planos) | 10 | Workflows, fora da contagem de prompts |

Total: **797 entradas textuais**. A biblioteca histórica tinha **647 canônicos** na versão original e **659** na v2.0. O registro verificável de três arquivos ZIP está em `provenance/sources.json`. A base v2.1 foi copiada sem modificar os conteúdos canônicos e seus manifests.

## Experimente

```bash
python3 -m unittest discover -s tests -v
python3 tools/library.py audit
python3 tools/library.py validate
python3 tools/peos_engine.py validate
python3 -m hub.cli stats
python3 -m hub.cli search --query 'segurança' --limit 5
python3 -m hub.cli compose --goal 'criar projeto de software com CI e testes'
python3 -m hub.cli recommend --goal 'auditar segurança' --limit 5
python3 tools/build_hub_index.py --check
python3 -m http.server 8000
# abra http://localhost:8000/hub-portal/
```

O `compose` herda a classificação heurística v2.1, produz JSON `PLAN_ONLY` e não altera GitHub, banco de dados ou sistemas externos. O portal é estático, funciona sem backend e usa o índice gerado em `hub-portal/catalog.json`.


### Recomendar prompts relacionados (modo somente leitura)

O comando `hub.cli recommend` integra o roteamento determinístico de PMUs com o catálogo de 797 entradas. Ele retorna o plano `PLAN_ONLY`, as referências canônicas reais (ID, caminho e SHA-256) selecionadas pelo manifesto do PMU e sugestões lexicais relacionadas com namespace e status editorial preservados. A recomendação **não** executa prompts, não aprova gates e **não** autoriza a redistribuição dos textos de origem. O limite de resultados relacionados é de 1 a 20; a escolha de PMU pode ser fixada usando `--pmu PMU-007`.

## Documentação

- [Arquitetura e fronteiras](docs/HUB_ARCHITECTURE.md)
- [Catálogo, taxonomia e proveniência](docs/HUB_CATALOG.md)
- [Segurança, agentes e gates](docs/HUB_GOVERNANCE.md)
- [Roadmap P0/P1/P2](docs/HUB_ROADMAP.md)
- [Registro de análise dos ZIPs](docs/SOURCE_AUDIT.md)
- [Planos PEOS e prompts selecionados](plans/INDEX.md)
- [Plano PEOS original de criação](plans/PEOS-KNOWLEDGE-HUB-INITIAL.json)
- [Política de contribuição](CONTRIBUTING.md)

## Integração e publicação

O repositório público [`alexoaraujo/peos-knowledge-hub`](https://github.com/alexoaraujo/peos-knowledge-hub) já possui integrações e CI verificadas no GitHub. A cadeia técnica #12 → #6 → #7 → #9 → #10 → #11 foi integrada por squash, com integridade Windows/Linux, testes Python/Node, Chromium E2E, benchmark e auditoria **automatizada** axe-core.

- **Governança solo:** `protect-main`, Pull Request e quatro checks GitHub Actions obrigatórios; aprovação externa não exigida.
- **Gate de publicação bloqueado:** [direitos/licenciamento de fontes, issue #2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2); ausência de licença explícita nos ZIPs não equivale a permissão de redistribuição.
- **Acessibilidade:** [auditoria manual, issue #8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8) ainda aberta. axe-core automatizado não equivale a certificação WCAG.
- **PMUs:** 10 entradas `PROPOSED`; agentes seguem `PLAN_ONLY`, sem execução externa.
- **Acompanhamento:** [roadmap auditável, issue #14](https://github.com/alexoaraujo/peos-knowledge-hub/issues/14) e [roadmap técnico](docs/HUB_ROADMAP.md).

Não inserir senhas, chaves privadas nem dados pessoais no catálogo. A integração técnica do MVP não autoriza release com licenças não comprovadas.
