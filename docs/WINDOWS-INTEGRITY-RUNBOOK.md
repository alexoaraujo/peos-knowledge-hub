# Runbook — falhas de integridade no Windows / Git Bash

## Diagnóstico PEOS PMU-003 + PMU-007 + PMU-009

**Causa-raiz verificada no GitHub Actions:** conversão CRLF durante checkout Windows, caminhos relativos formatados com `\\` em vez de `/`, codificação implícita de arquivo em teste e console/subprocessos sem UTF-8 explícito. Corrigidos com `.gitattributes`, `Path.as_posix()`, leitura/gravação UTF-8 e `PYTHONIOENCODING=utf-8`. Os testes passaram em Windows e Ubuntu no commit `6daeb46a0d05028b2f0d6b0d54bcbb51f0974f5c` ([execução](https://github.com/alexoaraujo/peos-knowledge-hub/actions/runs/43668730991)). Não alterar hashes/snapshots para acomodar falhas sem explicação.

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
python -m unittest discover -s tests -v > peos-test-errors.log 2>&1
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

- **G1**: suíte completa de pelo menos `41/41` testes aprovada em Linux e Windows no mesmo SHA
- **G2**: manifesto, releases, índices e contratos sem divergências
- **G3**: revisão de licença e redistribuição das fontes (issue #2)
- **G4**: aprovação independente do PR e rastreabilidade da evidência

Nenhuma validação local substitui execução no runner GitHub. Os prompts permanecem `PLAN_ONLY` e não fornecem autorização para mudanças em Production.

## Evidência final e controles de saída

- [ ] Registrar novo SHA exato após qualquer alteração adicional e verificar Windows + Ubuntu nesse SHA
- [ ] Confirmar que a saída de `git diff --exit-code` permanece limpa após os checks
- [ ] Obter revisão formal de colaborador elegível diferente do autor antes de merge
- [ ] Não declarar a issue #2 de licenciamento concluída por causa desta correção técnica

A execução cruzada que comprovou a correção possui 41 testes PASS em cada sistema. O arquivo `peos-test-errors.log` é diagnóstico local e **não deve ser commitado**.
