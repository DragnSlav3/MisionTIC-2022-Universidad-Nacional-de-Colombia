"""
El número de contagiados de Covid-19 en el país de NuncaLandia se
duplica cada día. Hacer un programa que diga el número total de
personas que se han contagiado cuando pasen D días a partir de hoy,
si el número de contagiados actuales es C.
"""

def tContagios(d, c):
  return c * (2 ** (d)-1)

d = int(input("Ingrese el número D de días a partir de hoy: "))
c = int(input("Ingrese el número C de contagiados actualmente: "))

total = str(tContagios(d, c))

print ("La cantidad de contagiados en NuncaLandia después de " + str(d) + " días a partir de hoy son: " + total + " personas")

# ¿Este ejercicio es igual al del origen del ajedrez de la guía 02 p.12 ?