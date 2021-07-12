"""
Desarrollar un algoritmo que verifique si todas las clave:valor de
un diccionario se encuentran en otro diccionario.
"""

capitales1 = {"Cundinamarca":"Bogotá", 
              "Antioquia":"Medellín", 
              "Valle del Cauca":"Cali",
              "Santander":"Bucaramanga",
              "Tolima":"Ibagué",
              "Vaupés":"Mitú"}

capitales2 = {"Antioquia":"Medellín", 
              "Cundinamarca":"Bogotá",
              "Boyacá":"Tunja",
              "Atlántico":"Barranquilla"}

capitales3 = {}

for (k, v) in capitales2.items():
  if (k,v) in capitales1.items():
    continue
  else:
    capitales3.update({k:v})

if len(capitales3)!=0:
  print("Una o más parejas clave-valor del diccionario 2 no se encuentran en el diccionario 1.")
else: 
  print("Todas las parejas clave-valor del diccionario 2 se encuentran dentro del diccionario 1.")

print(capitales3)
