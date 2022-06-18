from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

class usuarios(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(40))
    telefone = db.Column(db.String(20))

    def to_json(self):       
         return {"id": self.id, "nome": self.nome, "email": self.email, "telefone": self.telefone}
     
     # Selecionar Tudo
@app.route("/users", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = usuarios.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]

    return gera_response(200, "usuarios", usuarios_json)

 #Selecionar Individual
@app.route("/users/<id>", methods=["GET"])
def seleciona_usuario(id):
    usuario_objeto = usuarios.query.filter_by(id=id).first()
    usuario_json = usuario_objeto.to_json()

    return gera_response(200, "usuario", usuario_json)




def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run()
