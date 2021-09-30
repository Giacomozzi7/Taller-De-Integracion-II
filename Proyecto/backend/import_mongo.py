from pymongo import MongoClient
import json
import os

def inicializarBDD(filename):
    ruta_archivo = os.path.abspath("./Proyecto/backend/uploads/" + filename)
    #Inicializacion cliente Mongo
    MONGO_URI = 'mongodb://localhost'
    client =MongoClient(MONGO_URI)

    #Se inicializa la base de datos 'data' y la coleccion 'arquetipos'
    db = client['data']
    coleccion =db['arquetipos']

    db.arquetipos.delete_many({})

    #Abre el archivo json subido
    f = open(ruta_archivo,)
    file_data = json.load(f)
    
    #Importa las colecciones a mongoDB
    if isinstance(file_data, list):
        coleccion.insert_many(file_data)  
    else:
        coleccion.insert_one(file_data)

    #buscar = db.arquetipos.find({}, {})


inicializarBDD("arquetipos.json")


