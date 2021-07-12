import json
from pprint import pprint as pp

llaves = ["#r$t", "l*g+l$", "q+$m", "cr$s", "n*sl", "m$#c#n$s", "l¬b¬rt*s", "*d", "#g#t", "#+"]
valores = ["erat", "ligula", "quam",  "cras", "nisl", "maecenas", "lobortis", "id", "eget", "eu"]

diccionario = dict(zip(llaves, valores))


with open ("encriptado.json", "w") as enc:
    json.dump(diccionario, enc, indent=4)

with open ("encriptado.json", "r") as des:
    salida = json.load(des)

diccionario_resultado = {}
for clave in salida:
    key = str(clave)
    key = (key.replace("$", "a"))
    key = (key.replace("#", "e"))
    key = (key.replace("*", "i"))
    key = (key.replace("¬", "o"))
    key = (key.replace("+", "u"))
    valor_diccionario = salida[clave]
    diccionario_resultado[key] = valor_diccionario

with open ("desencriptado.json", "w") as dd:
    json.dump(diccionario_resultado, dd, indent=4)