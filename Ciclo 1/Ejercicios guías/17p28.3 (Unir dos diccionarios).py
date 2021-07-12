"""
Desarrollar una función que reciba dos diccionarios como parámetros
y los mezcle, es decir, que se construya un nuevo diccionario con las
llaves de los dos diccionarios; si hay una clave repetida en ambos
diccionarios, se debe asignar el valor que tenga la clave en el
primer diccionario.
"""

dic1 = {
        "key1":50, 
        "key2":"¿Valor?", 
        "key3": "value3", 
        "key4":"value4", 
        "key5":"value5", 
        "key6": "value6"
        }

dic2 = {
        "key2":"value2", 
        "key1":"value1", 
        "key3": "value3"
        }


def funcion (a, b):
  x = {}
  for i in a:
    if i in b:
      x[i]=a[i]
    else: 
      x[i]=a[i]
  for i in b:
    if i not in a:
      x[i]=b[i]     
  return x

print(funcion(dic1, dic2))

print()

prueba = funcion(dic1, dic2)

for k, v in prueba.items():
  print(f"Llave: {k} | Valor: {v}")