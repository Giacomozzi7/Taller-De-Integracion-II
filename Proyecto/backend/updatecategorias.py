from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)

#Se inicializa la base de datos 'data' y la coleccion 'arquetipos'
db = client['data']
coleccion = db['arquetipos']

#Funcion para actualizar categorias
def updateCategoria(id,fecha,categoria,descripcion):
    db.arquetipos.update_one({
    'id': int(id)
    },{
    '$set': {
        'fecha_creacion': fecha,
        'categoria': categoria,
        'descripcion': descripcion
    }
    }, upsert=False)

#Funcion para eliminar categoria
def eliminaCategoria(id):
    db.arquetipos.delete_one({"id" : int(id)})


#Funcion para actualizar arquetipos
def updateArquetipo(idArq,titulo,parrafo):
    id_subcat = 102
    idArq = int(idArq)
    print('update')

    #print(idArq,titulo,parrafo)
