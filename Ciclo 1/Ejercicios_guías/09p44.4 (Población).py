'''
En 2022 el país A tendrá una población de 25 millones de habitantes
y el país B de 18,9 millones. Las tasas de crecimiento anual de la
población serán de 2% y 3% respectivamente. Desarrollar un
algoritmo para informar en que año la población del país B superará a
la de A.
'''

a = 25_000_000
b = 18_900_000
year = 2022

while a > b:
  a = a + (a * 0.02)
  b = b + (b * 0.03)
  year += 1
  print(a, b, year, sep="\t")