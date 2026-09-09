# Documentação do Pipeline de CI

## Visão Geral

Pipeline de Integração Contínua (CI) configurado no GitHub Actions para o repositório `cicd-eedth`. O objetivo é garantir a qualidade e segurança do código antes que ele seja mesclado na branch `main`.

## Workflows

### 1. CI Pipeline (`.github/workflows/ci.yml`)

**Disparo**:
- `pull_request` para a branch `main`
- `push` para a branch `main`
- `workflow_dispatch` (manual, pela aba Actions)

**Jobs**:

| Job | Descrição | Dependências |
|-----|-----------|--------------|
| `test` | Chama o reusable workflow `_reusable-test.yml` para executar testes e auditoria de segurança. | Nenhuma. |
| `security-scan` | Executa o scanner de vulnerabilidades Trivy no código e dependências. Requer aprovação manual via environment `production`. | `test` |
| `notify` | Envia notificação com o status do pipeline para um webhook (Slack/Discord). Roda sempre, inclusive em falhas. | `test`, `security-scan` |

### 2. Reusable Test (`.github/workflows/_reusable-test.yml`)

**Disparo**: `workflow_call` (chamado pelo `ci.yml`).

**Inputs**:
- `python-version` (string, obrigatório): Lista de versões do Python em formato JSON. Padrão: `["3.10", "3.11"]`.

**Secrets**:
- `NOTIFY_WEBHOOK_URL` (opcional): URL do webhook para notificações.

**Jobs**:

#### Job: `test`
Executa testes em múltiplas versões do Python.

| Step | Ação | Descrição |
|------|------|-----------|
| 1 | `actions/checkout` | Baixa o código do repositório. |
| 2 | `actions/setup-python` | Configura a versão do Python com cache do pip. |
| 3 | `run: pip install` | Instala dependências de produção e desenvolvimento. |
| 4 | `run: pip-audit` | Audita dependências em busca de CVEs (falha o job se encontrar). |
| 5 | `run: pytest` | Executa os testes unitários. |
| 6 | `actions/upload-artifact` | Salva o relatório de testes como artefato. |

## Decisões Técnicas

### 1. Matrix de Versões do Python
Optamos por testar em Python 3.10 e 3.11 para garantir compatibilidade com versões recentes e estáveis, sem sobrecarregar o pipeline com muitas versões.

### 2. Reusable Workflow
A lógica de testes foi extraída para um workflow reutilizável (`_reusable-test.yml`) para:
- DRY (Don't Repeat Yourself): Evita duplicação de código YAML.
- Manutenibilidade: Mudanças nos testes são feitas em um único lugar.
- Reutilização: Pode ser chamada por outros workflows no futuro (ex: CD).

### 3. Environment com Aprovação
O job `security-scan` utiliza o environment `production` com required reviewers. Isso adiciona uma camada extra de segurança, exigindo aprovação manual antes de executar escaneamentos que podem expor dados sensíveis ou consumir mais recursos.

### 4. Segurança do Pipeline

#### Permissões Mínimas
Cada job declara permissões explícitas com escopo mínimo usando o bloco `permissions:`. Por exemplo, o job `test` tem apenas `contents: read` e `checks: write`.

#### Pinning de Actions
Todas as actions de terceiros são referenciadas por SHA de commit (imutável) em vez de tags mutáveis como `@v4`. Isso evita que mudanças inesperadas na action comprometam o pipeline.

| Action | SHA (v4.2.2) |
|--------|--------------|
| `actions/checkout` | `11bd7190...` |
| `actions/setup-python` | `b93645a1...` |
| `aquasecurity/trivy-action` | `f42b6a2f...` |

#### Segredos
Nenhum segredo (webhook URLs, tokens) está commitado no repositório. Todos os dados sensíveis estão configurados como secrets no GitHub (Settings -> Secrets and variables -> Actions).

## Como Rodar Localmente

Para testar a aplicação e os checks localmente:

```bash
# Instalar dependências (produção + desenvolvimento)
pip install -r requirements.txt -r requirements-dev.txt

# Rodar os testes unitários
pytest test_app.py -v

# Rodar a auditoria de dependências (pip-audit)
pip-audit -r requirements.txt -r requirements-dev.txt

# Rodar o Trivy (requer instalação local: https://aquasecurity.github.io/trivy)
trivy fs . --severity MEDIUM,HIGH,CRITICAL
