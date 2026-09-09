
---

## 📄 Arquivo: `docs/ci-pipeline.md`

```markdown
# Documentação do Pipeline de CI

## Visão Geral
Pipeline de Integração Contínua usando GitHub Actions. Executa testes e auditoria de segurança em pull requests e pushes na branch `main`.

## Workflows

### CI Pipeline (ci.yml)
**Disparo**: 
- `pull_request` para `main`
- `push` para `main`
- `workflow_dispatch` (manual)

**Job**:
- `test`: Chama o reusable workflow `_reusable-test.yml`

### Reusable Test (_reusable-test.yml)
**Inputs**:
- `python-version`: Lista de versões do Python (JSON)

**Steps**:
1. Checkout do código
2. Setup Python com cache pip
3. Instalação de dependências
4. `pip-audit` (segurança)
5. `pytest` (testes unitários)

## Decisões Técnicas

### Matrix de versões
Testamos em Python 3.10 e 3.11 para garantir compatibilidade com versões recentes.

### Reusable Workflow
Extraímos os steps de teste para um workflow separado para reutilização e manutenção centralizada.

### Permissões Mínimas
Cada job tem permissões explícitas com escopo mínimo (`contents: read`).

## Como rodar localmente

```bash
# Instalar dependências
pip install -r requirements.txt -r requirements-dev.txt

# Rodar testes
pytest test_app.py -v

# Rodar pip-audit
pip-audit -r requirements.txt -r requirements-dev.txt
