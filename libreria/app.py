from flask import render_template, Flask, url_for, redirect, request, flash
import dbMongo
import models
import ai

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

#//////////////////////////////////
#Listando los libros por categorias
#/////////////////////////////////
@app.route('/listCategorias')
def listCategorias():
    dbMongo.connection('Libreria', 'Libros')
    listCategorias = dbMongo.show('categoria')
    categorias = []
    
   
        
    return render_template('pages/listar_categorias.html', listCategorias=listCategorias, lenCategoria = len(listCategorias))

@app.route('/home')
def home():
    dbMongo.connection('Libreria','Libros')
    nombres = dbMongo.show('nombre')
    categoria = dbMongo.show('categoria')
    autor = dbMongo.show('autor')
    code = dbMongo.show('codigo')
    print(nombres)
    
    return render_template('pages/index.html', nombres =nombres, lenNombres = len(nombres), categoria = categoria,
                           autor = autor, code = code)
    
# /////////////////////////////////////////////////////////////////////
# Metodos que nos llevan a ver todos los libros de cada listCategorias
# /////////////////////////////////////////////////////////////////////

@app.route('/cTerror')
def cTerror():
    dbMongo.connection('Libreria','Libros')
    listaLibros = dbMongo.showby2('categoria','Terror','nombre')
    print(listaLibros)  
    
    return render_template('pages/cEspecifica.html', libroslist = listaLibros, librosLen = len(listaLibros))

@app.route('/cAccion')
def cAccion():
    dbMongo.connection('Libreria', 'Libros')
    listaLibros = dbMongo.showby2('categoria', 'Acción ', 'nombre')
    
    return render_template('pages/cEspecifica.html', libroslist = listaLibros, librosLen = len(listaLibros))


@app.route('/cRomance')
def cRomance():
    dbMongo.connection('Libreria', 'Libros')
    listaLibros = dbMongo.showby2('categoria', 'Romance', 'nombre')
    
    return render_template('pages/cRomance.html', libroslist = listaLibros, librosLen = len(listaLibros))



# //////////////////////////////
# Ir a comentarios y guardarlos
# //////////////////////////////


#Crear ruta para realizar los comentarios:
@app.route('/comentarios')
def comentarios():
    
    return render_template('pages/comentarios.html')




#Guardar comentarios
@app.route("/comments", methods=["POST"])
def save_comment():
    # Extraemos los datos del formulario
    name = request.form["name"]
    comment = request.form["comment"]
    verify = [comment]
    data = {'name':name, 'comment':comment}
    
    if ai.notSpam(verify) != True:
        flash('We dont accpet Spam')
        return comentarios()
    else:
        dbMongo.connection('Libreria', 'Comentarios')
        dbMongo.save(data)
        flash('Thanks for helping us to be better')
        return comentarios()
        
    

#Crear ruta para ver todos los comentarios

@app.route('/tComentarios')
def tComentarios():
    dbMongo.connection('Libreria', 'Comentarios')
    comments = dbMongo.show('comment')
    
    users = dbMongo.show('name')
    
    return render_template('pages/tComentarios.html', comments = comments, lenComment = len(comments), users = users)
    









# ////////////////////////////////////////////////////////////////////////////////////////////////

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
    #Obtenemos los datos de contra
    contraDB = dbMongo.getUser('correo',correo)
    #Obtenemos los datos de correo
    correoDB = dbMongo.getUser('correo', correo)
    
    if contraDB != None and contraDB != None:    
        contrauser = contraDB['contra']
        correouser = correoDB['correo']
        if contra != contrauser or correo != correouser:
            flash('Contraseña invalida')
            return redirect(url_for('inicio'))
        else:
            flash('Bienvenido a libreria Fenix')
            return home()
    else:
        flash('el usuario no existe')
        return redirect(url_for('inicio'))
    
    
    # contrauser = contraDB['contra']
    
    #Obtenemos los datos de correo
    # correouser = correoDB['correo']
    
    #Validamos los datos de acceoso

    # if contra != contrauser or correo != correouser :
    #     flash('Contraseña o Correo invalido')
    #     return redirect(url_for('inicio'))
    # else:
    #     flash('Bienvenido a libreria Fenix')
    #     return home()
        
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

