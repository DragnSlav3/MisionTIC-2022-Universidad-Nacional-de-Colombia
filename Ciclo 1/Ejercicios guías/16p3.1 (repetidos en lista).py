lista = [1, 2, 3, 4, 5, 2, 4]

# UNA MANERA
ci = 0
cj = 0
resultado = ""

for i in lista:
  for j in lista:
    if ci != cj:
      if lista[ci] == lista[cj]:
        resultado = (f"{lista[ci]} repetido")
        break
      else:
        resultado = "no hay repetidos"
    cj += 1
  ci += 1
  cj = 0
    

print(resultado)

print()

# OTRA MANERA

unicos=[]
repetidos=[]

for i in lista:
  if i not in unicos:
    unicos.append(i)
  else:
    if i not in repetidos:
      repetidos.append(i)
  
if repetidos != []:
  print(f"Hay repetidos, y son: {repetidos}")
else:
  print("No hay ningún número repetido en la lista.")