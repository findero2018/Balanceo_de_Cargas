
#Forma grupos de carga parecidos entre sí 
import sys
import numpy as np
import random

cargas = [40,38,55,50]
#aleatorios = [round(random.gauss(25, 6),1) for _ in range(20)]
aleatorios = [32.0, 27.4, 24.1, 33.7, 32.3, 30.1, 30.2, 27.7, 33.1, 33.5, 17.0, 20.8, 15.7, 38.2, 28.6, 21.1, 21.5, 18.2, 21.9, 20.1]
cargas.extend(aleatorios)

cargas = np.array(cargas)

total = round(sum(cargas)/3)

margen = 2

def subset_sum(numbers, target, partial=[], grupos=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s >= target-margen and s <= target+margen and len(partial)==8: 
#        print(f'Sum {partial} ={target}')
        grupos.append(partial)
#        print(len(grupos))
        
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 
    
    return grupos

#def subset_sum(numbers, target, partial=[], partial_sum=0):
#    if partial_sum >= target-margen and partial_sum <= target+margen:
#        print(f'Sum {partial} ={partial_sum}')
#        yield partial
#    if partial_sum > target+2:
#        return
#    for i, n in enumerate(numbers):
#        remaining = numbers[i + 1:]
#        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


data = subset_sum(cargas,total)
seen = set()
result = []
for d in data:
    if frozenset(d) not in seen:
        result.append(d)
        seen.add(frozenset(d))
    
primero = result[0]

restante = np.setxor1d(list(cargas),primero)

grupos = []

def subset_sum(numbers, target, partial=[], grupos=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s >= target-margen and s <= target+margen and len(partial)==8: 
#        print(f'Sum {partial} ={target}')
        grupos.append(partial)
#        print(len(grupos))
        
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 
    
    return grupos

data = subset_sum(restante,total)
seen = set()
result = []
for d in data:
    if frozenset(d) not in seen:
        result.append(d)
        seen.add(frozenset(d))

segundo = result[0]

restante = np.setxor1d(list(restante),segundo)

grupos = []

def subset_sum(numbers, target, partial=[], grupos=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s >= target-margen and s <= target+margen and len(partial)==8: 
#        print(f'Sum {partial} ={target}')
        grupos.append(partial)
#        print(len(grupos))
        
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 
    
    return grupos

data = subset_sum(restante,total)
seen = set()
result = []
for d in data:
    if frozenset(d) not in seen:
        result.append(d)
        seen.add(frozenset(d))

tercero = result[0]

print()
print(f'Cargas: {cargas}')
print()
print("Grupos:")
print(primero)
print(f'Suma: {round(sum(primero),2)}')
print(segundo)
print(f'Suma: {round(sum(segundo),2)}')
print(tercero)
print(f'Suma: {round(sum(tercero),2)}')





