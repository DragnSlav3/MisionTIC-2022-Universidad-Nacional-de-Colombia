'''
Imprimir los números pares en forma descendente hasta 2 que son
menores o iguales a un número natural n >= 2 dado.
'''

n = int(input("Ingrese un número menor o igual a 0: "))

if n % 2 != 0:
  n -= 1
else:
  n = n

while n >= 2:
  print(n)
  n -= 2

print("\nFin")