# Segurança — PEOS Knowledge Hub

## Modelo de risco

O núcleo PEOS é um **catálogo estático** de prompts com motor de composição `PLAN_ONLY`; planos **não** executam mutações de infraestrutura. Conteúdo de `prompts/`, `originais/` e ZIPs é dado potencialmente não confiável, nunca código executável. Perfis de agentes têm `permissions=[]` e `execution_mode=PLAN_ONLY`. Não transformar prompts em scripts sem autorização e isolamento apropriados.

## Desenvolvimento e CI

- A `main` é protegida por Pull Request, checks estritos, histórico linear, sem bypass. A política do mantenedor único **não exige revisão por outra pessoa**, mas exige revisão do diff, testes e evidências.
- Os workflows GitHub Actions devem declarar `contents: read`, evitar `pull_request_target` para código não confiável, desabilitar persistência de credenciais em `actions/checkout` e fixar actions em SHA completo. A análise CodeQL é uma exceção controlada de permissão: precisa exclusivamente de `security-events: write` para enviar resultados de segurança.
- O portal renderiza campos do catálogo com `textContent`; URLs de prompts são caminhos locais validados. Alterações nessa fronteira precisam de testes de injeção, normalização e caminhos.
- Não commitar `.env`, `.npmrc`, `.pypirc`, `node_modules/`, `test-results/`, logs, tokens ou chaves. `.gitignore` é prevenção acidental, **não scanner de segredos**.
- O pipeline usa Python stdlib, npm/Playwright e axe-core apenas em testes. Revisar dependências indiretas e advisories antes de release; versões fixas de dependências diretas não substituem lockfile/SBOM.
- Executar `python3 -m unittest discover -s tests -v`, os checks de integridade, Chromium E2E e axe-core conforme o escopo. Usar `python3 tools/release_preflight.py` para identificar pendências, **não** para aprovar direitos automaticamente.

## Reportar vulnerabilidade

Não publicar credenciais nem provas de exploração em issues abertas. Preferir **GitHub Security Advisories / private vulnerability reporting** se habilitado no repositório; caso indisponível, contatar o mantenedor por um canal privado acordado antes de enviar material sensível. Registros públicos podem descrever o impacto e o estado **sem** os segredos.

Na presença de uma credencial exposta, revogar/rotacionar no provedor de origem, verificar logs e escopo, invalidar a credencial antiga e só então limpar histórico quando necessário, preservando auditoria. Remover um segredo de um commit posterior **não** revoga o segredo já publicado.

## Gate de release

A publicação pública com licença declarada continua bloqueada pelas provas de titularidade/redistribuição ([issue #2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2)), auditoria manual de acessibilidade ([issue #8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8)) e decisão editorial de PMUs `PROPOSED`. Consulte [pré-flight](docs/RELEASE-READINESS.md). A publicação de código em repositório público **não** concede direitos sobre conteúdos de terceiros.

## Verificações adicionais de supply chain

- [`peos-codeql-security.yml`](.github/workflows/peos-codeql-security.yml) analisa Python e JavaScript com CodeQL fixado no commit da versão 4.36.2; resultados dependem de Code Scanning habilitado e da permissão concedida pelo GitHub. A configuração de workflow **não prova execução concluída**.
- [`.github/dependabot.yml`](.github/dependabot.yml) verifica atualizações semanais de GitHub Actions e abre PRs. Não há merge automático.
- O workflow Chromium ainda instala `@playwright/test` e `@axe-core/playwright` sem um `package-lock.json`; as dependências transitivas podem variar. Tratar lockfile com `npm ci` e inventário de dependências como melhoria P1 futura, sem gerar lockfile manualmente ou fingir um npm audit realizado.
- Nenhum check está autorizado a imprimir valores de secrets. O uso de `persist-credentials: false` reduz a exposição acidental do token de checkout, mas não substitui regras de permissão, rotação, SAST ou secret scanning nativo.

Ver [plano de segurança e cadeia de dependências](docs/SECURITY-SUPPLY-CHAIN.md).
