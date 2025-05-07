from flask import Flask
from models.usuario import usuarios_bp

app = Flask(__name__)
app.register_blueprint(usuarios_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)