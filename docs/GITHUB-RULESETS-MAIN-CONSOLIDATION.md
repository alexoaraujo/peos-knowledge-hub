# Auditoria e consolidação de ruleset para `main` — PEOS Knowledge Hub

## Situação efetiva verificada em 15/11/2026

Fonte: GitHub REST `GET /repos/alexoaraujo/peos-knowledge-hub/rulesets`, `GET /rulesets/27310126` e `GET /branches/main`.

- **Único ruleset na listagem**: `protect-main`, ID **27310126**, `enforcement=active`, `refs/heads/main`.
- Antigo ruleset ID **27310107**: consulta direta retornou **404 Not Found**. Não assumir que está apenas `disabled`: o objeto não é encontrado.
- `main.protected=true` graças ao ruleset; a proteção clássica segue `protection.enabled=false`.
- Requer PR, 1 aprovação, descarte de aprovações antigas, aprovação do último push, conversas resolvidas, sem bypass, bloqueio de exclusão/force push, histórico linear e squash/rebase.
- **Pendência 1:** required check `quality` (GitHub Actions, integration ID **15368**) não existe nos check-runs observados no SHA `317e911c5c543e9aef526c4117b0f2793e91a02d` da `main`.
- **Pendência 2:** `require_code_owner_review=true`, embora nenhuma das localizações padrão contenha `CODEOWNERS`. Não confundir isso com bloqueio comprovado: sua aplicabilidade depende dos arquivos afetados e de um CODEOWNERS válido.
- **Pendência 3:** aprovação independente ainda não registrada na PR #12. Workflow `Independent review on current SHA` permanece somente na branch da PR #12.

## Quatro checks reais identificados

| Contexto GitHub Actions | App ID | Verificado |
| --- | ---: | --- |
| `Canonical integrity (windows-latest)` | 15368 | SIM |
| `Canonical integrity (ubuntu-latest)` | 15368 | SIM |
| `integridade` | 15368 | SIM |
| `validate` | 15368 | SIM |

**Configuração-alvo de referência:** [`protect-main-hardened.proposed.json`](github-rulesets/protect-main-hardened.proposed.json). O nome do arquivo é histórico; o conteúdo proposto deve manter o nome **`protect-main`** e o **ID existente 27310126** na edição pelo GitHub UI. Arquivos de configuração no repositório **não alteram automaticamente** rulesets.

## Sequência de ajustes administrativos — sem excluir regras adicionais

1. Abrir [ruleset ativo ID 27310126](https://github.com/alexoaraujo/peos-knowledge-hub/settings/rules/27310126). Confirmar `enforcement=active` e escopo apenas `main`.
2. Remover o required status `quality` e incluir os quatro checks acima, selecionando o app GitHub Actions (ID 15368).
3. Manter 1 aprovação independente, stale review dismissal, last-push approval, resolved threads, linear history, proteção contra exclusão e push forçado.
4. Enquanto não existir CODEOWNERS com um **revisor elegível diferente do autor**, definir temporariamente `Require review from Code Owners=false`. Isso **não** reduz o requisito mínimo de aprovação geral.
5. Salvar e fazer nova consulta do ruleset. Confirmar exatamente os quatro contextos, `CODEOWNERS=false`, nenhuma regra `quality`.
6. Verificar [Settings → Rules](https://github.com/alexoaraujo/peos-knowledge-hub/settings/rules): somente ID **27310126** deve aparecer. O antigo **27310107** já retornou 404; não há outra regra ativa a desativar na última consulta.
7. Testar que uma PR sem review não pode ser mesclada; uma PR com revisão legítima e checks completos deve cumprir os gates. Não mesclar mudanças irreversíveis apenas para ensaio.
8. Registrar as provas e links na [issue #13](https://github.com/alexoaraujo/peos-knowledge-hub/issues/13).

## Limitações e risco de deadlock

- O conector nesta conversa é de leitura para rulesets; **nenhuma atualização administrativa foi aplicada** por esta auditoria.
- Não exigir o check `Independent review on current SHA` enquanto o workflow não estiver na `main`. A PR #12 deve ser revisada e aprovada independentemente antes da integração.
- Os checks `integridade` e `validate` são nomes genéricos: confirmar a associação ao app GitHub Actions e evitar outros workflows com mesmo contexto.
- O arquivo de referência documenta o estado desejado, **não** o estado real. O gate PEOS G4 somente passa após verificação da proteção efetiva e revisão independente.
