# -*- coding: utf-8 -*-
"""Entidad_Proyecto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_PuhiDZwmZjxKgUiNohzA5r4KBMF4qVq
"""

!pip install Faker
import pandas as pd
import uuid
import random
from faker import Faker
import datetime

#Numero de datos sinteticos 
num_users = 5000

# Lista de atributos 
features = [
    "id_Pro",
    "T.Proyecto",
    "dob",
    "Estado"

]# Crea el dataframe con la lista de atributos
df = pd.DataFrame(columns=features)

#Utilizamos uuid para generar numeros aleatorios 
df['id_Pro'] = [uuid.uuid4().int for i in range(num_users)]

#Verifica que cada numero generado sea único
print(df['id_Pro'].nunique()==num_users)

tb = ["Emprendimiento", "Inversión", "Socio Económica", "Legal" , "Estudiantil"]
df['T.Proyecto'] = random.choices(tb , weights=(25,35,20,10,10), k=num_users)

def random_dob(start, end, n):
    """
    Generar una lista de un número determinado de marcas de tiempo
    """
    
    # El formato de marca de tiempo
    frmt = "%Y-%m-%d"
    
    # Formateo de los dos períodos de tiempo
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    
    # Creando el grupo para tiempos aleatorios
    td = etime - stime
    
    # Generando una lista con los tiempos aleatorios
    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]
    
    return times

df['dob'] = random_dob("1980-01-01", "2006-01-01", num_users)

Genero_Bes = ["Activo", "Inactivo", "En espera"]

df['Estado'] = random.choices(
    Genero_Bes, 
    weights=(47,47,6), 
    k=num_users
)



df.to_csv('dataset_users.csv')