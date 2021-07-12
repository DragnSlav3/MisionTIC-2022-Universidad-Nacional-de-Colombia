'''
Dado un carácter, construya un programa en Python para determinar
si el carácter es un dígito o no.
'''

j = input("Ingrese UN carácter cualquiera: ")

if j.isdigit():
    print("Es un dígito.")
else:
    print("No es un dígito")

# Otra alternativa usando valores ASCII

def esDigito(x): # 48 a 57
  x = (ord(x))
  if x <= 57 and x >= 48:
    return ("Es un dígito.")
  else:
    return ("No es un dígito.")

print(esDigito(j))