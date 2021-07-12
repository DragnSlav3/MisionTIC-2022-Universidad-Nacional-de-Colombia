"""
Desarrollar un programa que determine si en una lista se encuentra
una cadena de caracteres con dos o más vocales. Si la cadena existe
debe imprimirla y si no existe debe imprimir 'No existe'.
"""

lista = ['Murciélago', 'Python', 'Sol', 'casa', 'fruta']
vocales = ['a', 'e', 'i', 'o', 'u']
cuentavocales = 0

for i in lista:
  for j in i:
    if j in vocales:
      cuentavocales += 1
    else:
      continue
  if cuentavocales >= 2:
    print(i)
  else:
    print("no existe")
  cuentavocales = 0
