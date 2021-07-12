"""
Si pido prestados P cantidad de pesos para pagarlos en dos meses,
si el interés del préstamo es del 3%. ¿Cuánto se debe pagar al 
final del segundo mes si el interés es compuesto mensualmente?.
"""

def iC(ci, p, t): # Capital Inicial (ci), Porcentaje (p), Tiempo (t)
  cf = ci * (1 + (p / 100)) ** t
  return cf

P = float(input("Ingrese la cantidad P de dinero prestada: "))
tasa = float(3)
tiempo = float(2)

print (iC(P, tasa, tiempo))