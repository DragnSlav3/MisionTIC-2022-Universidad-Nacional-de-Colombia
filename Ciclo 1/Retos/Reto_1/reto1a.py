def categoria(l):
  if l <= 20:
    print("uno")
  elif l > 20 and l <= 30:
    print("dos")
  elif l >= 31 and l <=50:
    print("tres")
  else: print("cuatro")

Papeleria = int(input())
SalidaHogar = (Papeleria * 2) + 4
SalidaLimpieza = int ((Papeleria + SalidaHogar) / 5)

print (Papeleria, SalidaHogar, SalidaLimpieza)
categoria(SalidaLimpieza)