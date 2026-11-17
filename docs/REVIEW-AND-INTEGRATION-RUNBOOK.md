# PEOS — Revisão, CI e integração para mantenedor único

## Política vigente — modo solo (17/11/2026)

O repositório `alexoaraujo/peos-knowledge-hub` é desenvolvido por um único mantenedor. **Não há exigência de aprovação independente antes do merge**. Qualquer revisão externa é opcional e pode ser registrada sem ser interpretada como bloqueio.

**Os controles técnicos permanecem obrigatórios:** Pull Request, quatro checks GitHub Actions no SHA correto, proteção contra exclusão/force push, histórico linear, conversas resolvidas e rastreabilidade da alteração. Não eliminar checks para contornar erro real.

## Configuração do ruleset

A auditoria atual de [`protect-main` ID 27310471](https://github.com/alexoaraujo/peos-knowledge-hub/settings/rules/27310471) confirmou:
- `required_approving_review_count=0`: configuração solo já efetiva.
- `require_last_push_approval=true`: **precisa ficar false**; caso contrário, revisão do último push pode continuar sendo exigida.
- `require_code_owner_review=false`: correto.
- Quatro checks obrigatórios: `Canonical integrity (windows-latest)`, `Canonical integrity (ubuntu-latest)`, `integridade`, `validate`.
- `required_linear_history`, `deletion`, `non_fast_forward`, `bypass_actors=[]`: preservar.

O conector GitHub pode consultar o ruleset, mas não possui operação administrativa de atualização. Consulte o [procedimento de ajuste](GITHUB-RULESETS-MAIN-CONSOLIDATION.md) antes de tentar mesclar.

## Testes e validação de PR

1. Identificar o HEAD e a base atuais da PR, comparando com `main` e outras branches empilhadas.
2. Executar os quatro checks obrigatórios **no SHA do merge validado**; quando a base mudar, repetir os testes e verificar os diffs.
3. Auditar a integridade do catálogo (659 canônicos, 128 BPD, 10 PMUs, 797 registros), IDs, hashes, ledger, snapshots e índices sem alterar a baseline por conveniência.
4. Para UI, executar Playwright/axe, revisar manualmente teclado, contraste, leitor de tela e viewport e anexar evidências na [issue #8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8).
5. Registrar achados de segurança, riscos e rollback. **Aprovação humana independente é opcional**; não registrar como aprovada caso não exista.
6. Atualizar branches divergentes preferencialmente sem force push, verificar conflitos e novo SHA.
7. Após checks obrigatórios PASS e proteção efetiva, executar merge pelo método aceito (`squash` ou `rebase`), respeitando as pendências de publicação.

## Sequência de integração

- #12 — ajustes de governança solo, CI e documentação
- #6 — validação da coleção BPD, revisão e testes próprios
- #7 → #9 → #10 → #11 — cadeia de portal/UX/pesquisa/E2E/acessibilidade; atualizar as bases sequencialmente e repetir CI antes de cada merge.

Evitar misturar branches não relacionadas ou afirmar que Draft está pronto antes dos testes. Mesmo em modo solo, não fazer merge com CI falhando.

## Gate de release separado

- [Issue #2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2): direitos/licenciamento das fontes continuam bloqueantes para a redistribuição.
- [Issue #8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8): auditoria manual de UX/acessibilidade ainda não concluída.
- [Issue #13](https://github.com/alexoaraujo/peos-knowledge-hub/issues/13): mantém trilha histórica sobre o merge da PR #5 sob regras anteriores. **Mudança de política não reescreve o histórico.**

## Estados

`PASS` exige teste/checagem real; `BLOCKED` significa erro, licença pendente ou restrição técnica efetiva; `NOT_EVALUATED` significa ausência de execução. Não confundir aprovação de CI com licença de redistribuição. O gate de review passa a ser **N/A (solo)**, não `APPROVED` fabricado.
