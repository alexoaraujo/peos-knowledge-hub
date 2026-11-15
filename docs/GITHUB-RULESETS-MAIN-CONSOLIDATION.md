# Consolidação de rulesets da main — auditoria 2026-11-15

## Evidência consultada no GitHub

- `protect-main` — ID **27310107**, `active`, escopo exclusivo `refs/heads/main`.
- `protect-main-hardened` — ID **27310126**, `active`, escopo exclusivo `refs/heads/main`.
- Os dois exigem PR e uma revisão, sem bypass actors.
- Ambos exigem o check `quality` (GitHub Actions, integration_id 15368), **não encontrado** na lista de check runs da `main` (`317e911c5c543e9aef526c4117b0f2793e91a02d`).
- Os quatro contextos efetivamente observados em `main` são `Canonical integrity (windows-latest)`, `Canonical integrity (ubuntu-latest)`, `integridade`, `validate` (app `github-actions`).
- `protect-main-hardened` exige CODEOWNERS review, mas `CODEOWNERS`, `.github/CODEOWNERS` e `docs/CODEOWNERS` não existem na `main`. A aprovação comum de um revisor diferente do autor deve continuar obrigatória.
- `GET /branches/main` retornou `protected: true`. Não confundir `protection.enabled: false` (proteção clássica) com inexistência de **rulesets**, que agora existem.

## Configuração de destino (ainda NÃO aplicada)

A versão proposta está em [`protect-main-hardened.proposed.json`](github-rulesets/protect-main-hardened.proposed.json) — **artefato de referência**, não arquivo de configuração automaticamente lido pelo GitHub.

Preservar: PR obrigatório; 1 approval; stale approvals descartadas; aprovação do último push por pessoa diferente; conversas resolvidas; bloqueio de deleção e force push; histórico linear; squash/rebase; checks estritos; nenhum bypass.

Correções:
1. Remover contexto obrigatório inexistente `quality`.
2. Exigir exatamente os quatro contextos publicados por GitHub Actions no commit validado, vinculados ao app correto.
3. Marcar `Require review from Code Owners` como **false** até cadastrar CODEOWNERS reais com colaboradores independentes elegíveis. O requisito de 1 aprovação permanece ativo.
4. **Não exigir `Independent review on current SHA` nesta fase**: o workflow ainda está em PR #12, não na `main`. Quando integrado e testado, acrescentar esse check obrigatório em alteração separada, observando eventos de atualização de reviews e SHAs.

## Ordem operacional segura

1. Abrir [ruleset hardened — ID 27310126](https://github.com/alexoaraujo/peos-knowledge-hub/settings/rules/27310126). Conferir o escopo `main`.
2. Editar o hardened mantendo estado `active`; ajustar os quatro checks e o requisito de CODEOWNERS conforme acima, salvar.
3. Reconsultar via `GET /rulesets/27310126` para confirmar persistência do estado, `required_status_checks` e parâmetros.
4. **Somente então** acessar [ruleset legado — ID 27310107](https://github.com/alexoaraujo/peos-knowledge-hub/settings/rules/27310107), alterar `Enforcement` de `Active` para `Disabled` (não excluir a política).
5. Reconsultar `GET /rulesets`: hardened deve estar `active`; legado deve estar `disabled`. Confirmar `main.protected=true`.
6. Validar em PR sem approval, confirmando que o merge está bloqueado; validar com colaboração independente legítima, reviews e checks verdes. Não gerar merge de produção apenas para testar.
7. Registrar screenshots/URLs e aprovação independente na [issue #13](https://github.com/alexoaraujo/peos-knowledge-hub/issues/13).

**Observação importante:** este repositório está na conta pessoal `alexoaraujo`. Em alguns planos e modalidades de repos, restrições de ruleset e revisores podem ter nuances de aplicabilidade. Confirmar em **Rules → Rulesets** e no banner de merge de uma PR real. Não criar `CODEOWNERS` apontando exclusivamente para o próprio autor para contornar a aprovação independente.

## Verificação operacional

Conector GitHub nesta conversa permite **ler** rulesets, mas não disponibiliza ferramenta para `PUT/PATCH` ou mudança de `enforcement`. Assim, este artefato **não efetua a configuração** e não pode ser contabilizado como gate G4=PASS até a reconsulta após edição administrativa.
