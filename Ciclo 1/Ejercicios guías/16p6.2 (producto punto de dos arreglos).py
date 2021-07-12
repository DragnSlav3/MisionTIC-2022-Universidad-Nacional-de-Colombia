"""
Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño. 
"""
v = [-7.2, 4, 3]
w = [1, -1, 8]
largolista = len(v)
x = 0

for i in range (largolista):
  x = x + (v[i] * w[i])

print(x)