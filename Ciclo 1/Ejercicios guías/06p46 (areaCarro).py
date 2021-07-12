from math import pi

def areaRectangulo(b, a):
    return b * a

def areaCirculo(r):
 return pi * r ** 2

b1 = float(input("Ingrese el ancho del rectángulo 1: "))
a1 = float(input("Ingrese la altura del rectángulo 1: "))
b2 = float(input("Ingrese el ancho del rectángulo 2: "))
a2 = float(input("Ingrese la altura del rectángulo 2: "))
r1 = float(input("Ingrese el radio de la rueda 1: "))
r2 = float(input("Ingrese el radio de la rueda 2: "))

areaTotalCarro = str(areaRectangulo(b1, a1) + areaRectangulo(b2, a2) + areaCirculo(r1) + areaCirculo(r2))
print("El área total del carro es: " + areaTotalCarro)