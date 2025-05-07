from flask import Blueprint, jsonify, request
from .dados import salvar_usuario, listar_usuarios

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/lista_usuarios', methods=['GET'])
def listar():
    retorno_dados = listar_usuarios()
    return jsonify(retorno_dados)
    # return jsonify([{"id": 1, "nome": "Larissa de Sousa"}])

@usuarios_bp.route('/criar_usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    novo = salvar_usuario(dados)
    return jsonify(novo), 200
    # return jsonify({"messagem": "Usuario Criado", "dados": dados})

