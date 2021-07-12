"""
Desarrollar una función que reciba dos diccionarios como parámetros
y los mezcle, es decir, que se construya un nuevo diccionario con las
llaves de los dos diccionarios; si hay una clave repetida en ambos
diccionarios, se debe asignar el valor que tenga la clave en el
primer diccionario.
"""
capitales1 = {"Cundinamarca":"BOGOTÁ", 
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
capitales3.update(capitales2)
capitales3.update(capitales1)
print(capitales3)
