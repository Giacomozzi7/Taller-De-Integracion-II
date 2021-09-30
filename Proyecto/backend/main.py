import os
from flask import Flask, render_template, request, url_for, send_from_directory, redirect

#Se definen directorios para templates y archivos subidos
UPLOAD_FOLDER = os.path.abspath("./Proyecto/backend/uploads/")
template_dir = os.path.abspath('..//Taller-De-Integracion-II//Proyecto//frontend//templates')
app = Flask(__name__,template_folder=template_dir)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
    return render_template('main.html')

@app.route("/subirarchivo", methods=["GET", "POST"])
def sube_archivo():
    if request.method == "POST":
        file = request.files["archivo"]
        filename = file.filename
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return redirect(url_for("get_file", filename = filename))
    
    return render_template('subir_archivo.html')

@app.route("/subirarchivo/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/editararquetipos")
def editar_arquetipos():
    return "<p>Aqui se editar los arquetipos</p>"

@app.route("/creardocumento")
def crear_documento():
    return "<p>Aqui se crean los documentos</p>"

if __name__ == "__main__":
    app.run(debug=True)