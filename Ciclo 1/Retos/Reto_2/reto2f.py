adminA = "pnja" #input()
adminB = "aesz" #input()
salas = "zesdljjyspclpwoaumqen" #input()
contA = 0
contB = 0
resultado = ""

def evaluador(a, b):
  if contA == contB:
      return ("N")
  elif contA > contB:
      return ("A")
  elif contA < contB:
      return ("B")

for i in salas:
  if i in adminA and i in adminB:
    resultado += evaluador(contA, contB)
  elif i not in adminA and i not in adminB:
    resultado += evaluador(contA, contB)
  elif i in adminA:
    contA += 1
    resultado += evaluador(contA, contB)
  elif i in adminB:
    contB+= 1
    resultado += evaluador(contA, contB) 
print(resultado)