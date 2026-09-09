ci_/                                 # Raiz do repositório
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
