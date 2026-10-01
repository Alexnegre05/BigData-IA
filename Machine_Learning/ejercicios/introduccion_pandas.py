
import pandas as pd

diccionario = {
    "Nombre": ["Ana", "Paco","Marta", "Luis", "Elena", "Carlos", "Sara", "Miguel", "Lucia", "Andres"],
    "Edad": [23,21,19,25,22,20,18,27,21,24],
    "Puntos":[43,38,41,35,39,36,34,45,42,37],
    "Estudios superiores": ["Si", "No", "Si", "No", "Si", "Si", "No", "No", "Si", "No"]
}

dataframe = pd.DataFrame(diccionario)
print(dataframe)