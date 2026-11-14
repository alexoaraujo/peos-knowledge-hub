# Release Notes — Biblioteca Mestre TI v2.1.0

## Alterações
- Mantidos 659 prompts canônicos com os mesmos IDs, hashes e categorias da v2.0.
- Mantida a coleção Programação e Design com 128 itens BPD.
- Adicionados 10 PMUs com prompts completos, hashes e manifesto dedicado.
- Adicionados 10 workflows versionados, com seis etapas cada e gates de evidência.
- Criado motor de composição determinístico, em Python padrão, que retorna plano JSON e não executa mutações.
- Criados testes para roteamento, preservação de hashes, referências e ausência de execução externa.
- Atualizados índices, compilado canônico, documentos e GitHub Actions.

## Verificações locais
- `python3 tools/library.py audit`: PASS.
- `python3 tools/library.py validate`: PASS.
- `python3 tools/peos_engine.py validate`: PASS.
- `python3 -m unittest discover -s tests -v`: 29 testes PASS.

## Limites
- PMUs e workflows são propostas editoriais, não homologação humana.
- O roteador usa palavras-chave e pode escolher especialidade inadequada em pedidos ambíguos.
- A CI não foi executada em GitHub remoto; testes de integrações externas não foram realizados.
- Não foi feita implantação no repositório GitHub.
