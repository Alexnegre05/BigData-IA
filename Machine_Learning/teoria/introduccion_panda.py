
import pandas as pd # pandas sirve para tener matrices en python

print("\n dataframe 1: \n")
datos = {
    "Marca": ["Mercedes", "Seat", "Honda"],
    "Modelo": ["GLA", "Formentera", "Cinic"],
    "Precio": [40000, 7000,5000]
}


dataframe = pd.DataFrame(datos) # dataframe crea una matriz con columnas: valores (a11,a12,a13...), siguiente (a21,a22,a23...)

print(dataframe)

print("\n")

print("dataframe 2: \n")
datos = [
    ["mercedes", "GLA", 40000],
    ["seat", "Formentera", 7000],
    ["Honda", "Cinic", 5000]
]

dataframe = pd.DataFrame(datos, ["Marca", "Modelo", "Precio"])

print(dataframe) # importante te cambia la m*n por n*m

print("\n")

print("dataframe 3: \n")
dataframe = pd.DataFrame(["Marca", "Modelo", "Precio"], datos)

print(dataframe) # te printea algo raro

print("\n")

# esto no es una matriz?, para que dataframes

matriz = [[1,2,3],[4,5,6],[7,8,9]]

# diccionario

# lista de diccionario

# 11 listas separadas

# lista tuplas