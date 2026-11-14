# Relatório de auditoria histórica 1.0 → 1.1

Resultado produzido pela comparação integral das matrizes e fichas dos documentos originais, com extrator reproduzível.

## Evidência consolidada

| Métrica | Resultado |
|---|---:|
| Prompts na v1.0 | 273 |
| Prompts na v1.1 | 647 |
| IDs originais preservados | 273 |
| IDs adicionados | 374 |
| IDs removidos | 0 |
| Renomeações | 3 |
| Alterações não documentadas em fichas históricas | 0 |

## Renomeações editoriais verificadas

| ID | Anterior | Atual |
|---|---|---|
| `1102` | GitHub Actions | GitHub Actions — Pipeline CI/CD |
| `1506` | Segurança de Banco de Dados | Auditoria de Segurança de Banco de Dados |
| `2009` | GitHub Actions | GitHub Actions — Governança e Automação do Repositório |

## Fontes imutáveis no pacote

- v1.0 SHA-256: `bdeb7674fa633e8e1671d6097ad4faf200a0bc9b9f0d476dc8414a9a450c3121`
- v1.1 SHA-256: `93f23c028a3ac78f51371f879cbbeb8b3f833fc546ff12d7e2914157129148aa`

## Limites

A auditoria verifica estrutura, preservação histórica dos IDs, fichas, textos e títulos; não certifica a correção factual de cada uma das 647 recomendações técnicas nem a atualidade das fontes citadas. O changelog original não integra o ZIP porque não estava disponível como arquivo local no momento da exportação; suas declarações centrais foram confrontadas com v1.0/v1.1.

## Reprodução

```bash
python3 tools/library.py audit
python3 tools/library.py validate
```
