# Governança, versionamento e gates

## Identidade e ciclo de vida

- Formato: IDs numéricos com quatro dígitos (`0001` ... `9999`), nunca recicláveis.
- Mudanças editoriais com objetivo preservado: ID imutável e incremento de revisão (`revision` + `content_version`).
- Mudanças materiais de finalidade: novo ID; registrar relação `replaces` / `replaced_by` após revisão e manter o antigo como tombstone.
- Status previstos: `ACTIVE`, `DEPRECATED`, `SUPERSEDED`. O snapshot entregue possui 647 ativos e nenhum tombstone.
- SemVer: versão geral da biblioteca (`library_version`) é independente da revisão por prompt (`revision` e `content_version`).
- `sha256` é calculado sobre os bytes UTF-8 da ficha de cada prompt (com `\n`).

## Gates mínimos de PR

| Gate | Evidência requerida | Política |
|---|---|---|
| G0 | Código e manifesto válidos | Obrigatório |
| G1 | IDs únicos; 273 históricos preservados | Obrigatório |
| G2 | Hashes, campos e taxonomy em sincronia | Obrigatório |
| G3 | Eventos para revisões e novos IDs | Obrigatório |
| G4 | Indexação e compilação reproduzíveis | Obrigatório |
| G5 | Testes positivos/negativos | Obrigatório |
| G6 | Revisão semântica por especialista da área | Manual; necessária para publicação oficial |
| G7 | Revisão de segurança/privacidade quando aplicável | Manual, conforme risco |
| G8 | Atestação de release / proteção de branch | Configuração de repositório (ainda não aplicada) |

## Trilhas de auditoria

O ledger `catalog/events.jsonl` registra operações `CREATE`, `EDIT` e futuros `DEPRECATE` / `SUPERSEDE`, com motivo e hash. O snapshot de release permite comparar versões. O baseline histórico em `originais/` não deve ser regravado após sua publicação. O Git fornece autoria e histórico de alterações, desde que o repositório seja protegido.

## Responsabilidades recomendadas

- **Curador da biblioteca**: unicidade de finalidade, aprovação de novos IDs e taxonomia.
- **Revisor especialista**: validação técnica e atualização da documentação oficial.
- **Mantenedor CI**: comandos, testes, dependências e falha fechada dos gates.
- **Security Reviewer**: privilégios, secrets, análise de prompt injection, segurança de automações.
- **Documentação**: índice de mudanças, release notes e rastreabilidade editorial.

Não há automação para publicar, assinar releases ou mudar um repositório GitHub de terceiros sem uma integração e autorização explícitas. Este pacote fornece arquivos para adoção mediante PR.
