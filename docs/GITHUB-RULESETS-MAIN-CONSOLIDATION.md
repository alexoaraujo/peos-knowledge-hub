# PEOS — Ruleset da main para mantenedor único

## Estado efetivo verificado em 17/11/2026

Ruleset ativo **`protect-main`** (ID **27310471**) em `refs/heads/main`, sem bypass, com histórico linear, restrições de exclusão/force push, PR obrigatório e checks estritos.

A API confirmou:
- `required_approving_review_count=0` — **já aplicado** no GitHub;
- `require_code_owner_review=false` — já aplicado;
- `require_last_push_approval=false` — **já aplicado** no GitHub: não exige aprovação do último push;
- `require_extra_approval_for_unattributed_changes=true` — continua presente, mas **não exige aprovação extra enquanto `required_approving_review_count=0`**, conforme documentação oficial do GitHub; alterar para `false` é opcional para alinhar visualmente o ruleset ao modo solo;
- `dismiss_stale_reviews_on_push=true`, `required_review_thread_resolution=true` — podem permanecer habilitados sem exigir que haja uma aprovação;
- `allowed_merge_methods=["squash","rebase"]`.

## Quatro checks obrigatórios preservados

| Contexto exato | Aplicativo | Situação |
| --- | --- | --- |
| `Canonical integrity (windows-latest)` | GitHub Actions (15368) | Obrigatório |
| `Canonical integrity (ubuntu-latest)` | GitHub Actions (15368) | Obrigatório |
| `integridade` | GitHub Actions (15368) | Obrigatório |
| `validate` | GitHub Actions (15368) | Obrigatório |

**Política final pretendida:** aprovação humana facultativa, nunca simulada; PR obrigatório, checks no SHA integrado e proteção efetiva da `main`. O workflow de revisão da PR #12 foi adaptado para modo `solo`: passa sem aprovação e mantém os testes de política independente para eventual adoção futura.

## Modo solo validado — nenhum ajuste obrigatório de aprovação pendente

1. Abrir [`protect-main` — ID 27310471](https://github.com/alexoaraujo/peos-knowledge-hub/settings/rules/27310471), sem criar outro ruleset.
2. Em **Require a pull request before merging**, manter a regra, com **Required approvals: 0**.
3. Conferir **Require approval of the most recent reviewable push = desativado** (já confirmado pela API).
4. Opcional: desativar **Require an additional approval for unattributed Copilot pull requests** para clareza. Com zero aprovações mínimas, o GitHub documenta que esta opção não tem efeito.
5. Manter **Require review from Code Owners** desativado; conservar **Require conversation resolution before merging**, checks obrigatórios, histórico linear, bloqueios de exclusão/force push e ausência de bypass.
6. Se editar a configuração opcional, salvar. Reconsultar `GET /repos/alexoaraujo/peos-knowledge-hub/rulesets/27310471`: exigir `required_approving_review_count=0`, `require_last_push_approval=false`, `require_code_owner_review=false`, e confirmar os quatro checks exatos.
7. Fazer teste em uma PR pequena **sem revisão**: checks obrigatórios verdes devem ser suficientes para o merge, sem alterar a biblioteca histórica. Não fazer merge em testes só para demonstrar a regra.

O arquivo [`protect-main-hardened.proposed.json`](github-rulesets/protect-main-hardened.proposed.json) registra os valores propostos. **Não importar como novo ruleset**, pois isso pode duplicar proteção; editar o ruleset atual.

## Limites

O conector conectado disponibiliza leitura de rulesets, mas **não disponibiliza atualização administrativa**. A publicação desta documentação e do JSON não muda os parâmetros ativos automaticamente.

A issue [#13](https://github.com/alexoaraujo/peos-knowledge-hub/issues/13) mantém a ocorrência histórica de merge sem revisão sob a política anterior. A política de mantenedor único passa a ser aplicada prospectivamente; não reescrever eventos antigos.

Licenciamento dos conteúdos (issue #2) e auditoria manual de UX/acessibilidade (issue #8) são gates de release separados e permanecem pendentes.

**Evidência adicional (17/11/2026):** a leitura direta da API confirmou `required_approving_review_count=0`, `require_last_push_approval=false`, `require_code_owner_review=false` e quatro checks obrigatórios. O modo solo de revisão está efetivo no ruleset. O campo Copilot extra approval permanece `true`, mas não exige review com o mínimo zero; consultar [regras GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).
