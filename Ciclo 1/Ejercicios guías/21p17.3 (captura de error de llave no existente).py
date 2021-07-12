"""
Capture la excepción cuando se trata de obtener una llave que no se
encuentra en un diccionario y muestre el mensaje
Intenta acceder una llave que no está en el diccionario
"""

def main():
  try:
    dict = {'James': 'Java', 'Dennis' : 'C', 'Das':'Python'}
    print(dict['Ada'])
  except Exception as e:
    print(f"Intenta acceder a una llave que no está en el diccionario. \n{e}\n{type(e)}")

main()