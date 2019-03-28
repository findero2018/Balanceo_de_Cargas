#**************************************************
#PropÃ³sito:  Genera grupos con una suma deseada.
#Inputs:     numbers: lista a agrupar.
#Regresa:    grupos: grupos que suman el mismo valor.
#Utiliza:    
#**************************************************

def grupos_suma(numbers, target, margen, partial=[], grupos=[]):
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
        grupos_suma(remaining, target, margen, partial + [n], grupos) 
    
    return grupos