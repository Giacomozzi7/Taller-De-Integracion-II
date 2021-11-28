from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)

#Se inicializa la base de datos 'data' y la coleccion 'arquetipos'
db = client['data']
coleccion = db['arquetipos']

#Busca todas las categorias para ser mostradas en las tablas
def filtrarCategoria():
    aCat =[]
    buscar = db.arquetipos.find({}, {"categoria":1,"_id":0,"id":1,"fecha_creacion":1,"descripcion":1})

    for busq in buscar:
        tCat = (busq['id'],busq['fecha_creacion'],busq['categoria'],busq['descripcion'])
        aCat.append(tCat)
    
    print(aCat)
    return aCat

#filtrarCategoria()

#Busca todos los arquetipos para ser mostrados en las tablas
def filtrarArquetipo():
    aArq = []
    buscar = db.arquetipos.find({}, {"subcategoria":1})
    for busq in buscar: 
        subcat = busq['subcategoria']
        for arq in subcat:
            arque = arq['arquetipos']
            for data in arque:
                tArq = (data['id_arquetipo'],data['titulo_arquetipo'],data['parrafo'])
                aArq.append(tArq)
    return aArq

#Busca todas las subcategorias para ser mostrados en las tablas
def filtrarSubcategoria():
    aSubcat = []
    buscar = db.arquetipos.find({}, {"subcategoria":1})
    for busq in buscar: 
        subcat = busq['subcategoria']
        for val in subcat:
            tSubcat = (val['id_subcat'],val['titulo_subcat'],val['descripcion'])
            aSubcat.append(tSubcat)
       
    return aSubcat


