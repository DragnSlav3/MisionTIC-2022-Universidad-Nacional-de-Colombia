"""
Desarrollar un programa que dado un número entero positivo n
calcule e imprima (separados por espacios) n/2 si es par o 3n+1 si es
impar. El programa debe repetir el proceso con el número resultado
de dicha operación mientras este sea diferente de 1. Por ejemplo para
el número 3 debe imprimir 10 5 16 8 4 2 1.
"""

n = int(input("Ingrese un número: "))

while n != 1:
  if n % 2 == 0:
    n = n / 2
    print(int(n), end=" ")
  else:
    n = (3 * n) + 1
    print(int(n), end=" ")

print("\nFin")