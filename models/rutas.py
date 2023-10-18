from config.db import app, db, ma

class Rutas(db.Model):
    tablename = "rutas"

    id = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id'))
    longitud = db.Column(db.String(100))
    punto_a = db.Column(db.String(50))
    punto_b = db.Column(db.String(50))

    def init(self, id_usuario, longitud, punto_a, punto_b):
        self.id_usuario = id_usuario
        self.longitud = longitud
        self.punto_a = punto_a
        self.punto_b = punto_b


with app.app_context():
    db.create_all()

class RutasSchema(ma.Schema):
    class Meta:
        fields = ('id','id_usuario','longitud','punto_a','punto_b'
        )