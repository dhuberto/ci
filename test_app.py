# ============================================================
# TESTES UNITÁRIOS
# ============================================================
# Verificam se as rotas da aplicação respondem corretamente.
# ============================================================

from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, DevOps!"}

def test_healthz():
    client = app.test_client()
    response = client.get('/healthz')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
