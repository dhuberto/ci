# ============================================================
# APLICAÇÃO FLASK
# ============================================================
# Uma API simples com duas rotas: raiz e health check.
# ============================================================

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, DevOps!"})

@app.route('/healthz')
def healthz():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
