
# media

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


count = 0   # contador de observaciones
print("— CANTIDAD DE OBSERVACIONES --")
n = reader.count()
print("Cantidad de observaciones = " + str(n))

print ("\n-- MIN --")
valoresOrdenados = reader.sort_values()
valoresOrdenados = valoresOrdenados.reset_index(drop=True)
print("Valor mínimo: "+str(valoresOrdenados [0]))

print ("\n-- MAX --")
valoresOrdenados = reader.sort_values()
valoresOrdenados = valoresOrdenados.reset_index(drop=True)
print("Valor máximo: " + str(valoresOrdenados[len(valoresOrdenados)-1]))


print ("\n-- MEDIA --")
def calculoMediaAritmetica(caracteristica):
   n = caracteristica.count()
   sumaValorObservaciones = 0
   mediaAritmetica = 0

   if n>0 :
       for valorObservacion in caracteristica:
           sumaValoresObservaciones = sumaValoresObservaciones + valorObservacion
       mediaAritmetica = sumaValorObservaciones / n

   return mediaAritmetica

def calculoMediana(self, caracteristica):
   mediana = 0
   caracteristica = caracteristica.sort_values()
   caracteristica = caracteristica.reset_index(drop=True)
   n = self.caracteristica.count()
   par = False
   if (n % 2 == 0):
       print("La cantidad de observaciones es par.")
       par = True

   if par:
       rango = (n / 2)
       rangoPython = rango-1
       valor1 = caracteristica[rangoPython]
       valor2 = caracteristica[rangoPython+1]
       mediana = valor1 +((valor2-valor1)/2)
   else:
       rango = ((n + 1) / 2)
       rangoPython = rango - 1
       mediana = caracteristica [rangoPython]
   return mediana

#crear una funcion que me dvuelva el valor mas repetido
def calculoModa(caracteristica):
    moda = Counter(caracteristica)
    return moda.most_common(1)

Counter(observaciones["Type 1"])

def rango(caracteristica):
    caracteristica = caracteristica.sort_values()
    caracteristica = caracteristica.reset_index(drop=True)
    n = len(caracteristica)
    rango = (caracteristica[n-1] - caracteristica[0])
    return rango


# funcion para los cuartiles


def calculoDelosCuartiles(self,mediana,rangoMediana):
   n = self.caracteristica.count()
   sort_caracteristica = self.caracteristica.sort_valores()
   sort_caracteristica = sort_caracteristica.reset_index(drop=True)
   q1 = 0
   q2 = mediana
   q3 = 0

   #Calculo Q1
   restoDivision = rangoMediana%2
   if (restoDivision != 0):
       q1 = sort_caracteristica[((rangoMediana/2)+1)-1]
   else:
       valorMin = sort_caracteristica[((rangoMediana/2)-1)]
       valorMax = sort_caracteristica[(rangoMediana/2)]
       q1 = (valorMin + ((valorMax - valorMin) / 2) + valorMax) / 2

   # Calculo Q3
   nbdatos = len(sort_caracteristica)+1
   nbDatosDesdeMediana = nbdatos - rangoMediana
   restoDivision = nbDatosDesdeMediana % 2
   if (restoDivision != 0):
       q3 = sort_caracteristica[nbDatosDesdeMediana - 1]
   else:
       valorMinQ3 = sort_caracteristica[(rangoMediana+(nbDatosDesdeMediana/2))-1]
       valorMaxQ3 = sort_caracteristica[(rangoMediana+(nbDatosDesdeMediana/2))]
       q3 = (valorMin + ((valorMax - valorMin) / 2) + valorMax) / 2
   return ([q1, q2, q3])