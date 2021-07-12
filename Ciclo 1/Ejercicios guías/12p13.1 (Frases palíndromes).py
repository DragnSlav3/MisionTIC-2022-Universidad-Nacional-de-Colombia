"""
Desarrollar un algoritmo que determina si una cadena de caracteres es
frase palíndrome, esto es, si es palíndrome al eliminarle espacios,
tildes, signos de puntuación y al considerar mayúsculas = minúsculas.
Ejemplos:
"Anula las alas a la luna" es frase palíndrome.
"Dábale arroz a la zorra el abad" es frase palíndrome.
"la tele letal" es frase palíndrome.
"arriba la birra" es frase palíndrome.
"Isaac no ronca así" es frase palíndrome.
"sometamos o matemos" es frase palíndrome.
"Anita, la latina" es frase palíndrome.
"""

frase = "Dábale arroz a la zorra el abad"

frase = frase.lower()
frase = frase.replace("á", "a")
frase = frase.replace("é", "e")
frase = frase.replace("í", "i")
frase = frase.replace("ó", "o")
frase = frase.replace("ú", "u")
frase = frase.replace(" ", "")
frase = frase.replace(",", "")

comp = frase[::-1]

if frase == comp:
  print("La cadena ingresada SÍ es una frase palíndrome.")
else:
  print("La cadena ingresada NO es una frase palíndrome.")

"""
frase = "Dábalé arroz a la zorra el abad"
frase = frase.replace(" ", "")
frase = frase.lower()
lon = 0
flag = True

while flag == True or lon <= len(frase):
  flag = False
  if "á" in frase:
    frase = frase.replace("á", "a")
  if "é" in frase:
    frase = frase.replace("é", "e")
  if "í" in frase:
    frase = frase.replace("í", "i")
  if "ó" in frase:
    frase = frase.replace("ó", "o")
  if "ú" in frase:
    frase = frase.replace("ú", "u")
  lon += 1

print(frase)

"""