from IPython.display import clear_output
import matplotlib.pyplot as plt
from random import randrange
from numpy import ones
from time import sleep

def iniciar(SIZE):
  imagen = ones((SIZE,SIZE))
  for i in range(SIZE*SIZE//10):
    x = randrange(SIZE)
    y = randrange(SIZE)
    imagen[y][x] = 0.0
  return imagen

def viva(imagen, y, x):
  return imagen[y][x] == 0.0

def vecinos(imagen, SIZE, y, x):
  c = 0
  for i in range(-1,2):
    vy = (y + i + SIZE)%SIZE
    for j in range(-1,2):
      vx = (x + j + SIZE)%SIZE
      if (y!=vy or x!=vx) and viva(imagen,vy,vx):
        c += 1
  return c

def actualiza(imagen, SIZE):
  nueva = imagen.copy()
  for y in range(SIZE):
    for x in range(SIZE):
      c = vecinos(imagen,SIZE,y,x)
      if viva(imagen,y,x):
        if c<2 or c>3:
          nueva[y][x] = 1.0
      else:
        if c==3:
          nueva[y][x] = 0.0
  return nueva

SIZE = 200
imagen = iniciar(SIZE)
plt.imshow( imagen, cmap='gray', vmin=0, vmax=1)
plt.show()
clear_output(wait=True)
for i in range(1000):
  imagen = actualiza(imagen,SIZE)
  plt.imshow( imagen, cmap='gray', vmin=0, vmax=1)
  plt.show()
  clear_output(wait=True)