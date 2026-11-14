# Arquitetura — PEOS Knowledge Hub v0.1

## Princípios
1. **EVIDENCE**: cada versão, prompt, contrato e artefato deve ter origem, hash, confiança e prova.
2. **CONTEXT**: projeto, repositório, ambiente e stack são entradas explícitas; não se presumem estados externos.
3. **GOVERNANCE**: IDs permanentes, versões e status editoriais não se alteram silenciosamente.
4. **SPECIALIZED PROMPTS**: 659 canônicos, 128 BPD e 10 PMUs em namespaces separados.
5. **GATES**: validações falham fechadas; sem evidência independente, o status é pendente/bloqueado.
6. **WORKFLOWS**: planos dependentes de etapas e gates; execução operacional fora do motor e sujeita a autorização.

## Componentes

```text
fontes ZIP (SHA256) ---> provenance/sources.json
                         |
Biblioteca v2.1 --------> catalog/manifest.json + contracts/*.json
         |               colecoes/programacao-design/manifest.json
         |               pmu/manifest.json --> workflows/manifest.json
         |                     |                    |
         +---------------------+--------------------+
                               |
                    hub/catalog.py (consulta)
                      |            |
                 hub/cli.py    tools/build_hub_index.py
                      |            |
              plan-only engine  hub-portal/ (busca estática)
                      |
            revisão humana de autorização/gates
```

## Fronteiras e decisão arquitetural ADR-001
- Armazenar prompts como Markdown, metadados como JSON e índices como artefatos reproduzíveis.
- Usar Python stdlib para o MVP e HTML/JS estático para descoberta; não exigir Neon, Vercel, Auth0, Jira nem tokens.
- Preservar a versão 2.1 imutável na importação; novos componentes habitam `hub/`, `hub-portal/`, `agents/`, `docs/HUB_*`, `provenance/` e `plans/`.
- Não transformar palavras-chave em aprovação, nem simular execução de agentes conectados a ferramentas.
- **Extensões futuras**: API opcional, UI integrada, indexação semântica, múltiplos projetos, autorização real e logs de auditoria.

## Requisitos não funcionais
- Reprodutibilidade: testes de hashes e índice gerado byte-a-byte.
- Segurança: no execution mode; segredos e PII não devem entrar na biblioteca.
- Portabilidade: qualquer ambiente com Python 3.11+ e browser moderno.
- Acessibilidade: portal com controles sem dependência de framework, foco em teclado e textos legíveis.
