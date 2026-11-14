# Release notes — Inclusão da coleção Programação e Design

**Tipo:** incorporação complementar estruturada; **não** altera a versão editorial do conteúdo canônico 1.1.0.

## Inclusões

- 128 itens locais `BPD-001` a `BPD-128` em 30 seções temáticas.
- Cópia integral da fonte original sob `originais/` e excertos por ID com SHA-256 e localização de origem.
- Manifesto versionado `colecoes/programacao-design/manifest.json` e snapshot `releases/v1.0.0.json`.
- Índice por seção, lista de candidatos a lacunas UX/UI e arquivo CSV unificado com 775 entradas.
- Documento Markdown completo que combina 647 fichas canônicas e 128 itens complementares.
- Validação da coleção incorporada ao comando `python3 tools/library.py validate`, aos testes e ao workflow GitHub Actions.

## Invariantes preservados

- 273 IDs da v1.0 preservados na v1.1; nenhum ID canônico removido, renumerado ou reutilizado.
- Os 647 arquivos de prompts canônicos, a taxonomia, os hashes e os snapshots históricos não foram alterados por esta incorporação.
- Nenhum candidato a lacuna de UX/UI foi promovido automaticamente à taxonomia ou recebeu um ID permanente sem revisão.

## Revisão ainda necessária

- Confirmar semanticamente os links temáticos entre os 128 itens locais e seus possíveis correspondentes canônicos.
- Avaliar 11 candidatos de UX/UI antes de criar novas finalidades, caso seja pertinente.
- Configurar a execução real do workflow em um repositório GitHub com branch protegida; o pacote contém a automação, mas não a implantação externa.

## Verificações executadas localmente

```bash
python3 tools/library.py audit
python3 tools/collections_integration.py check
python3 tools/library.py index --check
python3 tools/library.py compile --check
python3 tools/library.py validate
python3 -m unittest discover -s tests -q
```
