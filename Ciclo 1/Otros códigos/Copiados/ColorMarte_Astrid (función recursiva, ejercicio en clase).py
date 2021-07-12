def color_marte(n=3):
  entrada=input("Ingrese color: ")
  
  if entrada.lower() =="Rojo".lower():
    print("Ganaste")
  elif n == 1:
      print("Perdiste :(")
  else:
    color_marte(n-1)

color_marte() 

# Código de Stefany Gordillo