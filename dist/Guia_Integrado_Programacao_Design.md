# Guia de integração — Biblioteca Mestre e Programação e Design

## Escopo

- Biblioteca Mestre: 659 fichas e IDs canônicos, versão 2.1.0; baseline da coleção: 1.1.0.
- Coleção Programação e Design: 128 itens locais, 30 seções.
- Inventário combinado: 787 entradas navegáveis; NÃO representam necessariamente finalidades distintas.
- Candidatos a lacunas de UX/UI: 11 (em revisão).

## Navegação

- [Índice da coleção](../colecoes/programacao-design/INDEX.md)
- [Candidatos a novos prompts de UX](../colecoes/programacao-design/CANDIDATOS_A_NOVOS_PROMPTS.md)
- [Catálogo integrado CSV](Catalogo_Integrado.csv)
- [Biblioteca integrada em um único Markdown](Biblioteca_Mestre_TI_Integrada_Completa.md)
- [Documento original](../originais/Biblioteca-de-Prompts-para-Programação-e-Design.txt)

## Governança de IDs

IDs BPD são locais, independentes dos quatro dígitos permanentes da Biblioteca Mestre.
Não considerar que uma associação temática indica duplicata ou equivalência exata.

A coleção preserva a baseline original; a curadoria 2.0 de UX é registrada separadamente em `catalog/ux_curadoria_v2.json`.

## Validação

Execute `python3 tools/collections_integration.py check` e `python3 tools/library.py validate`.
