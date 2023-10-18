from config.db import app, db, ma

class Comentarios(db.Model):
    __tablename__ = "tblcomentarios"

    id = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id'))
    contenido = db.Column(db.String(100))
    titulo = db.Column(db.String(20))

    def __init__(self,id_usuario,contenido,titulo):
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.titulo = titulo


with app.app_context():
    db.create_all()

class ComentariosSchema(ma.Schema):
    class Meta:
        fields = ('id','id_usuario','contenido','titulo')       