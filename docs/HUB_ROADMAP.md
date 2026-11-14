# Roadmap executável — PEOS Knowledge Hub

## P0 — Núcleo reproduzível (MVP local)
- [x] Ingerir v2.1 sem alterar IDs, hashes ou namespaces.
- [x] Registrar hashes dos três ZIPs e inventário comparativo.
- [x] Motor de consulta/estatísticas em Python stdlib.
- [x] Composição `PLAN_ONLY` herdada de v2.1.
- [x] Portal estático e índice reproduzível.
- [x] Testes locais de regressão, integridade e CLI.
- [ ] Importar e auditar todos os arquivos no repositório remoto.
- [ ] Verificar Actions no SHA publicado e revisão independente.
- [ ] Revisar direitos/licença das fontes e homologar PMUs.

## P1 — Governança operacional
- [ ] PR templates, CODEOWNERS e aprovação editorial mínima.
- [ ] Casos de teste para qualidade de roteamento com métricas.
- [ ] Pesquisa avançada por facets, categorias e profissões no portal.
- [ ] Contratos JSON schema para eventos e registro de evidências.
- [ ] RBAC de publicação e trilha de auditoria (se houver API).

## P2 — Plataforma extensível
- [ ] API opcional e interface de composição versionada.
- [ ] Agentes com execução real em sandbox sob gates/autorizações.
- [ ] Integrações GitHub/Jira/Confluence/Neon opcionais.
- [ ] Search semântica com fallback determinístico e avaliação.
- [ ] Releases assinadas e SBOM/attestations quando apropriado.

**Definição de pronto**: testes passam na revisão e SHA exato; hashes íntegros; ausência de segredos; licença revisada; gates externos não são declarados PASS sem provas.
