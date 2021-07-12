"""
Capture la excepción para evitar que un programador sume una
cadena de texto a un número y muestre el mensaje
"Los tipos de datos no cuadran para hacer la operación"
"""

def operar(a, b):
  return a + b



def main():
  try:
    a = int(input("Escribe un número: "))
    b = 'hola'
    operar(a, b)
  except Exception as e:
    print(f"Error: Los tipos de datos no cuadran para hacer la operación. \n{e}\n{type(e)}")

main()