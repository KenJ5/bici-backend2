from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.sistema_alerta import Alerta, AlertaSchema

ruta_alerta = Blueprint("ruta_alerta",__name__)


alerta_schema = AlertaSchema()
alertas_schema = AlertaSchema(many=True)

@ruta_alerta.route("/alertas", methods=["GET"])
def alertas(): 
    resultall = Alerta.query.all()
    result = alertas_schema.dump(resultall)
    return jsonify(result)

@ruta_alerta.route("/savealerta", methods=["POST"])
def savealerta():
    data = request.get_json()
    db.session.add(Alerta(**data))
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_alerta.route("/updatealerta", methods=["PUT"])
def updatealerta():
    id = request.json['id']
    tipo = request.json['tipo']
    nalerta = Alerta.query.get(id) 
    nalerta.tipo = tipo
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_alerta.route("/deletealerta", methods=["DELETE"])
def deletealerta():
    id = request.json.get('id') 
    alerta = Alerta.query.get(id)
    db.session.delete(alerta)
    db.session.commit()
    return jsonify(alerta_schema.dump(alerta))
 
 