import os
from flask import Flask, render_template, request, url_for, send_from_directory, redirect, flash
from validarjson import validarJSON

#Se definen directorios para templates y archivos subidos
UPLOAD_FOLDER = os.path.abspath("./Proyecto/backend/uploads/")
template_dir = os.path.abspath('..//Taller-De-Integracion-II//Proyecto//frontend//templates')
app = Flask(__name__,template_folder=template_dir)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

filename = ""

@app.route("/")
def hello_world():
    return render_template('main.html')

@app.route("/subirarchivo", methods=["GET", "POST"])
def sube_archivo():
    if request.method == "POST":
        global filename
        file = request.files["archivo"]
        filename = file.filename
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        sAlerta = validarJSON(filename)
        print("ALERTA: ", sAlerta)
        if sAlerta =="":
            return redirect(url_for("crear_documento"))
    
    return render_template('subir_archivo.html')

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

#Ruta pàra confeccionar los documentos
@app.route("/creardocumento")
def crear_documento():
    return render_template('crear_documento.html')

@app.route("/editararquetipos")
def editar_arquetipos():
    return "<p>Aqui se editar los arquetipos</p>"

if __name__ == "__main__":
    app.run(debug=True)