# Arquitetura PEOS Knowledge Hub — v0.1

A arquitetura foi derivada da Biblioteca Mestre TI v2.1.0. Este documento acompanha o **bootstrap remoto**; a implementação integral está preparada no arquivo `PEOS_Knowledge_Hub_v0.1.0.zip`.

## Seis camadas

1. **EVIDENCE** — origem, hash SHA-256, confiança, prova.
2. **CONTEXT** — projeto, repositório, stack e ambiente explícitos.
3. **GOVERNANCE** — IDs permanentes, versionamento e estados editoriais.
4. **SPECIALIZED PROMPTS** — 659 canônicos, 128 BPD, 10 PMUs.
5. **GATES** — segurança, integridade, testes, revisão e autorização; falha fechada.
6. **WORKFLOWS** — 10 planos versionados com etapas e evidências.

## Stack prevista

Python 3 (stdlib), arquivos Markdown/JSON, portal estático HTML/CSS/JS e GitHub Actions; sem serviços pagos obrigatórios.

## Regras inegociáveis

- Não reciclar IDs ou reescrever hashes da baseline.
- Não confundir prompts BPD e canônicos: relação não implica equivalência.
- PMUs permanecem `PROPOSED`, agentes `PLAN_ONLY`.
- Sem mutações em sistemas externos por composição; a autorização é separada.
- Gate só é `PASS` com evidência real e validação no ambiente.
- Licenciamento das fontes é requisito pendente de aprovação.

## Plano P0

- [ ] Importação integral e PR de revisão (issue #1)
- [ ] Revisão de titularidade e licença (issue #2)
- [ ] CI remoto no SHA final (issue #3)

O pacote local aprovado teve **37 testes** (8 novos + 29 herdados) e foi validado sem alterar os contratos do material original.