'''
Dada una cadena de longitud 1, determine si el código ASCII de
primera letra de la cadena es par o no. Ayuda: utilice la función
ord(<carácter>) de Python que retorna el código ASCII de una
cadena de longitud 1.
'''

x = str(input("Ingrese UN carácter cualquiera: "))
x = ord(x)

def esPar(l):
  if l % 2 == 0:
    return " es par."
  else:
    return " no es par."

print("El caracter ingresado corresponde al número ASCII " + str(x) + " el cual" + esPar(x))