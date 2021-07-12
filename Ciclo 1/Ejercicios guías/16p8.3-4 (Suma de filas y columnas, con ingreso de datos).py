"""
Desarrollar un programa que sume los elementos de una columna
dada de una matriz.
Desarrollar un programa que sume los elementos de una fila dada de
una matriz.
"""

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []

for i in range (filas):
  matriz.append ([])
  for j in range (columnas):
    valor = float(input(f"Fila {i+1}, Columna {j+1}: "))
    matriz[i].append (valor)

print()    
print(matriz)
print()

for fila in matriz:
  print("[", end=" ")
  for columna in fila:
    print("{:5}".format(columna), end=" ")
  print("]")

print()

suma = int(input(f"Ingrese cuál columna desea sumar.\nDebe ser un valor igual o menor a {columnas}: "))

sumcol = 0
for fila in matriz:
  sumcol += fila[suma-1]

print(f"La suma de la columna {suma} es: {sumcol}")

print()
suma = int(input(f"Ingrese cuál fila desea sumar.\nDebe ser un valor igual o menor a {filas}: "))

filaescogida = matriz[suma-1]
sumafil = 0

for i in filaescogida:
  sumafil += i

print(f"La suma de la fila {suma} es: {sumafil}")