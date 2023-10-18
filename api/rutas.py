from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.rutas import Rutas, RutasSchema

ruta_rutas = Blueprint("ruta_rutas",__name__)
#routes_cliente = Blueprint("routes_cliente", __name__)

ruta_schema = RutasSchema()
rutas_schema = RutasSchema(many=True)

@ruta_rutas.route("/rutas", methods=["GET"])
def rutas(): 
    resultall = Rutas.query.all()
    result = rutas_schema.dump(resultall)
    return jsonify(result)

@ruta_rutas.route("/saveruta", methods=["POST"])
def saveruta():
    data = request.get_json()
    db.session.add(Rutas(**data))
    db.session.commit()
    return "Datos guardados con exitos"

@ruta_rutas.route("/updateruta", methods=["PUT"])
def updateruta():
    id = request.json['id']
    punto_a = request.json['punto_a']
    punto_b = request.json['punto_b']
    nruta = Rutas.query.get(id) 
    nruta.punto_a = punto_a
    nruta.punto_b = punto_b
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_rutas.route("/deleteruta/<int:id>", methods=["DELETE"])
def deletecliente(id): 
    ruta = Rutas.query.get(id)
    db.session.delete(ruta)
    db.session.commit()
    return jsonify(ruta_schema.dump(rutas))
 
 