"""
Desarrollar un programa que imprima el cuadrado del número que el
usuario ingresa mientras que el número ingresado no sea negativo.
"""

x = int(input("Ingrese un número: "))
s = 0

while x >= 0:
  s = x ** 2
  print(f"El cuadrado de {x} es {s}\n")
  x = int(input("Ingrese un número: "))
print("Fin")