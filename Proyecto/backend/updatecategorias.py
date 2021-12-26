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


#Funcion para actualizar subcategorias
def updateSubcategoria(idSubcat,titulo,descripcion):
    idSubcat = int(idSubcat)
    db.arquetipos.update(
    {'subcategoria':{'$elemMatch':{'id_subcat': idSubcat}}},
    {'$set':{'subcategoria.$.titulo_subcat':titulo,'subcategoria.$.descripcion':descripcion}}
    )

#Funcion para eliminar subcategorias
def eliminarSubcategoria(idSubcat):
    buscar = db.arquetipos.update_one(
    {'subcategoria':{'$elemMatch':{'id_subcat': int(idSubcat)}}},
    {'$pull':{'subcategoria':{'id_subcat': int(idSubcat)}}}
    )

