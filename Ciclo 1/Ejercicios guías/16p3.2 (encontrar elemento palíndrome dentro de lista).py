"""
Desarrollar un programa que determine si un elemento de una lista es
una cadena palíndrome. Si la cadena existe debe imprimirla y si no
existe debe imprimir 'No existe'.
"""

lista = ["elemento 1", 21, 121, "zorro", "ala", True, False, "amor a roma"]
nuevalista=[]

for i in lista:
  i = str(i)
  nuevalista.append(i)

j = 0

for i in nuevalista:
  j = i[::-1]
  if i == j:
    print(f"{i} es un elemento palíndrome en la lista.")
  else:
    print("No existe")