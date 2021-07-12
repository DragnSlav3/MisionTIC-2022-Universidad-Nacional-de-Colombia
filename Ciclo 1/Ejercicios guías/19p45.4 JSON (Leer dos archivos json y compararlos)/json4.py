"""
Desarrolle un programa que lea dos archivos JSON, y encuentre los
componentes clave:valor que son iguales en ambos. Genere un nuevo
archivo JSON con las coincidencias exactas entre los dos archivos.
"""

import json
from pprint import pprint as pp

with open("json1.json", "r") as j1:
    f1 = json.load(j1)

with open("json2.json", "r") as j2:
    f2 = json.load(j2)

f3 = []


for i in f1:
    diccionario={}
    for j in f2:
        if i["nombre"] == j["nombre"] and i["apellido"] == j["apellido"]:
            diccionario["nombre"] = i["nombre"]
            diccionario["apellido"] = i["apellido"]
            f3.append(diccionario)

with open ("json3.json", "w") as j3:
    json.dump(f3, j3)