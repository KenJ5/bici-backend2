from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.usuario import Usuario, UsuarioSchema

ruta_usuarios = Blueprint("ruta_usuarios",__name__)
#routes_cliente = Blueprint("routes_usuario", name)

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

@ruta_usuarios.route("/usuarios", methods=["GET"])
def usuarios(): 
    resultall = Usuario.query.all()
    result =usuarios_schema.dump(resultall)
    return jsonify(result)

@ruta_usuarios.route("/saveusuario", methods=["POST"])
def saveusuario():
    data = request.get_json()
    db.session.add(Usuario(**data))
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_usuarios.route("/updateusuario", methods=["PUT"])
def updateusuario():
    id = request.json['id']
    nombre = request.json['nombre']
    email = request.json['email']
    password = request.json['contraseña']
    nusuario = Usuario.query.get(id) #Select * from Cliente where id = id
    nusuario.nombre = nombre
    nusuario.email = email
    nusuario.contraseña = password
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_usuarios.route("/deleteusuario", methods=["DELETE"])
def deleteusuario():

    id = request.json.get('id') 
    if id is None:
        return jsonify({"message": "Se requiere el parámetro 'id' en el cuerpo de la solicitud"}), 400

    user = Usuario.query.get(id)
    if user is None:
        return jsonify({"message": "Usuario no encontrado"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "Usuario eliminado exitosamente"}), 200
