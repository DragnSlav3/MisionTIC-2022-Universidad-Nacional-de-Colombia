"""
Desarrollar un algoritmo que determine la mediana de un arreglo de
enteros. La mediana es el número que queda en la mitad del arreglo
después de ser ordenado.
"""

v = [10, 31, 6, 1, 0, 80, -1]

w = sorted(v)
print(w)
lon = len(v)

print(w[lon//2])