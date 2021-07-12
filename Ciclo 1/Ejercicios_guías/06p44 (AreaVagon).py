from math import pi

def areaRectangulo(b, a):
    return b * a

def areaCirculo(r):
 return pi * r ** 2

b = float(input("Ingrese el ancho del rectángulo: "))
a = float(input("Ingrese la altura del rectángulo: "))
r = float(input("Ingrese el radio de las ruedas: "))

areaDosRuedas = areaCirculo(r) * 2
areaTotalVagon = str(areaRectangulo(b, a) + areaDosRuedas)

print("El área total del vagón es: " + areaTotalVagon)