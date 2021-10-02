import os
from flask import Flask, render_template, request, url_for, send_from_directory, redirect, flash
from validarjson import validarJSON
from import_mongo import inicializarBDD
from exportar_data import exportaData

#Se definen directorios para templates y archivos subidos
UPLOAD_FOLDER = os.path.abspath("./Proyecto/backend/uploads/")
template_dir = os.path.abspath('..//Taller-De-Integracion-II//Proyecto//frontend//templates')
static_dir = os.path.abspath('..//Taller-De-Integracion-II//Proyecto//frontend//static')
app = Flask(__name__,template_folder=template_dir,static_folder = static_dir)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
filename = ""
aData = []

#Ruta para Main
@app.route("/")
def hello_world():
    return render_template('main.html')

#Ruta para subir archivo
@app.route("/subirarchivo", methods=["GET", "POST"])
def sube_archivo():
    sAlerta= ""
    if request.method == "POST": #Si se sube el archivo
        global filename
        file = request.files["archivo"]
        filename = file.filename
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        sAlerta = validarJSON(filename) #Se valida la estructura y el formato del archivo
        if sAlerta =="":
            inicializarBDD(filename)  #Se inicializa la conexion y la importacion de datos en mongo
            global aData ; aData = exportaData()
            return redirect(url_for("crear_documento"))
        else:
            render_template('subir_archivo.html',a= sAlerta)

        
    return render_template('subir_archivo.html',a = sAlerta)

#Ruta para ver el archivo json subido
@app.route("/verjson")
def ver_json():
    print("filename",filename)
    if filename != "": #si se ha subido algun archivo, lo muestra
        return redirect(url_for("get_file", filename= filename))
    else: #sino devuelve a crear_documento
        return redirect(url_for("crear_documento"))

#Ruta que muestra el archivo json de manera independiente
@app.route("/creardocumento/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

#Ruta para confeccionar los documentos
@app.route("/creardocumento")
def crear_documento():
    print(aData)
    if len(aData)>0:
        return render_template('crear_documento.html', aData = aData)
    else:
        return redirect(url_for("sube_archivo"))

#Ruta para editar los arquetipos
@app.route("/editararquetipos")
def editar_arquetipos():
    return "<p>Aqui se editar los arquetipos</p>"




#Init
if __name__ == "__main__":
    app.run(debug=True)