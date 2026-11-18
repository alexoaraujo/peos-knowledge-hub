# Publicação controlada — PEOS Knowledge Hub (MVP técnico)

Este repositório já possui a biblioteca e o portal integrados à `main`. **Não execute novamente as instruções históricas de importação por ZIP.** O material das três bibliotecas de origem foi incluído no repositório para fins de desenvolvimento e auditoria, mas ainda **não existe autorização de redistribuição/licença open-source comprovada**. A existência de arquivos em um repositório público não autoriza publicá-los com uma licença nova.

## Situação real

- GitHub: [`alexoaraujo/peos-knowledge-hub`](https://github.com/alexoaraujo/peos-knowledge-hub).
- Integração técnica: PRs #4, #5, #12, #6, #7, #9, #10, #11 e #15, com CI remoto Windows/Linux, Python/Node, navegador Chromium e axe-core.
- Política: mantenedor único, sem aprovação de outro desenvolvedor exigida; `main` protegida e checks obrigatórios.
- **Bloqueios de publicação:** [issue #2 — direitos das fontes](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2), [issue #8 — auditoria manual de acessibilidade](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8), homologação editorial dos PMUs (`PROPOSED`) e revisão final de segurança.

## Testar o candidato sem publicar

Na raiz de um checkout do commit exato da PR ou da `main`:

```bash
python3 -m unittest discover -s tests -v
python3 tools/library.py validate
python3 tools/peos_engine.py validate
python3 tools/build_hub_index.py --check
python3 tools/release_preflight.py
```

O último comando emite `release_readiness: BLOCKED` quando faltam evidências. Isso é **esperado**, não um defeito da CI. O modo de bloqueio obrigatório para um futuro processo de release é:

```bash
python3 tools/release_preflight.py --require-evidence
```

Este comando retorna código diferente de zero enquanto `release-authorization/approval.json` estiver ausente ou incompleto. **Não** coloque `--require-evidence` em jobs comuns de PR: isso impediria desenvolvimento legítimo antes da homologação. Veja [critérios e contrato do dossiê](docs/RELEASE-READINESS.md).

## Gate de publicação (após evidências reais)

1. Confirmar autoria, titularidade, direitos de modificação/redistribuição e atribuição dos três ZIPs; não declarar licença por presunção.
2. Concluir auditoria manual de teclado, leitor de tela, contraste e viewport, registrando SHA e links (issue #8).
3. Registrar parecer final de segurança e decisão sobre PMUs `PROPOSED`.
4. Criar dossiê de autorização com links para **evidências reais**, escopo e SHA; não incluir segredos, documentos privados nem dados pessoais em texto versionado.
5. Executar `--require-evidence` no SHA candidato. **Esse pré-flight verifica completude documental, não autenticidade das evidências nem conformidade jurídica/WCAG.** O mantenedor deve conferir as fontes manualmente.
6. Somente depois decidir `LICENSE` e `NOTICE` para código e conteúdo, gerar changelog, tag, artefatos e eventual deploy. A operação de release **não está automatizada** neste repositório.
7. Registrar URL de release, commit, resultados dos checks, decisão de publicação e procedimento de reversão na [issue #14](https://github.com/alexoaraujo/peos-knowledge-hub/issues/14).

As versões em `releases/*.json` são **manifestos históricos do catálogo**, não GitHub Releases publicados nem autorização para redistribuição.
