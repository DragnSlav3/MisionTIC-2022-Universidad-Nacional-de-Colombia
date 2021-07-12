import random

#Imprime el tablero de triqui
def imprimir(A):
  for i in range(len(A)):
    if i>0:
      print('-+-+-')
    for j in range(len(A[i])):
      if j>0:
        print('|',end='')
      print(A[i][j],end='')
    print()
  print('================')

# Crea el tablero incial de triqui
def inicial():
  return [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

# Determina las casillas que están vacias en el tablero
def vacias(A):
  v = []
  for i in range(3):
    for j in range(3):
      if A[i][j]==' ':
        v.append((i,j))
  return v

# Calcula el movimiento del jugador
def jugar(A, jugador):
  v = vacias(A)
  i,j = v[random.randrange(len(v))] # de manera aleatoria
  A[i][j] = jugador
  return A

# Determina si el jugador ganó o no
def ganador(A, jugador):
  # Revisa diagonal principal
  if (A[0][0]==jugador and A[1][1]==jugador and A[2][2]==jugador):
    return True
  # Revisa diagonal contraria  
  if (A[0][2]==jugador and A[1][1]==jugador and A[2][0]==jugador):
    return True
  
  for i in range(3):  
    # Revisa la i-ésima fila
    if (A[i][0]==jugador and A[i][1]==jugador and A[i][2]==jugador):
      return True
    # Revisa la columna i-ésima  
    if (A[0][i]==jugador and A[1][i]==jugador and A[2][i]==jugador):
      return True
  return False  

# Programa principal
def main():
  tablero = inicial()
  jugador = 'X'
  imprimir(tablero)
  for i in range(9):
    tablero = jugar(tablero,jugador)
    imprimir(tablero)
    if ganador(tablero,jugador):
      print('El ganador es ', jugador)
      return 
    if jugador=='X':
      jugador='O'
    else:
      jugador='X'
  print('Empate')

main()