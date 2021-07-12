"""
Diseñe una función que calcule la cantidad de carne de aves en kilos
si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6
kilos, 7 kilos y 1 kilo respectivamente.
"""

def CalcularCarne (N, M, K):
  gallinas = N * 6
  gallos = M * 7
  pollitos = K
  return (gallinas + gallos + pollitos)

gallinas = int(input("Cuántas gallinas: "))
gallos = int (input("Cuántos gallos: "))
pollitos = int (input("Cuántos pollitos "))

print("El total de carne son:", end=" ")
print(CalcularCarne (gallinas, gallos, pollitos), "kilos.")