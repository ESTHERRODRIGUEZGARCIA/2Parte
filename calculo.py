# funcion que me cree la media de la variable total

from math import sqrt
import os
from typing import Counter
import pandas as pd



import csv
f= open("Pokemon.csv")
reader = csv.reader(f)
for row in reader:
    print (row)

observaciones = pd.read_csv("Pokemon.csv")


def mediaAritmetica(caracteristica):
    n = caracteristica.count()
    sumaValorObservaciones = 0
    mediaAritmetica = 0
    if n>0 :
        for valorObservacion in caracteristica:
            sumaValorObservaciones = sumaValorObservaciones + valorObservacion
        mediaAritmetica = sumaValorObservaciones / n
    return mediaAritmetica

