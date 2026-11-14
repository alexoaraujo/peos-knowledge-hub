# Coleção Programação e Design — BPD

A coleção preserva os **128 prompts** do texto `Biblioteca-de-Prompts-para-Programação-e-Design.txt` em **30 seções**.

## Identidade e integridade

- `BPD-001` a `BPD-128` são **IDs locais** da coleção e não se confundem com `0001` a `9999` do catálogo mestre.
- O arquivo original é guardado sem reescrita em `originais/`. A cópia se encontra dentro do pacote distribuído.
- Cada excerto preserva o texto original do prompt, removendo apenas os separadores entre seções. O arquivo original integral permanece como referência definitiva.
- `manifest.json` identifica localização no original, SHA-256 do excerto, seção, título, categorias propostas e prompts canônicos relacionados.
- `releases/v1.0.0.json` é um snapshot imutável da importação inicial.
- `coverage=potential_gap` significa **hipótese para análise editorial**, não ausência comprovada nem aprovação automática de novo ID.
- `coverage=complementary` significa complemento ou semelhança temática; **não equivale a duplicidade semântica**.

## Consulta

- [Índice completo por seção](INDEX.md)
- [Candidatos à expansão de UX/UI](CANDIDATOS_A_NOVOS_PROMPTS.md)
- [Manifesto da coleção](manifest.json)

## Gates

```bash
python3 tools/collections_integration.py check
python3 tools/library.py validate
python3 -m unittest discover -s tests -v
```

Não edite um arquivo `BPD-*.md` sem versionar a fonte e registrar uma mudança de versão. O comando de importação recusa sobrescrever a coleção já existente; re-importar com fonte diferente requer nova migração aprovada.
