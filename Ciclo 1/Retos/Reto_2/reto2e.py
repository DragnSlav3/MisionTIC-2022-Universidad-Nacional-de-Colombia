adminA = "red"
adminB = "fbg"
salas = "rnscgpfzzgphiucgtb"
retorno = ""
acumA = 0
acumB = 0

def funcion (a, b):
    if acumA == acumB:
        if (i == "N"):
          print("N", end="")
        elif (i == "A"):
          print("N", end="")
        elif (i == "B"):
          print("N", end="")

    elif acumA > acumB:
      if (i == "N"):
        print("A", end="")
      elif (i == "A"):
        print("A", end="")
      elif (i == "B"):
        print("A", end="")

    elif acumA < acumB:
      if (i == "N"):
        print("B", end="")
      elif (i == "A"):
        print("B", end="")
      elif (i == "B"):
        print("B", end="")

for i in salas:
  if i in adminA and i in adminB:
    retorno += "N"
  elif i not in adminA and i not in adminB:
    retorno += "N"
  elif i in adminA:
    retorno += "A"
  elif i in adminB:
    retorno += "B"
  
for i in retorno:
  if i == "A":
    acumA += 1
    funcion (adminA, adminB)

  elif i == "B":
    acumB += 1
    funcion (adminA, adminB)

  elif i == "N":
    funcion (adminA, adminB)