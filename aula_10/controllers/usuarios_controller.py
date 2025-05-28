from flask import Flask, request, jsonify
from flask_restful import Api, reqparse
from werkzeug.security import generate_password_hash
from db.conexao import conexao_banco
import re

argumentos = reqparse.RequestParser()
argumentos.add_argument('email', type=str)
argumentos.add_argument('password', type=str)

def index():
    retorno = [{"id": 1, "nome": "Julio"}, {"id": 2, "nome": "Luiz"}]
    return jsonify({"mensagem": "Bem vindo a api", "status_code": 201, "dados": retorno})

def listar_usuarios():
    try:
        conn = conexao_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT ID, EMAIL FROM USERS")
        usuarios = cursor.fetchall()
        colunas = [desc[0] for desc in cursor.description]
        resultado = [dict(zip(colunas, row)) for row in usuarios]
        return jsonify(resultado)
    except Exception as e:
        conn.rollback()
        print("Erro ao buscar os usuarios:", e)
        return jsonify({"erro": f"Erro ao buscar usuarios{e}"}), 500
    finally:
        cursor.close()
        conn.close()

def registrar():
    try:
        dados = argumentos.parse_args()
        conn = conexao_banco()
        cursor = conn.cursor()
        
        if request.method == 'POST' and 'email' in dados and 'password' in dados:
        
            email = dados['email']
            password = dados['password']
            
            _hast_password = generate_password_hash(password)
            print("Gerou hash da senha", _hast_password)
            
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            conta_usuario = cursor.fetchall()
            if conta_usuario:
                return jsonify("Essa conta ja existe"), 303
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                return jsonify("Email invalido"), 303
            elif not password or not email:
                return jsonify("Por favor, verifique todos os campos"), 303
            else:
                cursor.execute("INSERT INTO users(email, password) values(%s, %s)", (email, password))
                conn.commit()
                return jsonify("Usuario inserido com sucesso"), 200
        else:
            return jsonify("A requisicao nao e um metodo POST!"), 303 
    except Exception as e:
        conn.rollback()
        print("Erro ao inserir o usuario:", e)
        return jsonify({"erro": f"Erro ao inserir o usuario{e}"}), 500
    finally:
        cursor.close()
        conn.close()

def deleta_usuario(user_id):
    try:
        conn = conexao_banco()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM USERS WHERE id = %s", (user_id, ))
        conn.commit()
        return jsonify({"message": "Usuario removido com sucesso"}), 200
    except Exception as e:
        conn.rollback()
        print("Erro ao deletar o usuario:", e)
        return jsonify({"erro": f"Erro ao deletar o usuario{e}"}), 500
    finally:
        cursor.close()
        conn.close()
        
def atualiza_usuario(user_id):
    try:
        conn = conexao_banco()
        cursor = conn.cursor()
        data = request.get_json()
        email = data.get("email")
        
        cursor.execute("UPDATE USERS SET email = %s WHERE id = %s", (email, user_id))
        conn.commit()
        return jsonify({"messagem": "Usuario atualizado com sucesso"})
        
    except Exception as e:
        conn.rollback()
        print("Erro ao atualizar o usuario:", e)
        return jsonify({"erro": f"Erro ao atualizar o usuario{e}"}), 500
    finally:
        cursor.close()
        conn.close()

