'''
Diseñe un algoritmo que pida un valor entero, y que siga leyendo
valores enteros mientras que alguno de esos valores no represente el
código ASCII de una letra mayúscula en el abc del inglés.
'''

l = int(input("Ingrese un número: "))

# ESTE CÓDIGO LEE ENTEROS MIENTRAS QUE NO CORRESPONDAN CON UNA LETRA MAYUSCULA
while l < 65 or l > 90:
  print("El número ingresado corresponde al carácter:", chr(l))
  l = int(input("Ingrese un número: "))
print("Fin \n")

# ESTE CÓDIGO LEE ENTEROS MIENTRAS QUE CORRESPONDAN CON UNA LETRA MAYÚSCULA
while l >= 65 and l <= 90:
  print("El número ingresado corresponde al carácter:", chr(l))
  l = int(input("Ingrese un número: "))
print("Fin \n")