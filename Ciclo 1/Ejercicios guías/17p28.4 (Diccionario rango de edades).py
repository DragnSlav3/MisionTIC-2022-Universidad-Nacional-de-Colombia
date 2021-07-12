"""
Desarrollar un programa que, dada una listas de personas, cada
persona representada como el siguiente ejemplo:
{"nombres":"Pedro Julio", "apellidos":"Tristán Merchán",
"edad":101}, imprima los nombres y apellidos de las personas que
están en un rango de edades.
"""

listapersonas = [
  {"nombres":"Pedro Julio", 
  "apellidos":"Tristán Merchán",
  "edad":101},

  {"nombres":"Manuela",
  "apellidos":"Padrón",
  "edad":35},

  {"nombres":"Jordi",
  "apellidos":"Bermejo",
  "edad":15},

  {"nombres":"Micaela",
  "apellidos":"Solís",
  "edad":38},

  {"nombres":"María Dionisia",
  "apellidos":"Hernández",
  "edad":43},

  {"nombres":"Itziar Santiago",
  "apellidos":"Arteaga",
  "edad":29},

  {"nombres":"Camilo",
  "apellidos":"Quiróz",
  "edad":21},

  {"nombres":"Teófilo",
  "apellidos":"Sierra",
  "edad":76},

  {"nombres":"Ainara Karina",
  "apellidos":"Orozco",
  "edad":33},

  {"nombres":"Ikrán",
  "apellidos":"Kaúr",
  "edad":35},
  ]

for persona in listapersonas:
  if (persona.get("edad")) >= 30 and (persona.get("edad")) <=40:
    print(f'{persona.get("nombres")} {persona.get("apellidos")} ({persona.get("edad")} años)')
