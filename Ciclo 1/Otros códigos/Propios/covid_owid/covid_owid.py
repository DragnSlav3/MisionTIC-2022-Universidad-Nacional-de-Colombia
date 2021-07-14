# Este script descarga la última actualización sobre información COVID de la página 
# Our World In Data, disponible en GitHub, en formato JSON.
# Crea una lista con la abreviatura de cada país, excluyendo las entradas con encabezado 
# "OWID", que no corresponden a países. Algunos países no cuentan con la información sobre 
# el número total de muertes, estos son almacenados en la variable "sinreportes", y se
# excluyen del proceso. 
# La información sobre el total de casos y el total de muertes en la base de datos original
# se encuentra dentro de un diccionario llamado "data" por cada país, por lo que el script
# accede únicamente a la entrada más reciente [-1]. La fecha se tiene en cuenta y se almacena.
# Aunque el archivo original también incluye el dato de muertes por millón de habitantes,
# este dato se genera de manera dinámica haciendo la división correspondiente.
# La información de cada país se almacena en formato diccionario y se agreag a la variable lista
# "jsonsalida", la cual es convertida y guardada en un archivo JSON llamado "jsonsalida.json".

import json
import requests

json_data = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.json")
json1 = json.loads(json_data.text)

paises = []
sinreportes = []
for k, v in json1.items():
    if k not in paises and k.startswith("OWID") == False:
        paises.append(k)
    if 'total_deaths' not in v["data"][-1]:
        sinreportes.append(k)

conreportes = []
for pais in paises:
    if pais not in sinreportes:
        conreportes.append(pais)

jsonsalida = []
for pais in conreportes:
    diccionario = {
        "abreviacion":pais, 
        "nombre":json1[pais]['location'],
        "poblacion": int(json1[pais]['population']), 
        "total_muertes":int(json1[pais]["data"][-1]['total_deaths']),
        "muertes_x_millon":int((int(json1[pais]["data"][-1]['total_deaths']))/(json1[pais]['population']/1000000)), 
        "fecha":json1[pais]["data"][-1]['date']
        }
    jsonsalida.append(diccionario)

with open("jsonsalida.json", "w") as datossalida:
    json.dump(jsonsalida, datossalida, indent=4)
print(f"Archivo JSON generado satisfactoriamente. Total de entradas: {len(jsonsalida)}.")