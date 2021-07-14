import json
import requests
import csv
from pprint import pprint

csv_data = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.csv")

json_data = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.json")

json1 = json.loads(json_data.text)

claves = []

for k, v in json1.items():
  if k not in claves and k.startswith("OWID") == False:
    claves.append(k)

pprint(claves)
print()
print(len(claves))
print()
pprint(json1["COL"]["data"][-1])
print(len(json1["COL"]["data"][-1]))
print(type((json1["COL"]["data"][-1])))



claves1 = []
for k, v in json1["COL"].items():
  if k not in claves1:
    claves1.append(k)

pprint(claves1)

for pais in claves:
    print(f"\nPaís: {json1[pais]['location']} ({pais})")
    print("Población: ", int(json1[pais]['population']))
    print("Total muertes COVID: ", (int(json1[pais]["data"][-1]['total_deaths'])))