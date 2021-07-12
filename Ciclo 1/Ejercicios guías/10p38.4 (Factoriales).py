"""
Imprimir los números de 1 hasta un número natural n dado, cada uno
con su respectivo factorial.
"""

n = int(input("Ingrese un número: "))
fac = 1

for i in range(1, n+1):
  fac *= i
  print(f"El factorial de {i} es {fac}")