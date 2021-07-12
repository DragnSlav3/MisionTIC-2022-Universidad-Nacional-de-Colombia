from IPython.display import clear_output
import matplotlib.pyplot as plt
from random import randrange
from numpy import ones
from time import sleep

# Tamaño de la imagen a generar
N = 300
# Valores necesarios
# Vertices de la figura
VERTICES = [[30,150],[270,30],[270,270]]
#VERTICES = [[30,30],[30,270],[270,270],[270,30]]
#VERTICES = [[20,150],[120,280],[270,238],[270,62],[120,20]]
# Punto inicial en la mitad de la imagen
p = [150,150]
# Inicia imagen en blanco (1)
# Pinta la imagen
imagen = ones((N, N))
plt.imshow( imagen, cmap='gray', vmin=0, vmax=1)
plt.show()
clear_output(wait=True)
# Genera puntos siguiendo la idea de Sierpinski
for i in range(10000):
  v = randrange(len(VERTICES))
  p[0] = (p[0]+VERTICES[v][0])//2
  p[1] = (p[1]+VERTICES[v][1])//2
  #p[0] = p[0]*35//100+VERTICES[v][0]*65//100
  #p[1] = p[1]*35//100+VERTICES[v][1]*65//100
  # Vuelve negro el punto (0 es negro)
  imagen[p[0]][p[1]] = 0 
# Pinta la imagen final
plt.imshow(imagen, cmap='gray', vmin=0, vmax=1)
plt.show()
clear_output(wait=True)