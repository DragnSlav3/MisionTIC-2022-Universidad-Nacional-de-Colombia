entrada = "pan pan ajo coco sal uva uva uva pera pan ajo ajo".split(" ")

entrada.append("elemento")
repeticiones = 0
pos_ant=""
listaelementos = []
listarepeticiones = []

for i in entrada:
    if i == pos_ant:
        repeticiones += 1
        pos_ant = i
    else:
        listaelementos.append(i)
        listarepeticiones.append(repeticiones)
        repeticiones = 1
        pos_ant = i
    
listaelementos.pop(-1)
listarepeticiones.pop(0)

print(listaelementos)
print(listarepeticiones)