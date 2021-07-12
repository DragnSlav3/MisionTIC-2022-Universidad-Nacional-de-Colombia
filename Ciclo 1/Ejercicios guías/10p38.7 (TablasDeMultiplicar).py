# Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

for i in range(1, 10):
  print(f"\nTabla del {i}")
  for j in range (1, 11):
    print(f"{i} × {j} = {i * j}")