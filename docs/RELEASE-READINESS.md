# PEOS — Dossiê verificável de preparação para release

**Estado de referência:** `BLOCKED` enquanto não forem comprovados os direitos de redistribuição, a auditoria manual de acessibilidade, a revisão de segurança e a decisão editorial dos PMUs. Este arquivo documenta como coletar evidências; **não aprova nenhuma delas**.

## Comandos

```bash
python3 tools/release_preflight.py
python3 tools/release_preflight.py --require-evidence \\
  --authorization-file /secure-external-location/approval.json \\
  --acknowledge-reviewed-evidence
```

O primeiro comando verifica a consistência mínima dos três registros de fontes, dos dez PMUs (`PROPOSED`) e dos dez agentes (`PLAN_ONLY`) e informa pendências sem bloquear CI de desenvolvimento. O segundo **falha fechado** na falta de dossiê para o commit exato e se destina a pré-flight manual de uma futura publicação, não à liberação automática.

## Dossiê necessário

Somente **depois de verificar documentos reais**, o mantenedor poderá criar um dossiê `approval.json` **fora do checkout do candidato** (por exemplo em uma pasta privada e controlada). O arquivo não existe por padrão. Incluir `approval.json` no mesmo commit que seu campo `target_sha` descreve cria uma **referência circular impossível de satisfazer**, pois o commit muda ao adicionar o documento. A verificação exige `--authorization-file /caminho/fora/do/repo/approval.json`, além de `--acknowledge-reviewed-evidence` para o operador declarar que examinou manualmente os comprovantes. Contrato exigido:

| Propriedade | Valor / evidência esperada |
| --- | --- |
| `schema_version`, `project` | `1.0.0`, `peos-knowledge-hub` |
| `target_sha` | Commit SHA completo de 40 caracteres do candidato |
| `approved_by` | Login do mantenedor responsável pela decisão; modo solo é permitido |
| `source_rights` | **Três** registros, um por `archive_sha256` em `provenance/sources.json`, com `rights_holder`, `permission_scope=redistribute_and_modify` e `evidence_url` |
| `manual_accessibility` | `verified=true`, `tested_sha=target_sha`, `evidence_url` da auditoria manual — issue #8 |
| `security_review` | `verified=true`, `tested_sha=target_sha`, `evidence_url` com parecer, escopo e riscos aceitos |
| `pmu_editorial` | `decision=retain_proposed` ou `exclude`, com `evidence_url` de decisão explícita |

Os `evidence_url` devem apontar para registros HTTPS verificáveis e apropriados para publicação. Não publique credenciais, dados pessoais, contratos integrais ou documentos privados nos links; use referência controlada, descrição e hash de evidência quando for necessário preservar confidencialidade.

Os três SHA-256 exigidos são os de `provenance/sources.json`:

- Programação/Design: `d2bf53683f1b4b91a7990cbe2a53b25daea92c3bd6f81646f85f0840545ef324`
- Biblioteca Mestre v2.0: `f12eb7114d76aa9a1c01e0705b11a48ad6f94e80c174f487ada278ab204b138b`
- Biblioteca Mestre v2.1: `39b1e8dbb1318057ba2ca31f79713f85bc1745d4de618d6deed794600f1556dd`

## Validação humana obrigatória além do script

O script verifica **estrutura e presença de declarações** e não possui acesso, competência jurídica ou autenticação para validar que um titular realmente concedeu direitos, que um link comprova a alegação ou que um teste manual ocorreu. Dossiês com dados falsos podem passar na checagem sintática; a validação humana real e o controle de PR são indispensáveis.

- **Issue #2:** determinar titularidade, trechos de terceiros, permissões de modificação e redistribuição, licenças para código e conteúdo e atribuições/NOTICE. Não inventar licença ausente.
- **Issue #8:** registrar teclado e foco, NVDA/VoiceOver, contraste, viewports 320/375/768px e desktop, links de prompts, erro/retry, resultado vazio e navegação. axe-core automatizado não substitui esta avaliação.
- **Segurança:** confirmar dependências e versões, integridade do catálogo e links, regras de Actions, segredos e ausência de permissões desnecessárias.
- **PMUs:** manter `PROPOSED` e `PLAN_ONLY` e decidir documentalmente entre publicar com rótulo explícito de proposta ou excluir esses itens de um artefato distribuído. O pré-flight **não altera** o catálogo para fazer a decisão passar.

## Política de execução e limites

1. O modo solo dispensa **revisor externo**, não direitos autorais, evidências, checks e autorização de publicação.
2. O repositório **não possui workflow de publicação automática** controlado por este script. Ele precisa ser invocado antes de toda futura criação de release/tag/artefato — e deve ser incorporado a um workflow de release quando esse existir.
3. O dossiê fica **fora do commit auditado**. Nenhuma evidência externa foi criada por esta PR. O modo estrito falha também se o arquivo estiver dentro do checkout ou se `--target-sha` não coincidir com o HEAD real.
4. `--acknowledge-reviewed-evidence` significa somente que o operador declara ter revisado as fontes: o programa **não abre URLs, não verifica autenticidade de permissões e não certifica WCAG**. A decisão real de publicação permanece do mantenedor.
5. Não abrir release enquanto faltarem evidências e não rotular este controle como `LICENSING_APPROVED` ou `WCAG_COMPLIANT` automaticamente.

Acompanhar os gates em [#14](https://github.com/alexoaraujo/peos-knowledge-hub/issues/14), direitos em [#2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2) e acessibilidade em [#8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8).
