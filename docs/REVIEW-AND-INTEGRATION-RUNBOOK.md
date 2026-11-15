# Runbook de revisão independente e integração de PRs PEOS

## Estado de referência
A cadeia `#7 → #9 → #10 → #11` está aberta como Draft. Não foram encontradas aprovações formais nas quatro PRs na verificação desta etapa. `#5` (integridade Windows/Linux) e `#6` (coleção BPD) são frentes independentes em Draft.

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
- Tratar #5 e #6 em avaliações independentes, sem misturar mudanças não relacionadas.

## Regraset de proteção recomendado (não aplicado automaticamente)

- Bloquear push direto para `main` quando o plano e visibilidade do repositório permitirem
- Exigir PR, checks obrigatórios, conversas resolvidas e aprovação de colaborador elegível diferente do autor
- Preferir permissões mínimas no CI; `pull_request_target` apenas em cenário estritamente controlado
- Não declarar a regra aplicada sem checar settings do GitHub; esta documentação não muda o ruleset

## Estados PEOS

`PASS`: somente após evidências autenticadas no SHA e revisão pertinente. `BLOCKED`: ausência de permissão, prova, licença ou revisão. `NOT_EVALUATED`: teste ou auditoria não executado. `FAIL`: verificação executada com desvio comprovado.

**Os testes automatizados de axe-core e Playwright não constituem auditoria humana WCAG nem autorização jurídica.**
