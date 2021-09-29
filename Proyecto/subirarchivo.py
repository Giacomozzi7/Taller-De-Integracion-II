import os
from flask import Flask, render_template, request, url_for, send_from_directory
from flask_pymongo import PyMongo
from werkzeug.utils import redirect, secure_filename
from werkzeug.datastructures import FileStorage

UPLOAD_FOLDER = os.path.abspath("./Downloads/")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def main_page():
  return """<p>Hello world!</p>
            <br>
            <a href="/subirarchivo">Subir archivo</a>
  """

@app.route("/subirarchivo")
def upload_file():
  return render_template('subirarchivo.html')

@app.route("/upload", methods=['GET', 'POST'])
def uploader():
  if request.method == 'POST':
    f = request.files['archivo']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for("obtener_archivo", filename = filename))

@app.route("/ArchivosJSON/<filename>")
def obtener_archivo(filename):
  return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == '__main__':
  app.run(debug=True)