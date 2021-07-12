"""
Desarrollar un algoritmo que calcule el producto directo de dos
arreglos de números reales de igual tamaño. 
"""

v = [3, 5, 6, 9]
w = [4, 3, 4, 9]

largolista = len(v)

x = []

for i in range (largolista):
  x.append (v[i] * w[i])

print(x)
