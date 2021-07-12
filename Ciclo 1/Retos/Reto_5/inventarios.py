def consultar_productos (lista_productos):
    nueva_lista = []
    for producto in lista_productos:
        if producto not in nueva_lista:
            nueva_lista.append(producto)
    return nueva_lista

def consulta_posiciones_x_producto(lista_indices, lista_productos, nombre_producto):
    indices_coincidentes = []
    for i in range(len(lista_productos)):
        if lista_productos[i] == nombre_producto:
            indices_coincidentes.append(i)

    lista_salida = []
    for i in lista_indices:
        for j in indices_coincidentes:
            if i == j:
                lista_salida.append(i)
    return lista_salida

def consulta_productos_intercambio(lista_principal, lista_sucursal):
    salida_intercambio = []
    for producto in lista_principal:
        if producto not in lista_sucursal:
            salida_intercambio.append(producto)
    return salida_intercambio

def consulta_max_productos_intercambio(lista_principal, lista_sucursal):
    lista_a = []
    lista_b = []
    salida = 0
    for i in lista_principal:
        if i not in lista_sucursal:
            lista_a.append(i)

    for i in lista_sucursal:
        if i not in lista_principal:
            lista_b.append(i)

    if len(lista_a) < len(lista_b):
        salida = (len(lista_a))
    else:
        salida = (len(lista_b))
    return salida