"""
Imprima los nombres completos (nombre y apellidos) de las personas
que practican el deporte ingresado por el usuario.
Imprima los nombres completos (nombre y apellidos) de las personas
que estén en un rango de edades dado por el usuario.
"""

import json

with open ("json/deportes.json", "r") as f:
  contenido = json.load(f)


deporte = input("Ingrese el deporte: ")

for k, v in contenido.items():
  if deporte in v["deportes"]:
    print(v["nombres"],v["apellidos"])

print()

edadinf = int(input("Ingrese el rango de edad inferior: "))
edadsup = int(input("Ingrese el rango de edad superior: "))

for k, v in contenido.items():
  if v["edad"] >= edadinf and v["edad"] <= edadsup:
    print(v["nombres"],v["apellidos"]) 


with open ("json/deportes.json", "r") as f:
  contenido = json.load(f)

resultado = {}

for k, v in contenido.items():
  for deporte in (v["deportes"]):
    if deporte not in resultado:
      resultado [deporte] = [k]
    else:
      resultado [deporte].append (k)

with open ("json/resultado.json", "w", encoding="utf-8") as f:
  json.dump(resultado, f, indent=4)