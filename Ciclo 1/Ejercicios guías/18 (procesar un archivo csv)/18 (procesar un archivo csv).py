"""
Dado el archivo de texto sales/SalesJan2009.csv, procese el archivo
para obtener las compras realizadas en un país dado. 
Dado el archivo de texto sales/SalesJan2009.csv, procese el archivo
para obtener las compras realizadas con un medio de pago dado.
"""

import csv

country = input("Ingrese el nombre del país del cual quiere obtener los datos: ")
contador1 = 0
with open("files\SalesJan2009.csv") as f:
  lista = csv.DictReader(f, delimiter=',')
  for i in lista:
    if i["Country"] == country:
      contador1 += 1
print(contador1)

payment = input("Ingrese el medio de pago del cual quiere obtener los datos: ")
contador2 = 0
with open("files\SalesJan2009.csv") as f:
  lista = csv.DictReader(f, delimiter=',')
  for i in lista:
    if i["Payment_Type"] == payment:
      contador2 += 1
print(contador2)