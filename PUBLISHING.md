# Publicação controlada no GitHub

Destino: `https://github.com/alexoaraujo/peos-knowledge-hub`.

O repositório remoto recebeu um commit bootstrap de documentação. O ZIP integral deste pacote é a entrega técnica. Execute as etapas de publicação sem `--force`, preservando histórico e revisão.

## Terminal Unix / Git Bash

```bash
git clone https://github.com/alexoaraujo/peos-knowledge-hub.git
unzip PEOS_Knowledge_Hub_v0.1.0.zip -d peos-import
cp -a peos-import/peos-knowledge-hub/. peos-knowledge-hub/
cd peos-knowledge-hub
python3 -m unittest discover -s tests -v
python3 tools/library.py validate
python3 tools/peos_engine.py validate
python3 tools/build_hub_index.py --check
git switch -c feat/peos-knowledge-hub-v0.1
git add -A
git commit -m "feat: import PEOS Knowledge Hub baseline v2.1 and validated MVP"
git push -u origin feat/peos-knowledge-hub-v0.1
```

Depois abra uma Pull Request para `main`, revise licenciamento e evidências de CI, confirme que o diff não inclui segredos e integre após os gates aprovados. O ZIP inclui arquivos ocultos `.github` e `.gitignore`.

## Windows PowerShell

```powershell
git clone https://github.com/alexoaraujo/peos-knowledge-hub.git
Expand-Archive -Path .\PEOS_Knowledge_Hub_v0.1.0.zip -DestinationPath .\peos-import -Force
Copy-Item -Path .\peos-import\peos-knowledge-hub\* -Destination .\peos-knowledge-hub\ -Recurse -Force
Copy-Item -Path .\peos-import\peos-knowledge-hub\.github -Destination .\peos-knowledge-hub\ -Recurse -Force
Copy-Item -Path .\peos-import\peos-knowledge-hub\.gitignore -Destination .\peos-knowledge-hub\ -Force
cd peos-knowledge-hub
python -m unittest discover -s tests -v
python tools/library.py validate
python tools/peos_engine.py validate
python tools/build_hub_index.py --check
git switch -c feat/peos-knowledge-hub-v0.1
git add -A
git commit -m "feat: import PEOS Knowledge Hub baseline v2.1 and validated MVP"
git push -u origin feat/peos-knowledge-hub-v0.1
```

Não inserir nenhum valor de segredo em variáveis, URLs ou logs. Não executar scripts da pasta `originais/` como comandos. Não declarar CI remoto aprovado antes de verificar o SHA efetivamente publicado.
