""""
Realice una base de datos de estudiantes con estructuras de datos diccionarios, 
en la que solicite repetidamente por pantalla, la información de: 
Nombre, apellido, edad, estatura.

Teniendo en cuenta la información registrada, imprima un reporte con:

a. el total de ítems registrados 
b. el promedio de edad 
c. el promedio de estatura

Genere un archivo en formato .json con toda la información capturada, para ser compartido posteriormente con otro sistema.
"""
import json

"""
try:
  cantidad = int(input("¿Cuántos registros desea crear? "))
except ValueError:
  print("\nERROR: El valor debe ser un número.\n")
except Exception as e:
  print("HA HABIDO UN ERROR", e, type(e))

def entradas():
  nombres = input("Nombres: ")
  apellidos = input("Apellidos: ")
  edad = input("Edad: ")
  estatura = input("Estatura (en centímetros): ")

  return {"nombres" : nombres, "apellidos" : apellidos , "edad": edad, "estatura" : estatura}

diccionario = {}

for i in range (cantidad):
  diccionario [i] = entradas()

with open("json.json", 'w') as f:
  json.dump (diccionario, f, indent=4, ensure_ascii=False)


"""
with open("json.json", "r") as j:
    contenido = json.load(j)

print()
total_items = (len(contenido))
print(f"Total de alumnos: {total_items}")

suma_edades = 0

for k, v in contenido.items():
    suma_edades += int(v["edad"])

promedio_edades = suma_edades / total_items
print(f"Promedio de edad: {promedio_edades} años.")

suma_estaturas = 0

for k, v in contenido.items():
    suma_estaturas += int(v["estatura"])

promedio_estaturas = suma_estaturas / total_items
print(f"Promedio de estatura: {promedio_estaturas} centímetros.")

diccionario2 = {"total_items" : total_items, "promedio_edades" : promedio_edades, "promedio_estaturas" : promedio_estaturas}

"""
with open("reporte.json", 'w') as p:
  json.dump (diccionario2, p, indent=4)
"""