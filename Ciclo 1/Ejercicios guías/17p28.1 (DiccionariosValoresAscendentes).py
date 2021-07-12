"""
Desarrollar un algoritmo que imprima de manera ascendente los
valores (todos del mismo tipo) de un diccionario.
"""

independencias = {"indCol": 1810, "indUSA": 1776, "indMex": 1821, "indPeru": 1811} # Países y sus años de independencia

print(list(sorted(independencias.values())))

ordenar = list(sorted(independencias.values()))
print(ordenar)