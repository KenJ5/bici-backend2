from config.db import app, db, ma

class comunidad(db.Model):
    tablename = "comunidad"

    id = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id'))
    nombre = db.Column(db.String(100))


    def init(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre


with app.app_context():
    db.create_all()

class comunidadSchema(ma.Schema):
    class Meta:
        fields = ('id','id_usuario','nombre')