'''
Dado un número real x, construya una función que permita
determinar si el número es positivo, negativo o cero. Para cada caso
se debe imprimir el texto que se especifica a continuación:
Positivo: "El número x es positivo"
Negativo: "El número x es negativo"
Cero (0): "El número x es el neutro para la suma"
'''

s = eval(input("Ingrese un número: "))

def esPositivo(m):
  if m == 0:
    return("el neutro para la suma.")
  elif m > 0:
    return("positivo.")
  else:
    return("negativo.")

print("El número " , end="")
print(s , end=" ")
print("es" , esPositivo(s))