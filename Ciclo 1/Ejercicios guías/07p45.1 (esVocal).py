'''
Dado un número entero, determinar si ese número corresponde al
código ASCII de una vocal minúscula. Ayuda: utilice la función
chr(<número>) de Python que retorna el carácter ASCII
correspondiente al número entero en el cual se evalúe la función.
'''
h = int(input("Escriba un número entero: "))
h = chr(h)

def esVocal(n):
  yes = " sí es una vocal minúscula."
  if n == "a":
    valor = yes
  elif n == "e":
    valor = yes
  elif n == "i":
    valor = yes
  elif n == "o":
    valor = yes
  elif n == "u":
    valor = yes
  else:
    valor = " no es una vocal minúscula."
  return valor

print (h + esVocal(h))