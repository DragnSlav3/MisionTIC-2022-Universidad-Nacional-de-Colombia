"""
Desarrollar un algoritmo que reciba dos cadenas de caracteres y
determine si la primera está incluida en la segunda. Se dice que una
cadena está incluida en otra, si todos los caracteres (con repeticiones)
de la cadena está en la segunda cadena sin tener en cuenta el orden
de los caracteres.
Ejemplos
La cadena "prosa" está incluida en la cadena "la profesora de idiomas".
La cadena "pepito" no esta incluida en la cadena 
"un pedazo de tierra", ya que le falta una "p".
La cadena "pepito" si esta incluida en la cadena "tijeras o papel".
"""

c1 = "prosa"
c2 = "la profesora de idiomas"
x = 0
y = 0
incluida = False

for i in c1:
  x = c1.count(i)
  y = c2.count(i)
  if x <= y:
    incluida = True
  else:
    incluida = False
    break

if incluida == True:
  print("La cadena 1 SÍ está incluída en la cadena 2.")
else:
  print("La cadena 1 NO está incluída en la cadena 2.")