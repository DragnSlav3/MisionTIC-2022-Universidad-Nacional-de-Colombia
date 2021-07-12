"""
Desarrollar un programa que dadas dos listas determine qué
elementos tiene la primer lista que no tenga la segunda lista.
Ejemplo
lista1: [1, 'Hola', -12.3, True]
lista2: [11, -12.3, 'Hola', False]
salida: [1, True]
"""

lista1 = [1, 'Hola', -12.3, True]
lista2 = [11, -12.3, 'Hola', False]
salida = []

for i in lista1:
  if i not in lista2:
    salida.append(i)

print(salida)