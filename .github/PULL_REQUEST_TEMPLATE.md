## PEOS — Revisão técnica e gates

### Contexto
- Issue relacionada:
- Escopo e motivo:
- Prompt(s) PEOS/BPD utilizados:
- Branch de origem e SHA de referência:
- Dependências de PR:
- Arquivos canônicos/manifests afetados? (sim/não; justificar):

### Execução → Verificação → Correção → Testes
- [ ] Diff revisado e alterações justificadas
- [ ] Testes comportamentais reais, sem mocks apresentados como produção
- [ ] CI passa no SHA final (links dos runs abaixo)
- [ ] Nenhum hash, ID canônico ou snapshot histórico reescrito sem aprovação
- [ ] Sem tokens, chaves, informações pessoais ou serviços pagos obrigatórios
- [ ] Logs e links para as evidências incluídos, sem declarar PASS por suposição

### Segurança, UX e documentação
- [ ] Documentação corresponde ao código efetivo (BPD-110/111)
- [ ] Interações e estados de erro testados
- [ ] Teclado, foco, contraste e leitor de tela revisados quando houver UI
- [ ] Acessibilidade automatizada não foi confundida com certificação WCAG
- [ ] Riscos e rollback documentados

### Gates de publicação (não se aplicam automaticamente a toda PR)
- [ ] Licença e autorização de redistribuição comprovadas para cada uma das 3 fontes (issue #2)
- [ ] Revisão independente **formal** por pessoa diferente do autor
- [ ] Revisão manual de acessibilidade e evidências completas (issue #8)
- [ ] Branch protegida e checks obrigatórios no SHA exato
- [ ] Aprovação explícita do release e plano de reversão, se necessário

### Evidências
| Gate | Estado (PASS/FAIL/BLOCKED/N/A) | Link/SHA | Revisor |
| --- | --- | --- | --- |
| Integridade | NOT_EVALUATED | | |
| Regressão | NOT_EVALUATED | | |
| Segurança | NOT_EVALUATED | | |
| UX/acessibilidade | NOT_EVALUATED | | |
| Licença/reutilização | BLOCKED | #2 | |
| Revisão independente | BLOCKED | | |
| Release | BLOCKED | | |

**Aprovação de CI isolada não autoriza merge nem release.** Não marque como pronto sem evidência e revisão humana.
