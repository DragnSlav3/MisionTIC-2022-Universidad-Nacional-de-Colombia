"""
Si un amigo, no tan amigo, me presta K pesos a i pesos de interés
diario, ¿cuánto le pagaré en una semana si el interés es simple?, ¿y
cuánto si el interés es compuesto?.
"""

#INTERÉS COMPUESTO
def iC(ci, p, t): 
  cf = ci * (1 + (p / 100) ) ** t 
  return cf


#INTERÉS SIMPLE
def iS(ci, p, t): 
  cf = ci * (1 + (p / 100) * t) 
  return cf

K = float(input("Ingrese la cantidad de dinero prestada (K): "))
tasa = float(input("Ingrese la tasa de interés diario (i): "))
tiempo = float(7)

print (iC(K, tasa, tiempo))
print (iS(K, tasa, tiempo))