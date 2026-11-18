## PEOS — Pull Request (mantenedor único)

### Contexto e escopo
- Issue relacionada:
- Objetivo e alterações:
- Prompt(s) PEOS/BPD:
- Branch, base e SHA:
- Impacto em conteúdo canônico/manifests: (sim/não)

### Executar → Verificar → Corrigir → Testar → Validar
- [ ] Diff revisado pelo mantenedor, sem mudanças fora do escopo
- [ ] Testes e integridade no SHA final (com links de runs)
- [ ] GitHub Actions: Windows, Ubuntu, `integridade` e `validate` PASS
- [ ] Nenhum hash, ID, ledger ou snapshot histórico reescrito sem justificativa e autorização
- [ ] Sem secrets, credenciais ou serviços pagos necessários ao pipeline
- [ ] Riscos, rollback e documentação atualizados
- [ ] Para UI: testes de teclado, UX, contraste e acessibilidade conforme issue #8

### Política de revisão
**Modo solo:** aprovação por outra pessoa NÃO é exigida. Comentários e revisões voluntárias são bem-vindos, mas não condicionam o merge. Não declarar revisão independente quando ela não ocorreu.

### Gates adicionais de publicação
- [ ] Direitos/licenciamento das fontes comprovados (issue #2) **antes do release**
- [ ] Acessibilidade e revisão manual comprovadas (issue #8) **antes de certificações/declarações**
- [ ] Checks obrigatórios e ruleset `protect-main` aplicados ao SHA do merge

### Evidências
| Controle | Estado | Link / SHA |
| --- | --- | --- |
| Integridade | NOT_EVALUATED | |
| Regressão Windows/Linux | NOT_EVALUATED | |
| Segurança | NOT_EVALUATED | |
| Revisão humana externa (opcional) | N/A_SOLO | |
| Direitos de conteúdo para release | BLOCKED | #2 |
| Acessibilidade manual para release | NOT_EVALUATED | #8 |

**Review independente não é exigida no modo solo.** Isso não libera merge com CI quebrada nem publicação de conteúdo sem licença adequada.
