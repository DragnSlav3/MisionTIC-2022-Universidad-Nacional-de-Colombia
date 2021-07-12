# Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

# PARA LISTAS
lista = [10, 20, 33, 45]
suma = sum(lista) 
print(suma)
longitud = len(lista)
print(longitud)
promedio = sum(lista) / len(lista)
print(promedio)
print(suma/longitud)

print()


arreglo = (
  [[2.3], [3.2], [3.14159]], 
  [[4.4], [5.1], [6.3]], 
  [[7.2], [8.6], [9.7]]
  )

s = 0
elementos = 0

for i in arreglo:
  for j in i:
    for k in j:
      s += k
      elementos += 1

print(elementos, "elementos en el arreglo")
print("La suma de todos los elementos es:", s)
print("El promedio es:", s/elementos)

"""
# AQUÍ ESTOY INTENTANDO QUE LOS DATOS DE ESTAS LISTAS ENTREN POR INPUT

#QUE ENTREN POR LISTAS SEPARADAS Y LUEGO UNIRLAS
listaA = [str(x) for x in input("listaA:").split()]
listaB = [str(x) for x in input("listaB:").split()]
listaC = [str(x) for x in input("listaC:").split()]

listaD = [listaA] + [listaB] + [listaC]
print(listaD)

# DARLE LA FORMA AL ARREGLO Y LLENARLO CON INPUTS SEPARADOS
arreglo = (
  [[input()], [input()], [input()]], 
  [[input()], [input()], [input()]], 
  [[input()], [input()], [input()]]
  )

print(arreglo)

# OTRA SUGERENCIA DEL TUTOR
equipo_A = [str(x) for x in input("equipo_A:")]

#EQUIVALENTE A...

equipo_A = []
equipoA = input()
for x in equipoA:
    equipo_A.append(str(x))
"""