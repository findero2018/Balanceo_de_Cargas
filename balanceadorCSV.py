#**********************************
# Cuando se tiene un archivo con columnas correspondientes a cada carga
# se utiliza este archivo
#
# Para que funcione automáticamente, se requiere que el CSV esté correctamente ordenado,
# o sea, que la primera columna corresponda a la primera pastilla, etc. 
#*******************************************


import pandas as pd
import balanceoMinimizado as bm

carpeta ='D:/Findero/Analisis/Marissa/Datos'
archivo = 'DATALOG_FND3C001_TM09_P066_22mar19_TBD.CSV'
filename = carpeta +'/'+ archivo

df = pd.read_csv(filename)

no_de_columnas = 12

columnas = [f'L{i+1}' for i in range(no_de_columnas)] 

df['Total'] = df[columnas].sum(axis = 1)    #Suma las columnas

cuartil = df.Total.quantile(0.75)

cuartil_mayor = df[df['Total'] > cuartil ].Total

cuartil_mayor = cuartil_mayor.values

promedio = round(cuartil_mayor.mean(),2)

idx = df['Total'].sub(promedio).abs().idxmin()

cargas = df.loc[idx].values

cargas = list(cargas[3:])

balanceo = bm.balanceador(cargas)

print(balanceo)




