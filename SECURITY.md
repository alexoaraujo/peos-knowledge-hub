# Segurança — PEOS Knowledge Hub

## Modelo de risco

O núcleo PEOS é um **catálogo estático** de prompts com motor de composição `PLAN_ONLY`; planos **não** executam mutações de infraestrutura. Conteúdo de `prompts/`, `originais/` e ZIPs é dado potencialmente não confiável, nunca código executável. Perfis de agentes têm `permissions=[]` e `execution_mode=PLAN_ONLY`. Não transformar prompts em scripts sem autorização e isolamento apropriados.

## Desenvolvimento e CI

- A `main` é protegida por Pull Request, checks estritos, histórico linear, sem bypass. A política do mantenedor único **não exige revisão por outra pessoa**, mas exige revisão do diff, testes e evidências.
- Os workflows GitHub Actions devem declarar `contents: read`, evitar `pull_request_target` para código não confiável e fixar actions em SHA completo.
- O portal renderiza campos do catálogo com `textContent`; URLs de prompts são caminhos locais validados. Alterações nessa fronteira precisam de testes de injeção, normalização e caminhos.
- Não commitar `.env`, `.npmrc`, `.pypirc`, `node_modules/`, `test-results/`, logs, tokens ou chaves. `.gitignore` é prevenção acidental, **não scanner de segredos**.
- O pipeline usa Python stdlib, npm/Playwright e axe-core apenas em testes. Revisar dependências indiretas e advisories antes de release; versões fixas de dependências diretas não substituem lockfile/SBOM.
- Executar `python3 -m unittest discover -s tests -v`, os checks de integridade, Chromium E2E e axe-core conforme o escopo. Usar `python3 tools/release_preflight.py` para identificar pendências, **não** para aprovar direitos automaticamente.

## Reportar vulnerabilidade

Não publicar credenciais nem provas de exploração em issues abertas. Preferir **GitHub Security Advisories / private vulnerability reporting** se habilitado no repositório; caso indisponível, contatar o mantenedor por um canal privado acordado antes de enviar material sensível. Registros públicos podem descrever o impacto e o estado **sem** os segredos.

Na presença de uma credencial exposta, revogar/rotacionar no provedor de origem, verificar logs e escopo, invalidar a credencial antiga e só então limpar histórico quando necessário, preservando auditoria. Remover um segredo de um commit posterior **não** revoga o segredo já publicado.

## Gate de release

A publicação pública com licença declarada continua bloqueada pelas provas de titularidade/redistribuição ([issue #2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2)), auditoria manual de acessibilidade ([issue #8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8)) e decisão editorial de PMUs `PROPOSED`. Consulte [pré-flight](docs/RELEASE-READINESS.md). A publicação de código em repositório público **não** concede direitos sobre conteúdos de terceiros.
