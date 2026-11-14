# Runbook — falhas de integridade no Windows / Git Bash

## Diagnóstico PEOS PMU-003 + PMU-007 + PMU-009

**Causa ainda não comprovada:** os erros `test_duplicate_id_is_blocked`, `test_manifest_integrity`, `test_index_determinism` e `test_stage_with_reason_creates_versioned_snapshot` foram observados em uma cópia Windows. A mesma baseline do ZIP completa passou nos 37 testes em Linux. Não altere hashes/snapshots para acomodar falhas sem explicação.

## Pré-condições

- Python 3 funcional (`python --version`).
- Checkout em `main` ou branch derivada, sem arquivos faltantes.
- `git status --short` conferido.
- `catalog/manifest.json`, `originais/`, `prompts/`, `releases/` presentes.

## Coleta de evidências (Git Bash)

```bash
git fetch origin
git rev-parse HEAD
git status --short
git ls-files --eol catalog/manifest.json prompts/0700-0799/0711.md tools/library.py
python --version
python tools/library.py validate
python tools/library.py index --check
python tools/library.py compile --check
python -m unittest discover -s tests -p 'test_library.py' -v > peos-test-errors.log 2>&1
cat peos-test-errors.log
```

## Matriz de decisão

| Evidência | Ação |
| --- | --- |
| Arquivos ausentes em `originais/` ou `releases/` | Reimportar do ZIP verificado, sem alterar snapshots |
| Diferença de hash e CRLF no arquivo | Verificar `.gitattributes`, `git ls-files --eol` e histórico; não re-hashear para ocultar a mudança |
| Apenas Windows falha | Consultar job `Canonical integrity (windows-latest)` e comparar com Ubuntu no mesmo SHA |
| Duplicated-ID teste retorna outro erro | Investigar primeiro erro de validação, evitando tratar sintoma como causa |
| Integridade passa mas snapshot falha | Inspecionar stderr do subcomando stage e permissões no diretório temporário |
| Qualquer gate sem evidência | `BLOCKED`: não gerar release ou mesclar alterações corretivas sem revisão |

## Gates obrigatórios

- **G1**: suíte completa `37/37` aprovada em Linux e Windows no mesmo SHA
- **G2**: manifesto, releases, índices e contratos sem divergências
- **G3**: revisão de licença e redistribuição das fontes (issue #2)
- **G4**: aprovação independente do PR e rastreabilidade da evidência

Nenhuma validação local substitui execução no runner GitHub. Os prompts permanecem `PLAN_ONLY` e não fornecem autorização para mudanças em Production.
