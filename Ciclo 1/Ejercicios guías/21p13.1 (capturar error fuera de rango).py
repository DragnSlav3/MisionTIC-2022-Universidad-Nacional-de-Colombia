"""
Capture la excepción que evita que el usuario acceda a posiciones que
no se encuentran definidas en la lista dada y muestre el mensaje
Intenta acceder a una posición que no está en la lista:
"""

lista = [1, 2, 3, 4]

try:
  lista[5]
except Exception as e:
  print("Intenta acceder una posición que no está en el arreglo.\n")
  print(e, '\n', type(e))