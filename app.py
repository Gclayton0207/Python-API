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

# Cadastrar
@app.route("/add_user", methods=["POST"])
def cria_usuario():
    body = request.get_json()

    try:
        usuario = usuarios(nome=body["nome"], email= body["email"], telefone= body["telefone"])
        db.session.add(usuario)
        db.session.commit()
        return gera_response(201, "usuario", usuario.to_json(), "Usuario cadastrado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {}, "Erro ao cadastrar")

# Editar
@app.route("/edit_user/<id>", methods=["PUT"])
def atualiza_usuario(id):
    usuario_objeto = usuarios.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('nome' in body):
            usuario_objeto.nome = body['nome']
        if('email' in body):
            usuario_objeto.email = body['email']
        if('telefone' in body):
            usuario_objeto.telefone = body['telefone']
        
        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {}, "Erro ao atualizar")
    
    
    

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run()
