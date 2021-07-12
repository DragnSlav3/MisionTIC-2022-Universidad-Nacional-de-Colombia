'''
Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.
'''

def esTriangulo(a, b, c):
  if a < (b + c) and b < (a + c) and c < (a + b):
    return "Es triángulo."
  else:
    return "No es un triángulo."

a = 7
b = 6
c = 13

print(esTriangulo(a, b, c))