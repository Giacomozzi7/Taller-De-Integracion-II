from pymongo import MongoClient


#Se consulta la informacion y se estructura para ser enviada al frontend
def exportaData():
    aData = []
    MONGO_URI = 'mongodb://localhost'
    client =MongoClient(MONGO_URI)
    #Se inicializa la base de datos 'data' y la coleccion 'arquetipos'
    db = client['data']
    coleccion =db['arquetipos']

    #Se recorren las colecciones para almacenar categorias_subcategorias y arquetipos
    buscar = db.arquetipos.find({}, {"categoria":1,"fecha_creacion":1,"subcategoria":1})
    for busq in buscar:
        aColeccion = []
        aColeccion.append(busq["categoria"]) ; aColeccion.append(busq["fecha_creacion"])
        len_subcat = len(busq["subcategoria"])
        aSubcat=[];aArquetipos=[]
        for i in range(len_subcat):
            aSubcat.append(busq["subcategoria"][i]["titulo_subcat"])

            aArq=[]
            len_arquetipos = len(busq["subcategoria"][i]["arquetipos"])
            for k in range(len_arquetipos):
                aArq.append((busq["subcategoria"][i]["arquetipos"][k]['titulo_arquetipo'],busq["subcategoria"][i]["arquetipos"][k]['parrafo']))
            
            aArquetipos.append(aArq)

        aData.append([aColeccion,aSubcat,aArquetipos])

    return aData
