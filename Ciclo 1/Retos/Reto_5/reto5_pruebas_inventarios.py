import inventarios

lista_productos = ["granos","verduras","delicatessen","dulces","papelería","dulces","aseo","granos","aseo"]
print(inventarios.consultar_productos (lista_productos))

lista_indices = [1, 4, 6, 3, 8]
lista_productos = ["aseo", "dulces", "granos", "dulces", "verduras", "dulces", "aseo", "granos", "hogar"]
nombre_producto = "dulces"
print(inventarios.consulta_posiciones_x_producto(lista_indices, lista_productos, nombre_producto))

lista_principal = ["aseo", "verduras", "granos", "dulces", "delicatessen", "enseres"]
lista_sucursal = ["licores", "enseres", "lácteos", "dulces", "carnes", "aseo", "granos"]
print(inventarios.consulta_productos_intercambio(lista_principal, lista_sucursal))

lista_principal = ["aseo", "verduras", "granos", "dulces", "delicatessen", "enseres"]
lista_sucursal = ["licores", "granos", "electrodomésticos", "aseo", "ropa"]
print(inventarios.consulta_max_productos_intercambio(lista_principal, lista_sucursal))