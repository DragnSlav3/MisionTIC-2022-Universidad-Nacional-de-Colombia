# Un granjero tiene cincuenta animales entre conejos y gallinas. Si la cantidad de patas de los animales es ciento cuarenta, ¿cuántos conejos y cuántas gallinas tiene el granjero?

a = 50 # cantidad de animales
p = 140 # cantidad de patas

# g = gallinas

g = (p - (4 * a)) / 2
g = abs(int(g))

# c = conejos
c = a - g

g = str(g)
c = str(c)

print ("El granjero tiene " + g + " gallinas y " + c + " conejos.")