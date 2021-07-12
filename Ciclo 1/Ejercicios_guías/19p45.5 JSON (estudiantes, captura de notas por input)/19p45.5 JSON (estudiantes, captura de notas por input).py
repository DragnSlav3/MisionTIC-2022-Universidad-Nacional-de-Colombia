from pprint import pprint as pp
import json
"""

continuar = "s"
codigo = 1
notas = []
jsonsalida = []


while continuar == "s":
    print("Estudiante", codigo)
    nota = input("Ingrese notas (separadas por coma): ").split(", ")
    notas.extend(nota)
    not_ = [float(i) for i in notas]
    diccionario = {"estudiante": codigo, "notas":not_}
    jsonsalida.append(diccionario)
    codigo += 1
    notas = []
    continuar = input("Continuar s/n ")

print(jsonsalida)

with open("estudiantes.json", "w") as salida:
    json.dump(jsonsalida, salida, indent=4)
"""

with open("estudiantes.json", "r") as e:
    notasjson = json.load(e)

jsonsalida = []

for i in notasjson:
    promedio = ((sum(i["notas"]))/(len(i["notas"])))
    diccionario = {"estudiante":i["estudiante"], "promedio":promedio}
    jsonsalida.append(diccionario)

with open("promedioestudiantes.json", "w") as promedios:
    json.dump(jsonsalida, promedios, indent=4)