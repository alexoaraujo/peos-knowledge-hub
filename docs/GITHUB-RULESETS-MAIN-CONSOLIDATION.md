# PEOS — Ruleset da main para mantenedor único

## Estado efetivo verificado em 17/11/2026

Ruleset ativo **`protect-main`** (ID **27310471**) em `refs/heads/main`, sem bypass, com histórico linear, restrições de exclusão/force push, PR obrigatório e checks estritos.

A API confirmou:
- `required_approving_review_count=0` — **já aplicado** no GitHub;
- `require_code_owner_review=false` — já aplicado;
- `require_last_push_approval=true` — **ainda precisa ser alterado para false** para não depender de revisor do último push;
- `require_extra_approval_for_unattributed_changes=true` — configurado atualmente; o GitHub só exige aprovação extra de PRs sem atribuição quando já existe contagem de aprovações maior que zero; recomendamos `false` por coerência com o modo solo;
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

## Ajuste administrativo pendente

1. Abrir [`protect-main` — ID 27310471](https://github.com/alexoaraujo/peos-knowledge-hub/settings/rules/27310471), sem criar outro ruleset.
2. Em **Require a pull request before merging**, manter a regra, com **Required approvals: 0**.
3. Desmarcar **Require approval of the most recent reviewable push**.
4. Desativar **Require an additional approval for unattributed Copilot pull requests**, se disponível.
5. Manter **Require review from Code Owners** desativado; conservar **Require conversation resolution before merging**, checks obrigatórios, histórico linear, bloqueios de exclusão/force push e ausência de bypass.
6. Salvar. Reconsultar `GET /repos/alexoaraujo/peos-knowledge-hub/rulesets/27310471`: exigir `required_approving_review_count=0`, `require_last_push_approval=false`, `require_code_owner_review=false`, e confirmar os quatro checks exatos.
7. Fazer teste de uma PR pequena **sem revisão**: checks obrigatórios verdes devem ser suficientes para o merge, sem alterar a biblioteca histórica.

O arquivo [`protect-main-hardened.proposed.json`](github-rulesets/protect-main-hardened.proposed.json) registra os valores propostos. **Não importar como novo ruleset**, pois isso pode duplicar proteção; editar o ruleset atual.

## Limites

O conector conectado disponibiliza leitura de rulesets, mas **não disponibiliza atualização administrativa**. A publicação desta documentação e do JSON não muda os parâmetros ativos automaticamente.

A issue [#13](https://github.com/alexoaraujo/peos-knowledge-hub/issues/13) mantém a ocorrência histórica de merge sem revisão sob a política anterior. A política de mantenedor único passa a ser aplicada prospectivamente; não reescrever eventos antigos.

Licenciamento dos conteúdos (issue #2) e auditoria manual de UX/acessibilidade (issue #8) são gates de release separados e permanecem pendentes.
