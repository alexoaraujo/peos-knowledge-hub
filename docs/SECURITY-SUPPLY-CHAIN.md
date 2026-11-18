# PEOS — Segurança da cadeia de dependências e evidências

## Baseline técnico verificado em 18/11/2026

| Controle | Estado confirmado | Limite da evidência |
| --- | --- | --- |
| CodeQL | `.github/workflows/peos-codeql-security.yml` analisa Python e JavaScript/TypeScript; `init` e `analyze` fixados no mesmo SHA `33d7b85da1a04171e211befe2c739303b9a4c066` (v4.39.3) | Execução SUCCESS e upload SARIF não demonstram ausência de alertas abertos |
| GitHub Actions | Ações com pin SHA de 40 caracteres; `actions/checkout` v7.0.1 no SHA `3d3c42e5aac5ba805825da76410c181273ba90b1` | Pin reduz mutabilidade, mas não substitui análise de origem e advisories |
| Credenciais | Checkouts usam `persist-credentials: false`; workflows declaram `contents: read`; CodeQL recebe `security-events: write` e `actions: read` | A permissão efetiva do token de cada execução depende também das políticas da plataforma |
| Dependências npm | `package.json` privado, `package-lock.json` v3 e `npm ci --ignore-scripts --no-audit --no-fund` no E2E | `--no-audit` dispensa a auditoria npm durante instalação; consultar alertas separadamente |
| Dependabot | Atualizações semanais para `github-actions` e `npm`, sem auto-merge configurado | PRs do Dependabot não substituem verificação de alertas ativos |
| Navegador | Chromium E2E, axe-core e benchmark; `@playwright/test` v1.65.1 verificado na `main` | Testes automatizados não constituem homologação manual integral WCAG |

## Governança observada

A ruleset [`protect-main`](https://github.com/alexoaraujo/peos-knowledge-hub/rules/27506105) ID `27506105` está ativa para `refs/heads/main`, sem bypass actors, com histórico linear, restrição a force-push/exclusão, PR obrigatória e política de mantenedor único (`required_approving_review_count: 0`). Os quatro checks obrigatórios efetivos são:

- `Canonical integrity (windows-latest)`
- `Canonical integrity (ubuntu-latest)`
- `integridade`
- `validate`

CodeQL e Chromium E2E executam em seus escopos, **mas não integram essa lista de required checks**. Antes de promover qualquer job com filtro de `paths` a required check, verificar a semântica de skipped/pendente e assegurar um check estável em todas as PRs; um required check não acionado pode bloquear a integração indefinidamente. Alterações administrativas na ruleset exigem permissão específica e não foram aplicadas nesta auditoria.

## Endurecimento desta rodada

CodeQL passa a acompanhar também mudanças em `package.json` e `package-lock.json` nos eventos `pull_request` e `push`; um teste de regressão exige os dois gatilhos. Isso amplia a análise estática de PRs de dependências, mas **não é substituto de Dependabot alerts nem `npm audit`**.

## Controles sem comprovação de leitura

Os endpoints de Code Scanning alerts, Dependabot alerts, Secret Scanning alerts e configurações administrativas de GitHub Actions não puderam ser consultados pelo conector desta sessão. A consulta direta à proteção clássica da branch retornou `403`; a ruleset foi lida por endpoint autorizado. Portanto, **não declarar zero vulnerabilidades, zero segredos expostos ou retenção global conforme** sem evidência adicional.

Para concluir a [issue #26](https://github.com/alexoaraujo/peos-knowledge-hub/issues/26), registrar por canal seguro: contagem/IDs e severidades dos alertas abertos, triagem e remediação de high/critical, configuração efetiva de secret scanning/push protection se disponível, política de retenção da Actions e permissões efetivas de fork/token. Não colar valores de segredos ou tokens em issues públicas.

O artefato de falha do Chromium está limitado no workflow a `retention-days: 7`; esta configuração **não prova** a retenção global de logs nem configurações de outros artefatos. Evidências devem incluir run ID, SHA, data UTC, escopo e resultado.

## Gate de publicação separado

CI bem-sucedido não autoriza redistribuição de material de terceiros. Manter os gates de direitos [#2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2), acessibilidade manual [#8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8), PMUs editoriais [#17](https://github.com/alexoaraujo/peos-knowledge-hub/issues/17) e roadmap [#14](https://github.com/alexoaraujo/peos-knowledge-hub/issues/14) independentes da engenharia de segurança.
