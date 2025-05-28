from flask import Blueprint
from controllers import usuarios_controller

usuarios_bp = Blueprint("usuarios_bp", __name__)

usuarios_bp.route("/", methods=["GET"])(usuarios_controller.index)
usuarios_bp.route("/lista_usuarios", methods=["GET"])(usuarios_controller.listar_usuarios)
usuarios_bp.route("/criar_usuarios", methods=["POST"])(usuarios_controller.registrar)
usuarios_bp.route("/deletar_usuarios/<int:user_id>", methods=["DELETE"])(usuarios_controller.deleta_usuario)
usuarios_bp.route("/atualizar_usuarios/<int:user_id>", methods=["PUT"])(usuarios_controller.atualiza_usuario)
