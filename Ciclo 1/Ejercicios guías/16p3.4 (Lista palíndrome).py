"""
Desarrollar un programa que determine si una lista es palíndrome.
Una lista es palíndrome si el elemento en la posición i es el mismo de
la posición n-1 -i con n la longitud de la lista.
"""

lista = ["a", 1, True, True, 1, "a"]
#lista = [1, 2, "a", "b", True, False]
invert = lista[::-1]

if lista != invert:
  print("No es una lista palíndrome.")
else:
  print("Sí es una lista palíndrome")
