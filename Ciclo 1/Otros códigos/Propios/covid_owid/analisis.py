# En este código agregué información posterior a la obtenida preliminarmente, separé los datos en dos archivos separados e hice
# su conversión a Excel. Hice uso de Pandas para hacer suma básica de columnas, y al final quise hacer un gráfico con MatPlotLib,
# pero aún me falta aprender más sobre su uso. La visualización final la hice en Excel. :)

import json
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

with open ("jsonsalida.json", "r") as f:
    data = json.load(f)


diccionario = {"abreviacion":"JW/WT", "nombre": "Jehova's Witnesses", "poblacion":8424185, "total_muertes":19000, "muertes_x_millon":2255, "fecha":"2021-07-09"}
data.append(diccionario)

poblacionmayor = []
poblacionmenor = []

for i in data:
  if i["poblacion"] >= 8_400_000:
    poblacionmayor.append(i)
  if i["poblacion"] <= 9_000_000:
    poblacionmenor.append(i)

print(len(poblacionmayor))
print(len(poblacionmenor))

with open ("poblacionmayor.json", "w") as pmayor:
  json.dump (poblacionmayor, pmayor, indent=4)

with open ("poblacionmenor.json", "w") as pmenor:
  json.dump (poblacionmenor, pmenor, indent=4)

pd.read_json("poblacionmayor.json").to_excel("poblacionmayor.xlsx")
pd.read_json("poblacionmenor.json").to_excel("poblacionmenor.xlsx")
pd.read_json("jsonsalida.json").to_excel("total.xlsx")

df = pd.DataFrame(poblacionmayor)
# print(df)

print(df.columns.values)
print()
poblacion_mundo = (df["poblacion"].sum())
muertes_mundo = (df["total_muertes"].sum())
muertes_x_millon_mundo = int(muertes_mundo / (poblacion_mundo/1_000_000))

print(f"Población mundial: {poblacion_mundo:,}")
print(f"Total de muertes en el mundo: {muertes_mundo:,}")
print(f"Muertes por millón en el mundo: {muertes_x_millon_mundo:,}")

import numpy as np


abreviaciones = []
muertes = []
for i in poblacionmayor:
  abreviaciones.append(i["abreviacion"])
  muertes.append(i["muertes_x_millon"])

muertes1 = np.array(muertes)
x = np.array(abreviaciones)

threshold = 517

above_threshold = np.maximum(muertes1 - threshold, 0)
below_threshold = np.minimum(muertes1, threshold)

fig, ax = plt.subplots()
ax.bar(x, below_threshold, 0.35, color="g")
ax.bar(x, above_threshold, 0.35, color="r",
        bottom=below_threshold)



plt.figure(figsize=(100, 10))
plt.bar(x, muertes1)
plt.xticks(rotation=90)
ax.plot([0., 4.5], [threshold, threshold], "k--")
plt.show()