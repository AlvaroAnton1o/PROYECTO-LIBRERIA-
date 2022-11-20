from flask import render_template, Flask, url_for, redirect, request, flash
import dbMongo
import models

app = Flask(__name__)
app.secret_key = "fenixLibreria"


@app.route('/')
def index():
    return render_template('pages/login.html')

@app.route('/inicio')
def inicio():
    return redirect('/')

@app.route('/agregarLibro')
def agregarLibro():
    return render_template('pages/agregar.html')

@app.route('/agregarUser')
def agregarUser():
    return render_template('pages/agregar_usuario.html')

@app.route('/home')
def home():
    return render_template('pages/index.html')

@app.route('/addUser', methods=['GET', 'POST'])
def addUser():
    nombre = request.form['userNombre']
    correo = request.form['userCorreo']
    contra = request.form['userContra']
    contraConfirm = request.form['contraConfirm']
    
    if models.validar_correo(correo) != True:
        flash('Correo invalido')
        return redirect(url_for('inicio'))
    elif models.validar_contra(contra) != True:
        flash('Constraseña invalida')
        return redirect(url_for('inicio'))
    elif contra != contraConfirm:
        flash('Contraseñas no coinciden')
        return redirect(url_for('inicio'))
    else:
        user = {'nombre':nombre,'correo':correo, 'contra':contra}
        dbMongo.connection('Libreria','Usuarios')  
        dbMongo.save(user)
        flash('Bienvenido a libreria Fenix')
        return home()

@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    correo = request.form['txtCorreo']
    contra = request.form['txtContra']
    dbMongo.connection('Libreria','Usuarios')
    contraDB = dbMongo.getUser('correo',correo)
    contrauser = contraDB['contra']
        
    return 

@app.route('/guardarLibro', methods=['GET', 'POST'])
def guardarLibro():
    codigo = request.form['txtCodigo']
    nombre = request.form['txtNombre']
    categoria = request.form['txtCategoria']
    autor = request.form['txtAutor']
    data = {'codigo':codigo, 'nombre':nombre, 'categoria':categoria, 'autor':autor}
    dbMongo.connection('Libreria','Libros')
    dbMongo.save(data)
    return redirect('agregarLibro')

if __name__=='__main__':
    app.run(debug=True)

