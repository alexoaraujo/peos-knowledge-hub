# Matriz de titularidade, proveniência e release — PEOS

**Data da verificação:** 2026-11-14 (Brasil). **Estado:** BLOQUEADO para atribuição de licença global e release open-source, até evidências externas.

## Verificação independente dos três arquivos ZIP recebidos

Inventário efetuado sobre os arquivos ZIP fornecidos nesta conversa, conferindo SHA-256, número de entradas e presença de arquivos nomeados `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` ou `NOTICE`.

| Origem | Entradas | SHA-256 do arquivo ZIP | Papel | Licença explícita no ZIP |
| --- | ---: | --- | --- | --- |
| `Biblioteca_Mestre_TI_Automatizada_Programacao_Design.zip` | 1053 | `d2bf53683f1b4b91a7990cbe2a53b25daea92c3bd6f81646f85f0840545ef324` | Histórico | Não localizada |
| `Biblioteca_Mestre_TI_v2.0_Completa_Automatizada.zip` | 1750 | `f12eb7114d76aa9a1c01e0705b11a48ad6f94e80c174f487ada278ab204b138b` | Histórico | Não localizada |
| `Biblioteca_Mestre_TI_v2.1_Completa_Automatizada(1).zip` | 1782 | `39b1e8dbb1318057ba2ca31f79713f85bc1745d4de618d6deed794600f1556dd` | Canônico | Não localizada |

Os hashes correspondem aos registrados em `provenance/sources.json`. Este inventário **não prova** que os textos sejam livres de direitos de terceiros, nem substitui auditoria jurídica de seus conteúdos. Não foi encontrado arquivo de licença explícita com esses nomes; outras referências textuais a licenças podem existir e devem ser examinadas na revisão de direitos.

## Pendências documentais e responsabilidade

- [ ] Identificar autor/titular dos textos das três bibliotecas e confirmar domínio sobre o material
- [ ] Obter autorização documentada para publicar, modificar, atribuir licença e redistribuir a versão integral
- [ ] Identificar citações e conteúdo derivado de terceiros com termos próprios
- [ ] Definir licença **para o código novo** separadamente da licença do conteúdo editorial
- [ ] Revisar possíveis atribuições exigidas e o arquivo NOTICE, se aplicável
- [ ] Registrar a decisão, o aprovador e as evidências na issue #2 antes de release

## Cadeia de PRs em andamento

```
main
  └─ PR #7 — Portal UX e acessibilidade
       └─ PR #9 — Pesquisa avançada
            └─ PR #10 — Browser E2E e benchmark
                 └─ PR #11 — axe-core WCAG automatizado
```

As PRs possuem testes automatizados. Em modo de mantenedor único, a revisão de outro desenvolvedor é facultativa; não inventar aprovações. O `axe-core` não prova conformidade WCAG completa.

## Critérios de bloqueio de release

**BLOCKED para release** se faltar autorização de redistribuição, suíte no SHA final, auditoria manual de acessibilidade quando relevante, escopo de licença e decisão explícita de publicação. Revisão independente é opcional no modo solo. A publicação prévia do código em repositório público não é prova de autorização/licença sobre o conteúdo.

**Regra PEOS:** Executar → Verificar → Corrigir → Testar → Revisar → Validar → Avançar, sem ultrapassar os gates indisponíveis.
