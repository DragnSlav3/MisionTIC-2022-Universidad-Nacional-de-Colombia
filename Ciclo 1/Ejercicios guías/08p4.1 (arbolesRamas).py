'''
Si en la UN están podando árboles y cada rama tiene P hojas, y a
cada árbol le quitaron K ramas, cuántos árboles se deben podar para
obtener T hojas?.
'''

T = int(input("¿Cuántas hojas deseas recolectar?: "))
K = int(input("¿Cuántas ramas le quitaron a cada árbol?: "))
P = int(input("¿Cuántas hojas tenía cada rama?: "))

valor = int(T/(K*P))

print("Para obtener", str(T) , "hojas, debes podar", str(valor), end=" ")
print("árboles.")