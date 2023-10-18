from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.comentarios import Comentarios, ComentariosSchema
from models.usuario import Usuario
ruta_comentarios = Blueprint("ruta_comentarios",__name__)


comentario_schema = ComentariosSchema()
comentarios_schema = ComentariosSchema(many=True)

@ruta_comentarios.route("/comentarios", methods=["GET"])
def comentarios(): 
    comentarios = db.session.query(Comentarios.id , Usuario.nombre, Comentarios.contenido, Comentarios.titulo).join(Comentarios).all()
    comentarios_json = []
    for comentario in comentarios:
        comentario_dict = {'id':comentario[0] , 'usuario': comentario[1], 'contenido': comentario[2], 'titulo': comentario[3]}
        comentarios_json.append(comentario_dict)
    return jsonify(comentarios_json)

@ruta_comentarios.route("/savecomentario", methods=["POST"])
def savecomentario():
    data = request.get_json()
    db.session.add(Comentarios(**data))
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_comentarios.route("/updatecomentario", methods=["PUT"])
def updatecomentario():
    id = request.json['id']
    contenido = request.json ['contenido']
    titulo = request.json ['titulo']
    ncomentario = Comentarios.query.get(id) #Select * from Cliente where id = id
    ncomentario.contenido = contenido
    ncomentario.titulo = titulo
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_comentarios.route("/deletecomentario/<int:id>", methods=["DELETE"])
def deletecliente(id):
    comentarios = Comentarios.query.get(id)
    db.session.delete(comentarios)
    db.session.commit()
    return jsonify(comentario_schema.dump(comentarios))
 
 