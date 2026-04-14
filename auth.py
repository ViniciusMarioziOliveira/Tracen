import jwt
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, jsonify, current_app


def gerar_token(usuario):
    payload = {
        "usuario": usuario,
        "perfil": "adm",
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    }

    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
    return token


def token_obrigatorio(func):
    @wraps(func)
    def verificar_token(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"erro": "Token ausente. Faça login."}), 401

        partes = auth_header.split()

        if len(partes) != 2 or partes[0] != "Bearer":
            return jsonify({"erro": "Cabeçalho Authorization inválido."}), 401

        token = partes[1]

        try:
            dados_token = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            request.usuario_logado = dados_token

        except jwt.ExpiredSignatureError:
            return jsonify({"erro": "Token expirado."}), 401

        except jwt.InvalidTokenError:
            return jsonify({"erro": "Token inválido."}), 401

        return func(*args, **kwargs)

    return verificar_token