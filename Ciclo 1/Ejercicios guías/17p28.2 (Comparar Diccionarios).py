"""
Desarrollar un algoritmo que verifique si todas las clave:valor de
un diccionario se encuentran en otro diccionario.
"""

dic1 = {
        "key1":"value1", 
        "key2":"value2", 
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

x = False

for i in dic2:
  if i in dic1:
    if dic2[i] == dic1[i]:
      x = True
    else: 
      x = False
      break
  else: 
    x = False
    break

if x:
  print("Todas las claves y los valores del diccionario 1 están presentes en el diccionario 2.")
else:
  print("Hay diferencias entre las claves y/o valores de ambos diccionarios.")