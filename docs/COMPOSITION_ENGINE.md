# Motor de composição PEOS v2.1

## Arquitetura

- **Catálogo imutável:** 659 IDs canônicos com hashes herdados da v2.0.
- **Namespace PMU:** 10 orquestradores `PMU-001` a `PMU-010`, sem consumir IDs numéricos.
- **Workflows:** 10 planos `WF-001` a `WF-010`, com etapas, gates e exigência de evidências.
- **Roteador:** correspondência determinística de palavras-chave; não é classificador semântico.
- **Executor:** deliberadamente ausente; a ferramenta produz planos, não altera ambientes.

## Uso

```bash
python3 tools/peos_engine.py validate
python3 tools/peos_engine.py compose --goal 'auditoria integral de um projeto'
python3 tools/peos_engine.py compose --pmu PMU-006 --goal 'criar um design system' --output plano.json
python3 -m unittest discover -s tests -v
python3 tools/library.py validate
```

## Política de conflito

1. Restrições de segurança, autorização e preservação de dados.
2. Requisitos e critérios de aceite explicitamente fornecidos.
3. Contratos canônicos de prompts referenciados.
4. Preferências de apresentação.

As combinações são referências curadas, não concatenação automática do texto dos prompts.

## Limitações e próximos passos

- Classificação por palavras-chave pode errar ou não identificar intenções complexas.
- A validação de gates depende de evidências reais, não de marcadores declarativos.
- Nenhum teste E2E com GitHub, Neon, Auth0 ou Vercel foi realizado.
- Os PMUs são conteúdo editorial proposto, ainda sem homologação humana.
- Não há credenciais, segredos ou serviços pagos exigidos.
