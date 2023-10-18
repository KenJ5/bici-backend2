from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.comunidad import comunidad, comunidadSchema

ruta_comunidad = Blueprint("ruta_comunidad",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

comunidad_schema = comunidadSchema()
comunidad_schema = comunidadSchema(many=True)

@ruta_comunidad.route("/comunidad", methods=["GET"])
def comunidad(): 
    resultall = comunidad.query.all()
    result = comunidad_schema.dump(resultall)
    return jsonify(result)

@ruta_comunidad.route("/savecomunidad", methods=["POST"])
def savecomunidad():
    data = request.get_json()
    db.session.add(comunidad(**data))
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_comunidad.route("/updatecomunidad", methods=["PUT"])
def updatecomunidad():
    id = request.json['id']
    nombre = request.json ['nombre']
    ncomunidad = comunidad.query.get(id) 
    ncomunidad.nombre = nombre
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_comunidad.route("/deletecomunidad", methods=["DELETE"])
def deletecomunidad():
    id = request.json.get('id')
    comunidad = comunidad.query.get(id)
    db.session.delete(comunidad)
    db.session.commit()
    return jsonify(comunidad_schema.dump(comunidad))
 
 