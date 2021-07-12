"""
1 Desarrollar un algoritmo que determine si una cadena de caracteres es
palídrome. Una cadena se dice palndrome si al invertirla es igual a
ella misma.
Ejemplos
"ala" es palídrome.
"amor a roma" es palíndrome.
"anita atina" es palíndrome.
"al sur de Colombia" NO es palíndrome.
"anula las alas a la luna" NO es palíndrome. (Al invertirla: "anul
al a sala sal aluna") no es igual a la original.
"la tele letal" NO es palíndrome.
"""

cadena = "amor a roma"
pali = cadena[::-1]

if cadena == pali:
  print("La cadena ingresada sí es palíndrome.")
else:
  print("La cadena ingresada NO es palíndrome.")