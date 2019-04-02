#********************************
# Este balancedor de cargas tiene en cuenta las posiciones originales.
# Este primer programa es para centros de carga verticales con dos columnas
# Tambien se asumen tres fases
#********************************

import pdb

import itertools
import time
import numpy as np

def balance():
    
    cargas = [90,38,55,50] # Cargas de prueba introducidas manualmente
    #aleatorios = [round(random.gauss(25, 6),1) for _ in range(20)] # Cargas de prueba producidas aleatoriamente
    #pdb.set_trace()
    aleatorios = [32.0, 27.4, 24.1, 33.7, 32.3, 30.1, 30.2, 27.7, 33.1, 33.5, 17.0, 20.8, 15.7, 38.2, 28.6, 21.1, 21.5, 18.2, 21.9, 20.1]
    cargas.extend(aleatorios) #Las cargas deben introducirse en el orden en que están listadas las pastillas
    
#    start = time.time()
    
    def balanceador():
    
        fases_iniciales = [ [cargas[0+x],cargas[2+x],cargas[4+x]] for x in [0,1,6,7,12,13,18,19]]
        fases_finales = [ [] for x in range(int(len(cargas)/3))]
        
        balance_inicial = list(map(sum, zip(*fases_iniciales)))
        balance_final = balance_inicial
        
        
        # El siguiente balanceo es lento, se puede mejorar 
        
        permutaciones = [[] for i in range(len(fases_iniciales))]
        
        for x in range(len(fases_iniciales)):
            permutaciones[x] = list(itertools.permutations(fases_iniciales[x]))
            
        
        for x1 in range(6) :
            for x2 in range(6):
                for x3 in range(6):
                    for x4 in range(6):
                        for x5 in range(6):
                            for x6 in range(6):
                                for x7 in range(6):
                                    for x8 in range(6):
                                
                                         grupo = [permutaciones[0][x1], permutaciones[1][x2], permutaciones[2][x3],
                                                 permutaciones[3][x4], permutaciones[4][x5], permutaciones[5][x6],
                                                 permutaciones[6][x7], permutaciones[7][x8]] 
                                         
                                         balance = list(map(sum, zip(*grupo)))
                                         
                                         if np.std(balance) < np.std(balance_final):
                                             balance_final = balance
                                             fases_finales = grupo
                                            
                                            
        return fases_iniciales, fases_finales, balance_final                   
    
    fases_iniciales, fases_finales, balance_final = balanceador()
    
    ordenados = [ [None,None,None] for x in range(int(len(cargas)/3))]
    
    #pdb.set_trace()
    
    for x in range(len(fases_iniciales)):
        buscar = list(fases_iniciales[x])
        for y in range(3):
            ordenados[x][y] = fases_finales[x].index(buscar[y])
            
    pastillas = [[x+1,2+x+1,4+x+1] for x in [0,1,6,7,12,13,18,19]]
    
    nuevas_pastillas = [[None,None,None] for x in range(int(len(cargas)/3))]
    #pdb.set_trace()
    for x in range(len(fases_iniciales)):
        for y in range(3):
            nuevas_pastillas[x][ordenados[x][y]] = pastillas[x][y]
            
    
    return nuevas_pastillas
#end = time.time()
#transcurrido = end - start
#print()
#print(f'Tiempo transcurrido: {round(transcurrido/60,2)} minutos') 





