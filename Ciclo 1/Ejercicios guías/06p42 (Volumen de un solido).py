from math import pi

def vEsfera(r1):
  vol = (pi * (4 / 3)) * r1 ** 3
  return vol

def vCono (r2, h):
  vol = ((pi * (r2 ** 2)) * h) / 3
  return vol

r1 = 3 #float(input("Ingrese el valor correspondiente a r1 (radio de la esfera): "))
r2 = 4 #float(input("Ingrese el valor correspondiente a r2 (radio del cono): "))
h = 9/2 #float(input("Ingrese el valor correspondiente a h (altura del cono): "))

print(vEsfera(r1) + vCono(r2, h))