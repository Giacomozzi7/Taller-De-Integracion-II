import os
import itertools
from flask import Flask, render_template, request, url_for, send_from_directory, redirect, flash
from validarjson import validarJSON
from import_mongo import inicializarBDD
from exportar_data import exportaData
from filtrar_data import *
from updatecategorias import updateCategoria, eliminaCategoria, updateArquetipo

#Se definen directorios para templates y archivos subidos
UPLOAD_FOLDER = os.path.abspath("./Proyecto/backend/uploads/")

#Intenta cargar directorio de templates segun corresponda
try:
    template_dir = os.path.abspath('..//Taller-De-Integracion-II//Proyecto//frontend//templates')
except:
   template_dir = os.path.abspath('..//Proyecto//frontend//templates')

#Intenta cargar directorio de static segun corresponda
try:
    static_dir = os.path.abspath('..//Taller-De-Integracion-II//Proyecto//frontend//static')
except:
    static_dir = os.path.abspath('..//Proyecto//frontend//static')


app = Flask(__name__, template_folder = template_dir, static_folder = static_dir)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
filename = ""
aData = []
aCat = []
aArq = []

#Ruta para Main
@app.route("/")
def hello_world():
    return render_template('main.html')

#Ruta para subir archivo
@app.route("/subirarchivo", methods=["GET", "POST"])
def sube_archivo():
    sAlerta = ""
    if request.method == "POST": #Si se sube el archivo
        global filename
        file = request.files["archivo"]
        filename = file.filename
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        sAlerta = validarJSON(filename) #Se valida la estructura y el formato del archivo
        if sAlerta == "":
            inicializarBDD(filename)  #Se inicializa la conexion y la importacion de datos en mongo
            global aData ; aData = exportaData()
            return redirect(url_for("crear_documento"))
        else:
            render_template('subir_archivo.html',a = sAlerta)

    return render_template('subir_archivo.html',a = sAlerta)

#Ruta para ver el archivo json subido
@app.route("/verjson")
def ver_json():
    print("filename",filename)
    if filename != "": #si se ha subido algun archivo, lo muestra
        return redirect(url_for("get_file", filename = filename))
    else: #sino devuelve a crear_documento
        return redirect(url_for("crear_documento"))

#Ruta que muestra el archivo json de manera independiente
@app.route("/creardocumento/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

#Ruta para confeccionar los documentos
@app.route("/creardocumento")
def crear_documento():
    if len(aData) > 0:
        aNData = exportaData()
        return render_template('crear_documento.html', aData = aNData)
    else:
        return redirect(url_for("sube_archivo"))

#Ruta para ver y editar categorias
@app.route("/vercategorias")
def verCategorias():
    global aCat
    if len(aData) > 0:
        aCat= filtrarCategoria()
        return render_template("/ver_categorias.html", aData = aCat)
    else:
        return redirect(url_for("sube_archivo"))

@app.route('/editarcategorias/<id>', methods=['POST','GET'])
def editarCategorias(id):
    if len(aData) > 0:
        categoria = aCat[int(id)]
        return render_template("/editar_categorias.html", aData = categoria)
    else:
        return redirect(url_for("sube_archivo"))

@app.route('/actualizar/<id>', methods=['POST'])
def update_Categoria(id):
    if request.method =='POST':
        fecha = request.form['fecha']
        categoria = request.form['categoria']
        descripcion = request.form['descripcion']
        updateCategoria(id,fecha,categoria,descripcion)

        return redirect(url_for('verCategorias'))

@app.route('/eliminar/<string:id>', methods = ['POST','GET'])
def eliminar_Categoria(id):
    eliminaCategoria(id)
    return redirect(url_for('verCategorias'))

#Ruta para ver y editar arquetipos
@app.route("/verarquetipos")
def verArquetipo():
    global aArq
    if len(aData) > 0:
        aArq = filtrarArquetipo()
        return render_template("/ver_arquetipos.html", aNData = aArq)
    
    else:
        return redirect(url_for("sube_archivo"))

@app.route('/editararquetipos/<idArq>', methods=['POST','GET'])
def editarArquetipos(idArq):
    if len(aData) > 0:
        nuevoId = int(idArq)-1000
        arque = aArq[nuevoId]
        return render_template("/editar_arquetipos.html", aData = arque)
    else:
        return redirect(url_for("sube_archivo"))

@app.route('/actualizarArq/<idArq>', methods=['POST'])
def update_Arquetipo(idArq):
    if request.method =='POST':
        titulo = request.form['titulo']
        parrafo = request.form['parrafo']
        updateArquetipo(idArq,titulo,parrafo)

        return redirect(url_for('verArquetipo'))

#Init
if __name__ == "__main__":
    app.run(debug=True)