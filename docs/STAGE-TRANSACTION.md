# Versionamento seguro da biblioteca — pré-flight PEOS

Este procedimento cobre **futuras versões do catálogo**. Não altera os snapshots da baseline `v2.1.0` durante a instalação da funcionalidade.

## Problema original

`tools/library.py stage` escrevia contratos, manifesto, snapshots, ledger, índices e compilados em sequência. Se uma etapa falhasse depois da primeira gravação, arquivos de saída poderiam ficar divergentes.

## Solução

A operação `stage` passa a:

1. Obter um lock exclusivo `.peos-stage.lock` no checkout.
2. Copiar a árvore de trabalho (inclusive modificações locais ainda não commitadas) para uma pasta temporária, excluindo `.git`, dependências e resultados de teste.
3. Executar a lógica de versionamento **somente na cópia**, recalculando o índice do Hub e validando a biblioteca no ambiente temporário.
4. Comparar o SHA-256 de entradas relevantes e saídas geradas para recusar publicação se arquivos tiverem sido alterados durante a preparação.
5. Promover somente arquivos gerados com mudança, usando substituição atômica **por arquivo** e tentativa de rollback dos arquivos já gravados em caso de erro normal de I/O.
6. Limpar o lock em saída normal ou erro capturado.

### Operação

```bash
# Trabalhar em uma branch específica; manter alterações dos textos de prompt sob controle de versão.
python3 tools/library.py stage --version 2.1.1 --reason "Motivo verificável"
python3 tools/library.py validate
python3 tools/build_hub_index.py --check
python3 -m unittest discover -s tests -v
git diff --check
git status --short
```

**Não executar** esse exemplo diretamente na `main`. Substituir `2.1.1` pela próxima versão realmente deliberada e executar apenas após alterações editoriais aprovadas.

## Garantias e limites

- Falha na preparação não modifica as saídas da árvore de trabalho, exceto o lock transitório.
- Durante a promoção, falhas comuns acionam rollback *best-effort* para os arquivos já substituídos.
- **Não é uma transação de filesystem inteiramente atômica**: perda de energia, término abrupto do processo, falha do disco e rollback mal sucedido podem deixar parte dos arquivos atualizados.
- Em incidentes, interromper novos stages, inspecionar o lock e recuperar os artefatos a partir do Git e dos snapshots antes de continuar. Não apagar automaticamente um lock órfão sem verificar o processo anterior.
- A operação preserva alterações locais em prompts, mas não cria commit automaticamente. Cada release de biblioteca continua sujeito a PR, checks e revisão de conteúdo.
- Não executar scripts de fontes desconhecidas com esta preparação: a cópia temporária é **isolamento de escrita**, não sandbox de código confiável.

## Ensaios automatizados

`tests/test_stage_transaction.py` cobre um versionamento futuro em diretório descartável, a rejeição de versão inválida e a reversão simulada quando uma segunda gravação falha.

## Publicação e direitos

A capacidade de gerar snapshot interno **não autoriza distribuição pública**. O release permanece bloqueado pela [issue #2](https://github.com/alexoaraujo/peos-knowledge-hub/issues/2), avaliação manual [#8](https://github.com/alexoaraujo/peos-knowledge-hub/issues/8) e curadoria editorial [#17](https://github.com/alexoaraujo/peos-knowledge-hub/issues/17). Gate de release: `tools/release_preflight.py --require-evidence` somente com dossiê externo real e revisão humana.
