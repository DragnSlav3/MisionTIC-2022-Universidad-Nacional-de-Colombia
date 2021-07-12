"""
Imprimir los números pares en forma descendente hasta 2 que son
menores o iguales a un número natural n >= 2 dado.
"""

n = int(input("Ingrese un número positivo mayor o igual a 2: "))

for i in range(n, 1, -2):
  if i % 2 == 0:
    print(i)
  else:
    continue