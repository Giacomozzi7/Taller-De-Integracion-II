from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/subirarchivo")
def sube_archivo():
    return "<p>Aqui se sube el archivo</p>"

@app.route("/editararquetipos")
def edita_rarquetipos():
    return "<p>Aqui se editar los arquetipos</p>"

@app.route("/creardocumento")
def crear_documento():
    return "<p>Aqui se crean los documentos</p>"

if __name__ == "__main__":
    app.run()