from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    retorno_dos_dados = [{"id": 1, "nome": "Ana"}, {"id": 2, "nome": "Julio"}]
    return jsonify(retorno_dos_dados)

@app.route('/usuarios_buscar', methods=['GET'])
def listar_buscar():
    retorno_dos_dados = [{"id": 1, "nome": "Luiz Felipe"}, {"id": 2, "nome": "Mayanne"}]
    return jsonify(retorno_dos_dados)

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    return jsonify({"messagem": "Usuario criado", "dados": dados})

@app.route('/pagina_html')
def index():
    return render_template("index.html", nome="Maria", lista=["maça", "banana", "uva"])

if __name__ == '__main__':
    app.run(debug=True)
