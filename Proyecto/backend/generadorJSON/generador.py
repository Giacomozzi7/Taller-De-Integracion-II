#Por Francisco Giacomozzi R.
import json
import random as ra
import datetime
aData = []

#Randomizacion de fechas en el 2021
def randomFecha():
    princ = datetime.date(2021, 1, 1)
    fin = datetime.date(2021, 12, 31)
    dias_entre = (fin - princ).days
    random_dias = ra.randrange(dias_entre)
    random_date = str(princ + datetime.timedelta(days=random_dias))

    return random_date

#Posibles descripciones para categorias y subcategorias
aDescrip = [
            "Proin mattis nisl nec dui finibus, at venenatis neque mollis",
            "Morbi a felis tincidunt, vestibulum neque quis, pellentesque velit",
            "Sed scelerisque sapien id libero vulputate, id vestibulum lacus gravida",
            "Integer aliquam eros ut lobortis egestas",
            "Integer tempor dui ante, ac congue felis vulputate tincidunt",
            "Suspendisse pulvinar diam justo",
            "Curabitur dapibus, dolor id scelerisque malesuada, mi enim gravida augue, eget lobortis turpis ante ac turpis"
        ]

#Posibles parrafos para arquetipos
aParrafo = [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "Integer a elit id ligula pretium scelerisque",
            "Aenean maximus semper arcu, a blandit lectus vulputate sollicitudin",
            "Donec quis semper eros. Aliquam eu efficitur enim",
            "Maecenas egestas tempus nisl, a facilisis magna ultricies sit amet",
            "Aliquam tristique, sapien eget vestibulum finibus, nisl ipsum blandit dui, at iaculis felis orci eu tortor",
            "Sed ligula lacus, efficitur eget tellus a, blandit lobortis lorem",
            "Phasellus sodales nisi sit amet tempus convallis",
            "Proin in ipsum quis diam luctus aliquet",
            "Vestibulum tellus lacus, porttitor a faucibus nec, vehicula vel nulla",
            "Suspendisse quis pharetra velit",
            "Phasellus quis felis eget arcu suscipit venenatis"
]

#Funcion que genera estructura del JSON
def generaEstructura(nCOL,nMaxSubcat,nMaxArquetipos):
    nID = 0 ; nIDSubcat = 100 ; nIDArquetipo = 1000
    nC  = 1 ; nCA = 1

    for v in range(0,nCOL):
        nSubcat = ra.randint(1,nMaxSubcat)
        dict = { 
                "id" : nID,  
                "categoria": "categoria_"+str(nID + 1),
                "descripcion": ra.choice(aDescrip),
                "fecha_creacion": randomFecha(),
                "subcategoria": [{}] * nSubcat 
            }

        for k in range(0,nSubcat):
            nArquetipos = ra.randint(1,nMaxArquetipos)
            dictsubcat  = {
                "id_subcat": nIDSubcat,
                "titulo_subcat": "subcategoria_"+str(nC),
                "descripcion": ra.choice(aDescrip),
                "arquetipos": [{}] * nArquetipos
            }
            dict['subcategoria'][k] = dictsubcat
            nIDSubcat += 1
            nC += 1

            for j in range(0,nArquetipos):
                dictarquetipos = {
                    "id_arquetipo": nIDArquetipo,
                    "titulo_arquetipo": "arquetipo_"+str(nCA),
                    "parrafo": ra.choice(aParrafo)
                }
                dict['subcategoria'][k]['arquetipos'][j] = dictarquetipos
                nIDArquetipo += 1
                nCA += 1
        
        nID += 1
        aData.append(dict)
    
    return aData

#PRIMER PARAMETRO  : NUMERO TOTAL DE CATEGORIAS
#SEGUNDO PARAMETRO : NUMERO MAXIMO DE SUBCATEGORIAS POR CATEGORIA
#TERCER PARAMETRO  : NUMERO MAXIMO DE ARQUETIPOS POR SUBCATEGORIA
aData = generaEstructura(5,2,4)

with open('arquetipos.json', 'w') as arq:
    json.dump(aData, arq)


