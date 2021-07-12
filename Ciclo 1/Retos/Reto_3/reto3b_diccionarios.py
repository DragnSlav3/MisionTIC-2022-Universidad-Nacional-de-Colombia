# "pan pan ajo coco sal uva uva uva pera pan ajo ajo"
# "ajo coco coco coco uva pera ajo ajo"
entrada = input().split(" ")

diccionario = {}
elementoanterior = ""
salidaelementos = str(entrada[0]) + " "
salidacantidades = ""
ciclos = 0

for i in entrada:
    if i != elementoanterior and elementoanterior != "":
        salidaelementos+= str(i) + " "
        salidacantidades+=str(diccionario[elementoanterior]) + " "
        diccionario[elementoanterior]=0
    
    if i in diccionario:
        diccionario[i]+=1
        elementoanterior=i
        if ciclos == len(entrada)-1:
            salidacantidades+=str(diccionario[elementoanterior])
    else:
        diccionario[i]=1
        elementoanterior=i
        if ciclos == len(entrada)-1:
            salidacantidades+=str(diccionario[elementoanterior])
    ciclos+=1

print(salidaelementos)
print(salidacantidades)
