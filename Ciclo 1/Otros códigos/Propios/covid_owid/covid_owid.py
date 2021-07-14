import json
import requests
import csv
from pprint import pprint

csv_data = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.csv")

json_data = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.json")

json1 = json.loads(json_data.text)

paises = []
sinreportes = []

for k, v in json1.items():
    if k not in paises and k.startswith("OWID") == False:
        paises.append(k)
    if 'total_deaths' not in v["data"][-1]:
        sinreportes.append(k)

conreportes = []
for pais in paises:
    if pais not in sinreportes:
        conreportes.append(pais)

pprint(paises)
print(sinreportes)
print()
print(len(paises))
print()

data = json1["ISR"]["data"][-1]
print("***")
#print(int(json1["AIA"]["data"][-1]['total_deaths']))
print("***")
pprint(data)
print(len(data))
print(type(data))


claves1 = []
for k, v in json1["COL"].items():
  if k not in claves1:
    claves1.append(k)

pprint(claves1)

for pais in conreportes:
    print(f"\nPaís: {json1[pais]['location']} ({pais})")
    print("Población: ", int(json1[pais]['population']))
    print("Total muertes COVID: ", (int(json1[pais]["data"][-1]['total_deaths'])))
    print("Muertes por millón de hab.: ", int((int(json1[pais]["data"][-1]['total_deaths']))/(json1[pais]['population']/1000000)))
    print("Dato oficial: ", int(json1[pais]["data"][-1]['total_deaths_per_million']))
    print(json1[pais]["data"][-1]['date'])

# PENDIENTE PROBAR TRY EXCEPT CON LOS PAÍSES SIN REPORTES
# PENDIENTE GENERAR JSON A PARTIR DE ESTA INFORMACIÓN
# PENDIENTE GENERAR ALGÚN TIPO DE VISUALIZACIÓN