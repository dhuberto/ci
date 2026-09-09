# Início do arquivo test_app.py
# Testes unitários para verificar as rotas da aplicação

from app import app

def test_hello():
    """Testa se a rota raiz retorna a mensagem correta"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, DevOps!"}

def test_healthz():
    """Testa se a rota de health check retorna status 200"""
    client = app.test_client()
    response = client.get('/healthz')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

# Fim do arquivo test_app.py
