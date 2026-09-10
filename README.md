[![.github/workflows/ci.yml](https://github.com/dhuberto/ci/actions/workflows/ci.yml/badge.svg)](https://github.com/dhuberto/ci/actions/workflows/ci.yml)

```
ci/                                         # Raiz do repositório
│
├── .github/                                # Pasta especial do GitHub
│   ├── CODEOWNERS                          # Define quem revisa os PRs
│   └── workflows/                          # Pasta onde ficam os pipelines
│       ├── ci.yml                          # Pipeline principal (dispara em PR/push)
│       └── _reusable-test.yml              # Workflow reutilizável (chamado pelo ci.yml)
│
├── docs/                                   # Pasta de documentação
│   └── ci-pipeline.md                      # Documentação detalhada do pipeline
│
├── README.md                               # Apresentação do projeto e checklist
├── requirements.txt                        # Dependências de produção
├── requirements-dev.txt                    # Dependências de desenvolvimento (testes, segurança)
├── app.py                                  # Aplicação Flask
└── test_app.py                             # Testes unitários da aplicação
```
# CI/CD - Grupo dhuberto


## Checklist da Atividade 1

- [x] Repositório privado no GitHub
- [x] @HardSource adicionado como collaborator (Read)
- [x] Branch `main` protegida com required status checks
- [x] CODEOWNERS configurado
- [x] `ci.yml` disparando em `pull_request` e `push` para `main`
- [x] Testes automatizados com pytest
- [x] Auditoria de dependências com pip-audit
- [x] Matrix de Python (3.10 e 3.11)
- [x] Cache de dependências (pip)
- [x] Reusable workflow (`_reusable-test.yml`)
- [x] `permissions:` explícito e mínimo
- [x] Badge do pipeline no README
- [x] Documentação em `docs/ci-pipeline.md`
- [x] `workflow_dispatch` para execução manual

## Como rodar localmente


# Clonar para a maquina local o repositorio
```bash
git clone https://github.com/dhuberto/ci.git
cd ci
```

# Criar o ambiente virtual
```bash
python3 -m venv venv
```

# Ativar o ambiente virtual
# No Linux/Mac:
```bash
source venv/bin/activate
```

# Instalar as dependências
```bash
pip install -r requirements.txt -r requirements-dev.txt
```
# Rodar pip-audit verificaçaõ manual de seguraça
```bash
pip-audit -r requirements.txt -r requirements-dev.txt
```

# Iniciar o servidor
```bash
python app.py -v
```

# Testar rota raiz
```bash
http://localhost:5000/
```
# Deve retornar: {"message":"Hello, DevOps!"}

# Testar health check
```bash
http://localhost:5000/healthz
```

# Deve retornar: {"status":"healthy"}
