import json

with open ("datos.json", "r") as f:
    datos = json.load(f)

# PROBLEMA 1
rendimientoVacasSemana= (((datos[0]["cantidadVacas"])*(datos[0]["areaCorralVacas"]))*((datos[0]["rendimientoVacaLeche"])/(datos[0]["rendimientoVacaTerreno"])))*7
print(f"En total la granja produce {int(rendimientoVacasSemana):,} litros de leche semanales.")

# PROBLEMA 2
sonGallinas = (datos[0]["cantidadAves"])/3
huevos3dXmes = (sonGallinas/2)*10
huevos5dXmes = (sonGallinas/2)*6
print(f"En total la granja produce {int(huevos3dXmes + huevos5dXmes):,} huevos al mes.")

# PROBLEMA 3
# SIN IMPORTAR LA CANTIDAD, EL RESULTADO SIEMPRE SERÁ 1/3

# PROBLEMA 4

precioAlambreReq = (datos[0]["perimetroCorralVacas"] * 5) * datos[0]["precioAlambre"]
precioVarillaReq = (datos[0]["perimetroCorralVacas"] * 8) * datos[0]["precioVarilla"]
precioTablasReq = (datos[0]["perimetroCorralVacas"] * 4) * datos[0]["precioTablas"]

if precioAlambreReq < precioVarillaReq and precioAlambreReq < precioTablasReq:
    print(f"El material más económico para reparar el corral de las vacas es el alambre, cuyo costo total es de ${precioAlambreReq:,}.")
if precioVarillaReq < precioAlambreReq and precioVarillaReq < precioTablasReq:
    print(f"El material más económico para reparar el corral de las vacas es la varilla, cuyo costo total es de ${precioVarillaReq:,}.")
if precioTablasReq < precioAlambreReq and precioTablasReq < precioVarillaReq:
    print(f"El material más económico para reparar el corral de las vacas son las tablas, cuyo costo total es de ${precioTablasReq:,}.")