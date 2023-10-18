from flask import Flask, redirect, jsonify, render_template, request, session
from config.db import app, db
from flask_cors import CORS
from api.usuario import ruta_usuarios
from api.comentarios import ruta_comentarios
from api.rutas import ruta_rutas
from api.comunidad import ruta_comunidad
from api.sistema_alerta import ruta_alerta

from models.usuario import Usuario, UsuarioSchema
cliente_schema = UsuarioSchema()
clientes_schema = UsuarioSchema(many=True)

app.register_blueprint(ruta_usuarios, url_prefix="/api_user")
app.register_blueprint(ruta_rutas, url_prefix="/api_rutas")
app.register_blueprint(ruta_comentarios, url_prefix="/api_comentarios")
app.register_blueprint(ruta_comunidad, url_prefix="/api_comunidad")
app.register_blueprint(ruta_alerta, url_prefix="/api_alerta")

CORS(app)
CORS(app, resources={r"/api_user/*": {"origins": "http://127.0.0.1:5000"}})

@app.route("/")
def index():

    if 'usuario' in session:       
        logged_in = True
        return render_template('index.html', usuario=session['usuario'], id_user=session['id_user'], logged_in=logged_in)
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/trayecto")
def trayecto():
    if 'usuario' in session:       
        logged_in = True
        return render_template('trayecto.html', usuario=session['usuario'], id_user=session['id_user'], logged_in=logged_in)
    else:
        return redirect('/login')
   

@app.route("/rutas")
def rutas():
    if 'usuario' in session:       
        logged_in = True
        return render_template('rutas.html', usuario=session['usuario'], id_user=session['id_user'], logged_in=logged_in)
    else:
        return redirect('/login')
   

@app.route("/ingresar", methods=['POST'])
def ingresar():
    email = request.form['email']
    password = request.form['pass']
    user = db.session.query(Usuario.id).filter(Usuario.email == email, Usuario.contraseña == password).all()
    resultado = clientes_schema.dump(user)
    id_user = Usuario.query.filter_by(email=email, contraseña=password).first()

    if len(resultado)>0: 
    
        session['id_user']=id_user.id
        session['usuario'] = email
        
        return redirect('/')
    else:
        return redirect('/youtube')   
@app.route("/register") 
def register():     
    return render_template('register.html')  
@app.route("/registrar", methods=['POST']) 
def registrar():     
    name = request.form['name']     
    email = request.form['email']     
    password = request.form['pass']     
    new_user = Usuario(name, email, password)     
    db.session.add(new_user)     
    db.session.commit()     
    return redirect('/login')
   
if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')