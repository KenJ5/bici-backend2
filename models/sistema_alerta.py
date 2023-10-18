from config.db import app, db, ma

class Alerta(db.Model):
    __tablename__ = "alerta"

    id = db.Column(db.Integer, primary_key = True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('rutas.id'))
    tipo = db.Column(db.String(100))


    def __init__(self,id_ruta,tipo):
        self.id_ruta = id_ruta
        self.tipo = tipo


with app.app_context():
    db.create_all()

class AlertaSchema(ma.Schema):
    class Meta:
        fields = ('id','id_ruta','tipo')       