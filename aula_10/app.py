from flask import Flask
from flask_restful import Api
from blueprints.usuarios_blueprint import usuarios_bp

app = Flask(__name__)
api = Api(app)

app.register_blueprint(usuarios_bp, url_prefix="/api")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5009, debug=True)
