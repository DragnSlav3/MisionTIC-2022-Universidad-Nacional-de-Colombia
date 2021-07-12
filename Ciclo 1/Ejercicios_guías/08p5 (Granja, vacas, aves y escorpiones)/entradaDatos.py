import json

cantidadVacas = int(input("Ingrese la cantidad V de vacas: "))
corralVacasLista = input("Ingrese las medidas del corral N x M: ").split(", ")
corralN, corralM = tuple(corralVacasLista)
areaCorralVacas = int(corralN) * int(corralM)
perimetroCorralVacas = (int(corralN) + int(corralM)) * 2
rendimientoVacaTerreno = int(input("Ingrese los metros cuadrados de pasto necesarios (K) para que una vaca produzca una determinada cantidad de leche: "))
rendimientoVacaLeche = int(input("Ingrese la cantidad (X) de leche que produce una vaca por día: "))
cantidadAves = int(input("Ingrese la cantidad A de aves: "))
precioAlambre = float(input("Ingrese el valor del metro de alambre: "))
precioVarilla = float(input("Ingrese el valor del metro de varilla: "))
precioTablas = float(input("Ingrese el valor del metro de tablas: "))

datos = [{
    "cantidadVacas":cantidadVacas,
    "areaCorralVacas":areaCorralVacas,
    "perimetroCorralVacas":perimetroCorralVacas,
    "rendimientoVacaTerreno":rendimientoVacaTerreno,
    "rendimientoVacaLeche":rendimientoVacaLeche,
    "cantidadAves":cantidadAves,
    "precioAlambre":precioAlambre,
    "precioVarilla":precioVarilla,
    "precioTablas":precioTablas
    }]

print(datos)

with open("datos.json", "w") as salida:
    json.dump(datos, salida, indent=4)