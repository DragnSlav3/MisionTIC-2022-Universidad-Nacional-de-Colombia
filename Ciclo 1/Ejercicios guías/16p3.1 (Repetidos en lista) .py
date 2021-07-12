"""
Desarrollar un programa que determine si en una lista no existen
elementos repetidos.
"""
lista = ["Carlos", "María", "José", "Miguel", "María"]

def repetidos(lista):
  nueva = []
  mensaje = ""
  for i in lista:
    if i not in nueva:
      nueva.append(i)
      mensaje = "No hay elementos repetidos"
    else:
      mensaje = "En la lista sí hay elementos repetidos"
      break
  return mensaje

print(repetidos(lista))