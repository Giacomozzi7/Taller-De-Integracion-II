from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/subirarchivo")
def sube_archivo():
    return "<p>Aqui se sube el archivo</p>"


if __name__ == "__main__":
    app.run()