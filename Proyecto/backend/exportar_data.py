from pymongo import MongoClient


#Se consulta la informacion y se estructura para ser enviada al frontend
def exportaData():
    aData = []
    MONGO_URI = 'mongodb://localhost'
    client =MongoClient(MONGO_URI)
    #Se inicializa la base de datos 'data' y la coleccion 'arquetipos'
    db = client['data']
    coleccion =db['arquetipos']

    aColeccion = []
    buscar = db.arquetipos.find({}, {"categoria":1,"fecha_creacion":1,"subcategoria":1})
    for busq in buscar:
        aColeccion.append(busq["categoria"])
        aColeccion.append(busq["fecha_creacion"])

        len_subcat = len(busq["subcategoria"])

        aSubcat=[]
        for i in range(len_subcat):
            aSubcat.append(busq["subcategoria"][i]["titulo_subcat"])
        
        print(aColeccion)
        print(aSubcat)

        break


exportaData()