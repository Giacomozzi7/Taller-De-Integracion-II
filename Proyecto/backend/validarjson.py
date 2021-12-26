import json
import os

#Valida si el archivo subido es un json y si cumple con la estructura para ser importado
def validarJSON(filename):
    sAlerta = ""
    ruta_archivo = os.path.abspath("./Proyecto/backend/uploads/" + filename)
    f = open(ruta_archivo,)
    try:
        data = json.load(f)
        try:
            data[0]['categoria']
            data[0]['subcategoria']
            data[0]['subcategoria'][0]['arquetipos']
        except:
            sAlerta = "El archivo no tiene la estructura adecuada"
    except:
        sAlerta = "El archivo ingresado no es un JSON"

    return sAlerta
