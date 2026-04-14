from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
from auth import token_obrigatorio, gerar_token
from flask_cors import CORS
import os
from dotenv import load_dotenv
import json
from flasgger import Swagger

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Versão do openAPI
app.config['SWAGGER'] = {
    'openapi' : '3.0.0'
}

# Chamar o open API para o código
swagger = Swagger(app, template_file='openapi.yaml')

CORS(app, origins="*")

ADM_USUARIO = os.getenv("ADM_USUARIO")
ADM_SENHA = os.getenv("ADM_SENHA")

# Firebase
if os.getenv("VERCEL"):
    cred = credentials.Certificate(json.loads(os.getenv("FIREBASE_CREDENTIALS")))
else:
    cred = credentials.Certificate("firebase.json")

firebase_admin.initialize_app(cred)
db = firestore.client()


# =========================
# ROTA INICIAL
# =========================
@app.route("/", methods=["GET"])
def root():
    return jsonify({"api": "Academia Tracen", "versao": "1.0", "autor": "Vini do Back"})


# =========================
# LOGIN
# =========================
@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()

    if not dados:
        return jsonify({"error": "Envie os dados!"}), 400

    if dados.get("usuario") == ADM_USUARIO and dados.get("senha") == ADM_SENHA:
        token = gerar_token(dados["usuario"])
        return jsonify({"token": token}), 200

    return jsonify({"error": "Credenciais inválidas"}), 401


# =========================
# CATRACA 🔥
# =========================
@app.route("/catraca", methods=["POST"])
def catraca():
    dados = request.get_json()

    if not dados or "cpf" not in dados:
        return jsonify({"error": "CPF é obrigatório"}), 400

    cpf = dados["cpf"]

    doc = db.collection("alunos").document(cpf).get()

    if not doc.exists:
        return jsonify({"status": "erro", "msg": "Aluno não encontrado"}), 404

    aluno = doc.to_dict()

    if aluno["bloqueado"] or aluno["status"] != "ativo":
        return jsonify({
            "status": "bloqueado",
            "msg": "Procure a secretaria da academia"
        }), 403

    return jsonify({
        "status": "liberado",
        "msg": "Acesso liberado"
    }), 200


# =========================
# GET TODOS ALUNOS
# =========================
@app.route("/alunos", methods=["GET"])
def get_alunos():
    lista = db.collection("alunos").stream()
    alunos = []

    for doc in lista:
        alunos.append(doc.to_dict())

    return jsonify(alunos), 200


# =========================
# GET ALUNO POR CPF
# =========================
@app.route("/alunos/<cpf>", methods=["GET"])
def get_aluno(cpf):
    doc = db.collection("alunos").document(cpf).get()

    if not doc.exists:
        return jsonify({"error": "Aluno não encontrado"}), 404

    return jsonify(doc.to_dict()), 200


# =========================
# POST (CRIAR ALUNO)
# =========================
@app.route("/alunos", methods=["POST"])
@token_obrigatorio
def criar_aluno():
    dados = request.get_json()

    if not dados or "cpf" not in dados or "nome" not in dados:
        return jsonify({"error": "Dados incompletos"}), 400

    cpf = dados["cpf"]

    db.collection("alunos").document(cpf).set({
        "nome": dados["nome"],
        "cpf": cpf,
        "status": dados.get("status", "ativo"),
        "bloqueado": dados.get("bloqueado", False)
    })

    return jsonify({"message": "Aluno criado com sucesso"}), 201


# =========================
# PUT (ATUALIZA TOTAL)
# =========================
@app.route("/alunos/<cpf>", methods=["PUT"])
@token_obrigatorio
def atualizar_aluno(cpf):
    dados = request.get_json()

    if not dados or "nome" not in dados or "status" not in dados or "bloqueado" not in dados:
        return jsonify({"error": "Dados incompletos"}), 400

    doc = db.collection("alunos").document(cpf)

    if not doc.get().exists:
        return jsonify({"error": "Aluno não encontrado"}), 404

    doc.set({
        "nome": dados["nome"],
        "cpf": cpf,
        "status": dados["status"],
        "bloqueado": dados["bloqueado"]
    })

    return jsonify({"message": "Aluno atualizado"}), 200


# =========================
# PATCH (PARCIAL)
# =========================
@app.route("/alunos/<cpf>", methods=["PATCH"])
@token_obrigatorio
def atualizar_parcial(cpf):
    dados = request.get_json()

    if not dados:
        return jsonify({"error": "Nada para atualizar"}), 400

    doc_ref = db.collection("alunos").document(cpf)

    if not doc_ref.get().exists:
        return jsonify({"error": "Aluno não encontrado"}), 404

    doc_ref.update(dados)

    return jsonify({"message": "Atualizado com sucesso"}), 200


# =========================
# DELETE
# =========================
@app.route("/alunos/<cpf>", methods=["DELETE"])
@token_obrigatorio
def deletar_aluno(cpf):
    doc = db.collection("alunos").document(cpf)

    if not doc.get().exists:
        return jsonify({"error": "Aluno não encontrado"}), 404

    doc.delete()

    return jsonify({"message": "Aluno deletado"}), 200


# =========================
# ERROS
# =========================
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Rota não encontrada"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Erro interno"}), 500


if __name__ == "__main__":
    app.run(debug=True)