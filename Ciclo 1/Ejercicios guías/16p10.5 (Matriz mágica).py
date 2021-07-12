"""
Desarrollar un algoritmo que determine si una matriz es mágica. Se
dice que una matriz cuadrada es mágica si la suma de cada una de
sus filas, de cada una de sus columnas y de cada diagonal es igual.
"""

filas = int(input("Ingrese el número de filas: "))
columnas = filas

matriz = []

for i in range (filas):
  matriz.append ([])
  for j in range (columnas):
    valor = float(input(f"Fila {i+1}, Columna {j+1}: "))
    matriz[i].append (valor)

for fila in matriz:
  print("[", end=" ")
  for columna in fila:
    print("{:5}".format(columna), end=" ")
  print("]")

print()

# SUMANDO LAS COLUMNAS
listacolumnas = []
indicecolumna = 0
flag = False

for fila in matriz:
  for columna in fila:
    if len(listacolumnas) != len(fila):
      listacolumnas.append(columna)
    else:
      listacolumnas[indicecolumna] += columna
    indicecolumna +=1
  indicecolumna = 0
  
for i in listacolumnas:
    for j in listacolumnas:
      if i != j: # AQUI GENERABA
        print("Al sumar cada columna el resultado no es igual.")
        flag = True
        break
    if flag:
      break
 
if flag == False:
  print("Al sumar cada columna el resultado sí es igual.")

# SUMANDO LAS FILAS
sumafila = 0
flag2 = False

for fila in matriz:
  suma = sum(fila)
  if sumafila == 0:
    sumafila = suma
  else:
    if sumafila != suma:
      print("Al sumar cada fila el resultado no es igual.")
      flag2 = True
      break
  
if flag2 == False:  
  print("Al sumar cada fila el resultado sí es igual.") 

# SUMAR DIAGONALES

diagonal1 = 0 # EL ERROR SE ARREGLA INICIANDO VALOR EN 0 Y NO POSICIÓN
diagonal2 = 0 # EL ERROR SE ARREGLA INICIANDO VALOR EN 0 Y NO POSICIÓN
indicediag2 = len(matriz)-1
flag3 = True

for i in range(len(matriz)-1):
  for j in range (len(matriz[i])-1):
    if i == j:
      if indicediag2 != (len(matriz)-1):
        indicediag2 -= 1
      diagonal1 += matriz[i][j] #AQUÍ SE GENERA UN ERROR PORQUE EL PRIMER VALOR SE SUMA A SÍ MISMO
      diagonal2 += matriz[i][indicediag2] #AQUÍ SE GENERA UN ERROR PORQUE EL PRIMER VALOR SE SUMA A SÍ MISMO

if diagonal1 != diagonal2:
  print("Al sumar cada diagonal el resultado no es igual.")
else:
  flag3 = False
  print("Al sumar cada diagonal el resultado sí es igual.")

if flag == False and flag2 == False and flag3 == False:
  print("La matriz ingresada sí es una matriz mágica.")
else:
  print("La matriz ingresada no es una matriz mágica.")