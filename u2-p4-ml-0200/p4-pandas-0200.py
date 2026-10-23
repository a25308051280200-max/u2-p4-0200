import pandas as pd 
import numpy as np 
# Alejandra Rivera Valenzuela NC 0200
n_filas = 5
n_columnas = 5
tag_columna=tuple('ABCDE') # etiquetas para las columnas  de una tupla 
print(tag_columna)
matriz=np.random.randint(1,6, size=(n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("con numeros aletorios comprendidos entre 1 y 10")
print(matriz)
# la variable df es DataFrame
df = pd.DataFrame(matriz, columns= tag_columna)
print("----La tabla o datafarme ----NC = 0200")
print(df)
print("----Alejandra Rivera Valenzuela NC 0200 ----NC = 0200")
