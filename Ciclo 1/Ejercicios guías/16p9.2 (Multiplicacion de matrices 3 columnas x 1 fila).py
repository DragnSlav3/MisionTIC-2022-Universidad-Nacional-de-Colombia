"""
Desarrollar un algoritmo que permita multiplicar dos matrices de
números reales (enteros).
"""

c = [1, 4, 0]
d = [[2], [-1], [5]]
msimple= ((c[0]*d[0][0])+
          (c[1]*d[1][0])+
          (c[2]*d[2][0]))
print(msimple)

largo = len(c)
ciclos = 0
suma = 0
mult = 0

while ciclos < largo:
  mult = 0
  mult = c[ciclos]*d[ciclos][0]
  suma += mult
  ciclos += 1

print(suma)