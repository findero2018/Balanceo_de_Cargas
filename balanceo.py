#**************************************************
#Propósito:  A partir de una lista, produce grupos del mismo
#            tamaño cuya suma total es aproximadamente la mima.
#Inputs:     Se especifica la lista de cargas y cuántos grupos de necesitan.
#Regresa:    Imprime los grupos formados y su suma.
#Utiliza:    agrupador.py
#**************************************************

import numpy as np
import random
from agrupador import grupos_suma

cargas = [40,38,55,50] # Cargas de pruba introducidas manualmente
#aleatorios = [round(random.gauss(25, 6),1) for _ in range(20)] # Cargas de prueba producidas aleatoriamente

aleatorios = [32.0, 27.4, 24.1, 33.7, 32.3, 30.1, 30.2, 27.7, 33.1, 33.5, 17.0, 20.8, 15.7, 38.2, 28.6, 21.1, 21.5, 18.2, 21.9, 20.1]
cargas.extend(aleatorios)

cargas = np.array(cargas)       # Esta es la lista de cargas. 
cargas_original = cargas
margen = 2      # Margen de variación en la suma de los grupos.                        
total = round(sum(cargas)/3)    # El valor deseado para la suma de los grupos. 
numero_grupos = 3

# Se crean los grupos

resultados = [None]*numero_grupos

for i in range(1,numero_grupos):

    data = grupos_suma(cargas,total)    
    seen = set()
    result = []
    for d in data:                      # Se eliminan los grupos que solo sean permutaciones de otro. 
        if frozenset(d) not in seen:
            result.append(d)
            seen.add(frozenset(d))
        
    resultados[i] = result[0]                 # Se van a crean muchos grupos que cumplan con la suma, solo se toma el primero

    cargas = np.setxor1d(list(cargas),resultados[i])    # Cargas sin acomodar aún.

print()
print(f'Cargas: {cargas_original}')
print()
print("Grupos:")

for i in range(1,numero_grupos):
    print(resultados[i])
    print(f'Suma: {round(sum(resultados[i]),2)}')