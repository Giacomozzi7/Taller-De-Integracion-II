import os
from flask import Flask, render_template, request, url_for, send_from_directory

template_dir = os.path.abspath('..//Taller-De-Integracion-II//Proyecto//frontend//templates')
app = Flask(__name__,template_folder=template_dir)

@app.route("/")
def hello_world():
    return render_template('main.html')

@app.route("/subirarchivo")
def sube_archivo():
    return render_template('subir_archivo.html')

@app.route("/editararquetipos")
def editar_arquetipos():
    return "<p>Aqui se editar los arquetipos</p>"

@app.route("/creardocumento")
def crear_documento():
    return "<p>Aqui se crean los documentos</p>"

if __name__ == "__main__":
    app.run(debug=True)