# Roadmap executável — PEOS Knowledge Hub

**Estado em 17/11/2026:** MVP técnico integrado à `main`; release público/licenciamento **BLOCKED**. Os 10 PMUs seguem `PROPOSED` e as composições/agents seguem `PLAN_ONLY`.

## P0 — Integridade e MVP reproduzível

- [x] Importar os 659 prompts canônicos, 128 BPD, 10 PMUs e 10 workflows sem alterar IDs ou hashes históricos.
- [x] Registrar proveniência e hashes dos três ZIPs originais.
- [x] CLI Python stdlib para consulta, estatísticas e composição `PLAN_ONLY`.
- [x] Portal estático, 797 entradas e índice determinístico.
- [x] Testes comportamentais, snapshots, ledger, índices e validação multiplataforma Windows/Ubuntu (PR #5).
- [x] Governança solo, PR obrigatório, quatro checks requeridos e branch protegida (PR #12).
- [x] Integrar validação BPD 128/30 (PR #6).
- [x] Integrar UX responsiva (PR #7), pesquisa facetada (PR #9), Chromium E2E/benchmark (PR #10) e axe-core automatizado (PR #11).
- [ ] Comprovar autorização de redistribuição/licenciamento das fontes (issue #2) **antes de qualquer release open-source**.
- [ ] Homologar editorialmente os 10 PMUs ou documentar expressamente sua exclusão/estado `PROPOSED` no release.
- [ ] Executar auditoria manual de acessibilidade e registrar evidências no SHA final (issue #8).
- [ ] Verificar gate de release final no commit/tag publicado após resolvidos os bloqueios acima.

## P1 — Qualidade e governança operacional

- [x] Template de PR, política para mantenedor único e histórico de proteção da `main`.
- [x] Busca facetada por namespace, categoria, grupo e tags.
- [x] Testes browser Chromium e benchmark de 500 consultas (sanity guard, **não** SLA de produção).
- [x] Auditoria automática axe-core WCAG A/AA dos estados selecionados (**não** atestado WCAG completo).
- [ ] Auditoria manual UX/UI: teclado, leitor de tela, contraste, responsividade e falhas offline (issue #8).
- [ ] Casos de teste e métricas de qualidade de seleção/roteamento de prompts (distintos do benchmark de busca).
- [ ] Contratos JSON Schema para eventos e registro verificável de evidências.
- [ ] Política de publicação/editoria e permissões caso futuramente haja API.

## P2 — Expansão opcional (não implementada)

- [ ] API opcional com autenticação, RBAC e versionamento de composição, somente com necessidade comprovada.
- [ ] Agentes com execução real isolada e trilha de autorização; nunca presumir executor pelos perfis `PLAN_ONLY`.
- [ ] Integrações opcionais GitHub, Jira, Confluence e Neon conforme limites do plano gratuito.
- [ ] Busca semântica com fallback determinístico e avaliação objetiva.
- [ ] Assinatura de release, SBOM e attestations conforme viabilidade e licenciamento.
- [ ] Hospedagem/deploy do portal com política de acesso a conteúdo compatível com direitos verificados.

## Cadeia de integração efetiva

| PR | Componente | Merge SHA |
| --- | --- | --- |
| [#12](https://github.com/alexoaraujo/peos-knowledge-hub/pull/12) | Governança solo | `36460deb05af5ddfd739e1b3bb011e7b3025d8c6` |
| [#6](https://github.com/alexoaraujo/peos-knowledge-hub/pull/6) | Validação BPD | `58910df6f554c77c8238ff7fbcaafab2bac63838` |
| [#7](https://github.com/alexoaraujo/peos-knowledge-hub/pull/7) | Portal UX e responsividade | `3755bdc2b1a9221cccef1ed7be0bb410e64e0394` |
| [#9](https://github.com/alexoaraujo/peos-knowledge-hub/pull/9) | Pesquisa avançada | `f6a1069b5beb7289359aa21891758836f6334514` |
| [#10](https://github.com/alexoaraujo/peos-knowledge-hub/pull/10) | Chromium E2E e benchmark | `4ca24bc9fab14f6072aab51041383c532921d26d` |
| [#11](https://github.com/alexoaraujo/peos-knowledge-hub/pull/11) | axe-core automatizado | `3987170b6475a51ef6aa1618c7cb663651d6ff6d` |

## Governança de conclusão

[Issue #14](https://github.com/alexoaraujo/peos-knowledge-hub/issues/14) mantém o checklist verificável para o release. Revisão externa é facultativa no modo solo; **checks técnicos e direitos de publicação não são facultativos**.

**Definição de pronto de código:** checks obrigatórios `Canonical integrity (windows-latest)`, `Canonical integrity (ubuntu-latest)`, `integridade` e `validate` PASS no SHA integrado, além dos gates de navegador e busca quando aplicáveis. **Definição de release:** licença/autorização, evidências de acessibilidade e decisão editorial dos PMUs; não confundir CI verde com autorização legal ou certificação de acessibilidade.
