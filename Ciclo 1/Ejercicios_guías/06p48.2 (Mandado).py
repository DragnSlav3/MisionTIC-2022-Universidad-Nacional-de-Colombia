def mandado(p, m, h, b):
  panes = p * 300
  leche = m * 3300
  huevos = h * 350
  dinero = b
  return (dinero - (panes + leche + huevos))

a = int(input("panes: "))
b = int(input("leche: "))
c = int(input("huevos: "))
d = int(input("dinero: "))
e = mandado(a, b, c, d)

if e == 0:
    print("El dinero que llevabas era el valor exacto de tu compra.")
if e < 0:
    print(f"Quedas debiendo {e} pesos al tendero.")
if e > 0:
    print(f"Felicidades, te sobraron {e} pesos.")