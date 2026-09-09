# Início do arquivo app.py
# Aplicação Flask com duas rotas: raiz e health check

from flask import Flask, jsonify

# Cria a aplicação Flask
app = Flask(__name__)

# Rota principal - retorna uma mensagem de boas-vindas
@app.route('/')
def hello():
    return jsonify({"message": "Hello, DevOps!"})

# Rota de health check - usada para verificar se a aplicação está viva
@app.route('/healthz')
def healthz():
    return jsonify({"status": "healthy"}), 200

# Só executa o servidor se o arquivo for rodado diretamente (não importado)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Fim do arquivo app.py
