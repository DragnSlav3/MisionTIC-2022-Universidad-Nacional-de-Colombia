# Desarrollar un programa que imprima el cuadrado del número que el usuario ingresa mientras que el número ingresado no sea negativo.

x = int(input("Ingrese un número: "))

while (x >= 0):
  print(x**2)
  x = int(input("Ingrese un número: "))
else:
  print ("\n" "¡Fin del ciclo!")