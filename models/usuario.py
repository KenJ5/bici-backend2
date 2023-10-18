from config.db import app, db, ma

class Usuario(db.Model):
    __tablename__ = "tblusuario"

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(50))
    contraseña = db.Column(db.String(100))

    def __init__(self,nombre,email,contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña= contraseña

with app.app_context():
    db.create_all()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','email','contraseña')       