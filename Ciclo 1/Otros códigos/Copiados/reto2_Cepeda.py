salas1="pnja"
salas2="aesz"
salas_est = "zesdljjyspclpwoaumqen"
bonoA = 0
bonoB = 0
bonoN = 0
cont = 0
centinela = 0
est=salas_est
lon_cad = len(est)

while centinela or cont < lon_cad:
  centinela = False
  for i in range (0, lon_cad):
    listado = est[i]
    if listado in salas1:
      bonoA = bonoA+1
    if listado in salas2:
      bonoB = bonoB+1
    else:
      bonoN = bonoN+1
    if bonoA > bonoB:
      bono = "A"
    if bonoB > bonoA:
      bono = "B"
    if bonoA == bonoB:
      bono = "N"
    bonos = "".join(bono)
    cont = cont+1
    print(bonos, end="")