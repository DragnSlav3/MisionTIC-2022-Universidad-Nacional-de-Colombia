"""
Hacer un algoritmo que deje al final de un arreglo de núumeros todos
los ceros que aparezcan en dicho arreglo.
Ejemplo
vector original: [1; 6; 0; 7; 3; 8; 0; 2; 11]
vector salida: [1; 6; 7; 3; 8; 2; 11; 0; 0]

vector original: [0; 11; 36; 10; 0; 17; 23; 81; 0; 0; 12; 11; 0]
vector salida: [11; 36; 10; 17; 23; 81; 12; 11; 0; 0; 0; 0; 0]
"""

vo = [0, 11, 36, 10, 0, 17, 23, 81, 0, 0, 12, 11, 0]
vs = []
v0 = []

for i in vo:
  if i != 0:
    vs.append(i)
  else:
    v0.append(i)

print(vs+v0)
