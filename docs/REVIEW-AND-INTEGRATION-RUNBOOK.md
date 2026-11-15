# Runbook de revisão independente e integração de PRs PEOS

## Atualização de configuração — 15/11/2026

A auditoria de rulesets descrita abaixo como ausência de proteção é **histórica** e já não representa o estado atual. A leitura mais recente do GitHub retorna:
- Único ruleset **`protect-main` ID 27310126**, ativo para `main`; `main.protected=true`.
- Ruleset antigo ID 27310107: **404 Not Found**, não apenas desativado.
- Required check ainda configurado incorretamente como `quality`; o check não figura entre os contextos da CI disponíveis.
- CODEOWNERS review exigida embora não haja arquivo CODEOWNERS nos locais reconhecidos.
- A [proposta atualizada](GITHUB-RULESETS-MAIN-CONSOLIDATION.md) define os quatro required checks reais e a sequência segura de remediação administrativa.
- Não houve alteração administrativa por este documento. G4 permanece bloqueado pela ausência de aprovação formal independente e pela configuração efetiva de checks ainda pendente.

## Estado de referência
A cadeia `#7 → #9 → #10 → #11` permanece independente do gate documental. A PR #5 (integridade Windows/Linux) **já foi mesclada na `main`**, em 2026-11-15T03:04:46Z (merge SHA `317e911c5c543e9aef526c4117b0f2793e91a02d`). A API de reviews da PR #5 retornou **zero revisões formais**, embora a CI Windows/Ubuntu tenha aprovado 41/41 testes; o desvio G4 foi registrado na issue #13. A PR #6 permanece aberta como Draft, e a PR #12 contém esta remediação documental.

## Execução da revisão (BPD-075/076/077/109/110/111/113/118)

1. Um revisor **diferente do autor** deve comparar o diff da PR específica e seu SHA final. A revisão de um agente de IA pode auxiliar a detectar problemas, mas não substitui a aprovação humana exigida.
2. Conferir links de CI no SHA final; execução anterior não é evidência após novos commits.
3. Revisar invariantes: 659 IDs canônicos, 128 BPD, 10 PMUs PROPOSED, 10 workflows e 797 entradas; arquivos originais sem reescrita indevida.
4. Conferir se os prompts/planos seguem `PLAN_ONLY`, sem segredos e sem reivindicação de funcionalidades não implementadas.
5. Para interface: executar manualmente leitor de tela, contraste, teclado, estados vazios, erros e telas móveis; registrar screenshots e relatório na issue #8.
6. Examinar fontes/licenças e autorizações na issue #2; não atribuir licença global unilateralmente.
7. Solicitar correções em PR específica, executar novamente testes e verificar a revisão formal. Só então considerar `Ready for Review` e merge.

## Integração empilhada e atualização de bases

- Integrar **#7 → main** somente após aprovação independente e controles aplicáveis.
- Atualizar a base da **#9** para `main` **depois** da integração da #7 e verificar que os commits/arquivos da #7 não reapareçam no diff.
- Integrar #9; atualizar a base da #10 para `main`; repetir conferência de diff/CI.
- Integrar #10; atualizar a base da #11 para `main`; repetir conferência.
- Não realizar `force push` nem ignorar required checks sem autorização. A atualização das bases pode disparar novos testes.
- Para a #5, executar **auditoria retrospectiva independente** e registrar parecer na issue #13, sem apresentar aprovação posterior como aprovação pré-merge.
- Tratar #6 em avaliação independente, sem misturar mudanças não relacionadas; atualizar a base somente com inspeção do diff e checks no novo SHA.

## Proteção da main: diagnóstico confirmado e configuração necessária

- Exigir Pull Request para alterar `main` e impedir push direto ou bypass não autorizado quando o plano e visibilidade permitirem.
- Exigir no mínimo **uma aprovação formal de colaborador elegível diferente do autor**, descartar aprovações obsoletas após push quando disponível e resolver conversas antes do merge.
- Exigir os checks obrigatórios estáveis (inclusive integridade Windows/Ubuntu) no SHA efetivamente mesclado, evitando depender de runs de commits anteriores.
- Configurar especificamente a aplicabilidade a administradores e possíveis bypasses; somente autorizar exceções sob procedimento de emergência auditável.
- Preferir permissões mínimas no CI; evitar `pull_request_target` para código não confiável.
- Executar ensaio negativo em PR descartável (sem review: **bloqueia**) e positivo (review por revisor elegível + checks: **permite**), registrando evidências e link do ruleset na issue #13.
- **Leitura confirmada via GitHub API em 15/11/2026:** `GET /repos/alexoaraujo/peos-knowledge-hub/rulesets` retornou `[]`; `GET /repos/alexoaraujo/peos-knowledge-hub/branches/main` retornou `protected: false` e `protection.enabled: false`. O endpoint de branch protection detalhada retornou `403 Resource not accessible by integration`. Portanto, a `main` está sem proteção ativa, mas não há autorização de escrita administrativa disponível nesta conexão. **Não declarar regras aplicadas.**

## Incidente de governança G4 — evidências e restrições

| Campo | Evidência |
| --- | --- |
| PR | [#5](https://github.com/alexoaraujo/peos-knowledge-hub/pull/5) |
| Merge | [`317e911c5c543e9aef526c4117b0f2793e91a02d`](https://github.com/alexoaraujo/peos-knowledge-hub/commit/317e911c5c543e9aef526c4117b0f2793e91a02d) |
| Head validado | `4438a4a8e92a47aa28afc27d9b8eb3170120a15e` |
| Testes | [Windows e Ubuntu PASS](https://github.com/alexoaraujo/peos-knowledge-hub/actions/runs/43669518684) |
| Review formal GitHub | Nenhuma revisão retornada pela API no momento da auditoria |
| Exceção PEOS G4 | [Issue #13](https://github.com/alexoaraujo/peos-knowledge-hub/issues/13), aberta |
| Histórico `main` | Merge da #5 confirmado como HEAD durante a auditoria |
| Ruleset/branch protection | **CONFIRMADO SEM PROTEÇÃO:** `rulesets=[]`, `main.protected=false`; consulta detalhada retorna HTTP 403 para a integração |

A ausência de revisão formal registrada **não** permite afirmar qual configuração ou bypass possibilitou o merge. Verificar ruleset, direitos de bypass e mecanismo de aprovação. Uma revisão feita posteriormente é *retrospectiva*, não apaga a ocorrência.

## Estados PEOS

`PASS`: somente após evidências autenticadas no SHA e revisão pertinente. `BLOCKED`: ausência de permissão, prova, licença ou revisão. `NOT_EVALUATED`: teste ou auditoria não executado. `FAIL`: verificação executada com desvio comprovado.

**Os testes automatizados de axe-core e Playwright não constituem auditoria humana WCAG nem autorização jurídica.**

## Verificador automatizado de revisão independente (PR #12)

O workflow `.github/workflows/peos-independent-review.yml` executa `tests/test_independent_review_gate.py` e consulta o endpoint de reviews da PR para exigir:
- aprovação `APPROVED` atribuída a outro usuário, ligada exatamente ao `head.sha` atual;
- nenhuma solicitação de alterações `CHANGES_REQUESTED` pendente de outro revisor;
- rejeição de autoaprovação, review obsoleto, review `DISMISSED` e ausência de metadados.

O verificador usa apenas `contents:read` e `pull-requests:read`, não contém secrets adicionais e **não altera PRs**. Seu status será negativo até surgir aprovação elegível, o que é o comportamento esperado (fail-closed). A execução isolada não protege a `main`.

### Etapas administrativas para ativação obrigatória

1. Abrir [GitHub Settings → Rules → Rulesets](https://github.com/alexoaraujo/peos-knowledge-hub/settings/rules).
2. Criar ruleset ativo destinado à branch `main`; exigir Pull Request antes do merge.
3. Solicitar ao menos **uma aprovação independente**, considerar `Dismiss stale approvals` e bloquear conversas não resolvidas; impedir bypass administrativo não autorizado.
4. Adicionar como required checks, após publicação do workflow na branch padrão e disponibilidade dos contextos: `Independent review on current SHA`, `Canonical integrity (windows-latest)`, `Canonical integrity (ubuntu-latest)`, `validate` e `integridade` **somente após conferir os nomes exatos no GitHub**.
5. Testar uma PR descartável sem aprovação (merge bloqueado) e outra com aprovação elegível + checks verdes (merge permitido); registrar evidências na [issue #13](https://github.com/alexoaraujo/peos-knowledge-hub/issues/13).

**Importante:** os nomes `validate` e `integridade` podem não ser globalmente exclusivos, e required checks devem referenciar o app e contexto concretos. A escolha final exige inspeção dos checks no GitHub. Não inserir um check novo como obrigatório antes que o workflow esteja publicado na branch padrão e funcionando, para não provocar deadlock operacional.
