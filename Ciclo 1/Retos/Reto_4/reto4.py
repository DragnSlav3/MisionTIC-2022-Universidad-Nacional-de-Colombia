import json
diccionario1 = input()
lista = input().split (" ")
diccionario = json.loads(diccionario1)

precios = 0
elementos = ""

for i in lista:
  if i in diccionario:
    elementos += i + " "
    for k, v in diccionario.items():
      if k == i:
        precios += v
    
print (precios)
print (elementos)