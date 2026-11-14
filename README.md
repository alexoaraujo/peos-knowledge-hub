# PEOS Knowledge Hub

**Prompt Engineering Operating System — Knowledge Hub**

Plataforma open-source planejada de engenharia de prompts para TI, com biblioteca versionada, taxonomia, governança, validação automatizada, workflows e agentes especializados.

## Estado de publicação

**Bootstrap inicial do repositório.** O pacote integral PEOS Knowledge Hub v0.1.0 foi preparado e validado localmente a partir dos três ZIPs fornecidos. A importação completa ainda **não foi publicada neste repositório**.

A baseline preparada é a Biblioteca Mestre TI **v2.1.0**, com **659 prompts canônicos**, **128 BPD**, **10 PMUs (ainda PROPOSED)** e **10 workflows de planejamento**: 797 entradas textuais em três namespaces, com workflows separados.

O projeto local inclui:
- Catálogo e taxonomia com IDs imutáveis e hashes SHA-256;
- CLI Python sem dependências obrigatórias pagas;
- Portal de pesquisa estático;
- 10 perfis de agentes em modo **PLAN_ONLY**, sem credenciais de execução;
- Documentação técnica, governança, proveniência e roadmap P0/P1/P2;
- GitHub Actions para integridade, testes e índices reproduzíveis;
- **37 testes locais aprovados** (não equivalem a CI remoto).

## Publicação da versão completa

O conteúdo completo é distribuído como `PEOS_Knowledge_Hub_v0.1.0.zip` no resultado da análise no ChatGPT. Descompacte o pacote, copie seus arquivos para o clone desta pasta, execute os testes e envie uma Pull Request. Não sobrescreva a branch `main` à força.

```bash
python3 -m unittest discover -s tests -v
python3 tools/library.py validate
python3 tools/peos_engine.py validate
python3 tools/build_hub_index.py --check
```

**Licenciamento:** os três arquivos originais não continham LICENSE. A titularidade e o licenciamento do conteúdo devem ser revisados antes de atribuir uma licença aberta ao conjunto inteiro.

**Segurança:** o motor original gera planos, não executa ações externas; gates permanecem pendentes sem evidência.

**Projeto:** `alexoaraujo/peos-knowledge-hub`
