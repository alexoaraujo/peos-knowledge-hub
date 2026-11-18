# PEOS — Segurança da cadeia de dependências e análise de código

## Escopo e referências

Este conjunto trata a superfície Python/JavaScript e os workflows do GitHub Actions **sem alterar prompts, manifests, snapshots, release ou credenciais**.

## Controles implementados

| Controle | Implementação | Limite |
| --- | --- | --- |
| Análise estática | `.github/workflows/peos-codeql-security.yml`: CodeQL em Python e JavaScript/TypeScript, consultas `security-extended` | Deve executar e reportar resultados no Code Scanning; não substitui pentest ou revisão manual |
| Supply chain de Actions | `.github/dependabot.yml`: atualizações semanais, três PRs simultâneas no máximo | Não audita npm sem manifesto e lockfile |
| Imutabilidade das Actions | Todas as referências `uses` fixadas em commit SHA de 40 caracteres | SHA correto não garante origem segura ou ausência de vulnerabilidades |
| Credenciais de checkout | `persist-credentials: false` nos oito workflows existentes e no novo CodeQL | Token ainda tem permissões de leitura; o CodeQL recebe `security-events: write` para publicar SARIF |
| Testes de política | `tests/test_repository_security.py`: limita ações, permissões e credenciais | Não substitui auditoria dos próprios provedores |

### CodeQL

O SHA `8aad20d150bbac5944a9f9d289da16a4b0d87c1e` foi verificado como commit do tag `github/codeql-action/v4.36.2`. A nova análise tem dois jobs, um Python e um JavaScript/TypeScript, e dispara para PRs de código, atualizações da `main`, agenda semanal e execução manual.

A permissão `security-events: write` é necessária para o upload; os demais workflows continuam sem essa permissão. Não marcar `SAST PASS` até confirmar a execução real e consultar os alertas.

### Dependabot

O monitoramento semanal cobre exclusivamente `package-ecosystem: github-actions`. Não faz merge automático. A configuração não prova que alertas de segurança, secret scanning ou políticas administrativas de Code Security já estão habilitados; confirmar esses recursos na interface do GitHub e anexar evidências.

## Pendências P1 da próxima rodada

1. Criar `package.json` e `package-lock.json` genuíno, resolvido em ambiente de npm confiável, para `@playwright/test` e `@axe-core/playwright`. Trocar a instalação atual sem lock por `npm ci --ignore-scripts` e habilitar Dependabot `npm` **após** o manifesto validado.
2. Examinar relatórios CodeQL e Dependency Graph; corrigir achados por gravidade, com PRs e checks nos SHAs exatos. Não declarar zero alertas sem inspeção.
3. Verificar secret scanning com acesso administrativo no repositório; desabilitar divulgação de valores de credenciais em logs, revogar qualquer segredo real detectado, preservar evidência sem dados sensíveis.
4. Definir se o job `CodeQL` será required status check depois da primeira execução consistente na `main`. **Não torná-lo obrigatório antes**, para evitar bloqueio indefinido.
5. Validar no runner a matriz CodeQL para Python/JavaScript. Se o GitHub não permitir Code Scanning por política/permissão, registrar o bloqueio e preservar a CI anterior sem bypass.

## Gate de publicação

A análise de segurança **não autoriza** republicação dos três ZIPs nem o release em rascunho. Direitos [#2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2), acessibilidade manual [#8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8), PMUs editoriais [#17](https://github.com/alexoaraujo/peos-knowledge-hub/issues/17) e roadmap [#14](https://github.com/alexoaraujo/peos-knowledge-hub/issues/14) seguem como fontes de decisão.

Referências técnicas: [configuração CodeQL no GitHub](https://docs.github.com/en/code-security/how-tos/find-and-fix-vulnerabilities/secure-your-code/configuring-advanced-setup-for-code-scanning), [atualizações Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-version-updates/configuring-dependabot-version-updates).
