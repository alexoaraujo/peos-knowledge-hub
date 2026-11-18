# Governança, agentes e gates

## Loop PEOS
**Executar → Verificar → Corrigir → Testar → Revisar → Validar → Avançar**. Avançar somente se requisitos, permissões e evidências de cada gate forem suficientes e validados. Para alterações em produção, exigir autorização explícita, plano de rollback e revisão técnica documentada. No modo solo, uma aprovação externa não é obrigatória; controles técnicos e autorizações de publicação permanecem obrigatórios.

## Estados
- `PROPOSED`: prompt/agent aguardando aprovação editorial.
- `PLAN_ONLY`: plano gerado; não implica execução.
- `NOT_EVALUATED` / `BLOCKED_UNTIL_VERIFIED`: não há evidência para aprovar gate.
- `PASS`: só após evidência verificável fora do plano, aprovação requerida e verificações reais.
- `FAIL`: qualquer invariante crítica violada; corrigir antes de avançar.
- `N/A`: somente com justificativa documentada.

## Gate padrão
G0 Escopo e autorização; G1 Proveniência e contexto; G2 Integridade e segurança; G3 Testes e critérios de aceite; G4 Revisão técnica pelo mantenedor (review externo opcional); G5 Release readiness; G6 Aprovação final/rollback quando aplicável. O workflow original tem seis passos G0–G5; o G6 é um gate adicional do estado de composição, não uma etapa automaticamente cumprida. Nenhum gate de liberação de direitos autorais é dispensado pela política de revisão solo.

## Agentes
As dez descrições em `agents/manifest.json` são **perfis de orquestração planejada**, mapeados 1:1 a PMUs e WFs. Nenhum agente possui credenciais ou executor. A execução de ferramentas só poderá surgir em implementação futura com RBAC, aprovação explícita, trilha de auditoria, idempotência e ambientes descartáveis de teste.

## Segurança de publicação
- Nenhum segredo em arquivos versionados; GitHub Actions com `contents: read` por padrão.
- Executar verificações em PR e main. Evitar `pull_request_target` para código não confiável.
- Markdown e JSON são dados de fonte, nunca comandos a executar por padrão.
- Sem licença no material original; avaliar titularidade e política de redistribuição **antes da publicação open-source definitiva**.

## Regra de integração verificada para mantenedor único

O repositório exige alterações em `main` por PR, histórico linear e checks obrigatórios `Canonical integrity (windows-latest)`, `Canonical integrity (ubuntu-latest)`, `integridade` e `validate` (app GitHub Actions). Zero aprovações externas são exigidas no modo solo; nenhuma revisão inexistente deve ser declarada. Os checks de Chromium/axe-core e pesquisa são exigidos como evidências adicionais quando o escopo os aciona.

O conteúdo permanece em repositório público, mas a publicação de um release de biblioteca com licença open-source depende de [direitos e titularidade, issue #2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2). A [auditoria manual de acessibilidade, issue #8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8) não pode ser substituída pela ausência de violações nos testes automatizados.
