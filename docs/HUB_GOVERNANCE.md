# Governança, agentes e gates

## Loop PEOS
**Executar → Verificar → Corrigir → Testar → Revisar → Validar → Avançar**. Avançar somente se requisitos, permissões e evidências de cada gate forem suficientes e validados. Para alterações em produção, exigir autorização explícita, rollback e revisão independente.

## Estados
- `PROPOSED`: prompt/agent aguardando aprovação editorial.
- `PLAN_ONLY`: plano gerado; não implica execução.
- `NOT_EVALUATED` / `BLOCKED_UNTIL_VERIFIED`: não há evidência para aprovar gate.
- `PASS`: só após evidência verificável fora do plano, aprovação requerida e verificações reais.
- `FAIL`: qualquer invariante crítica violada; corrigir antes de avançar.
- `N/A`: somente com justificativa documentada.

## Gate padrão
G0 Escopo e autorização; G1 Proveniência e contexto; G2 Integridade e segurança; G3 Testes e critérios de aceite; G4 Revisão independente; G5 Release readiness; G6 Aprovação final/rollback quando aplicável. O workflow original tem seis passos G0–G5; o G6 é um gate adicional do estado de composição, não uma etapa automaticamente cumprida.

## Agentes
As dez descrições em `agents/manifest.json` são **perfis de orquestração planejada**, mapeados 1:1 a PMUs e WFs. Nenhum agente possui credenciais ou executor. A execução de ferramentas só poderá surgir em implementação futura com RBAC, aprovação explícita, trilha de auditoria, idempotência e ambientes descartáveis de teste.

## Segurança de publicação
- Nenhum segredo em arquivos versionados; GitHub Actions com `contents: read` por padrão.
- Executar verificações em PR e main. Evitar `pull_request_target` para código não confiável.
- Markdown e JSON são dados de fonte, nunca comandos a executar por padrão.
- Sem licença no material original; avaliar titularidade e política de redistribuição **antes da publicação open-source definitiva**.
