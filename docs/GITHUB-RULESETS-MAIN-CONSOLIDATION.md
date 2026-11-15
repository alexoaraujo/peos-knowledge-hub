# Auditoria de proteção da branch main — PEOS Knowledge Hub

## Estado atual verificado pela API GitHub (15/11/2026)

- **Ruleset único:** `protect-main`, ID **27310471**, `target=branch`, `enforcement=active`, restrito a `refs/heads/main`.
- Rulesets anteriores **27310107** e **27310126** não estão mais na lista; a consulta direta ao ID 27310126 retornou **404**.
- `GET /branches/main`: `protected=true`. Proteção clássica `protection.enabled=false` não significa falta de proteção, porque o ruleset está ativo.
- `bypass_actors=[]`: nenhum bypass declarado.
- Aprovação de PR obrigatória, com **1 aprovação**, descarte de aprovações obsoletas após push, aprovação do último push, conversas resolvidas; `require_code_owner_review=false`.
- Histórico linear obrigatório; bloqueio de exclusão e push não fast-forward; apenas squash e rebase.
- `code_quality` restrito a erros; check-runs estritos obrigatórios.

## Checks obrigatórios efetivamente configurados

| Nome do contexto | Integration ID | Verificação |
| --- | ---: | --- |
| `Canonical integrity (windows-latest)` | 15368 | GitHub Actions: publicado e aprovado |
| `Canonical integrity (ubuntu-latest)` | 15368 | GitHub Actions: publicado e aprovado |
| `integridade` | 15368 | GitHub Actions: publicado e aprovado |
| `validate` | 15368 | GitHub Actions: publicado e aprovado |

O status inválido `quality` **não está mais configurado**. Esses quatro contextos foram confrontados com a API `GET /commits/317e911c.../check-runs` na `main`.

## Arquivo JSON

[`protect-main-hardened.proposed.json`](github-rulesets/protect-main-hardened.proposed.json) é uma cópia de referência do alvo configurado: **não deve ser importado novamente**. Importar pode criar regras duplicadas. A regra ativa é o **ID 27310471**; editar sempre esse ID se houver mudanças adicionais.

## Verificações ainda necessárias para G4=PASS

1. Obter pelo menos uma revisão formal independente na [PR #12](https://github.com/alexoaraujo/peos-knowledge-hub/pull/12), vinculada ao HEAD final.
2. Confirmar na UI do GitHub a impossibilidade de merge de uma PR sem aprovação. A ausência de review na #12 e o `Independent review on current SHA` em falha são evidências de review pendente, mas **não bastam isoladamente para comprovar enforcement do ruleset**.
3. Não definir `Independent review on current SHA` como required check antes da integração do workflow na `main` e da verificação do contexto no GitHub Actions; a regra já exige uma aprovação na própria plataforma.
4. Após aprovar e integrar a #12, revalidar os 4 checks no SHA final e, se necessário, atualizar o ruleset com evidência.
5. Concluir a revisão retrospectiva da PR #5 na [issue #13](https://github.com/alexoaraujo/peos-knowledge-hub/issues/13) sem reescrever a história nem alegar aprovação pré-merge.
6. Manter release bloqueado por direitos/licenciamento [issue #2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2) e auditoria manual de acessibilidade [issue #8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8).

**Status:** ruleset consolidado e configuração coerente com a política PEOS; revisão independente e ensaio de enforcement ainda pendentes. Sem novos merges autorizados por esta documentação.
