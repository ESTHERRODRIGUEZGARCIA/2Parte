
# media

from math import sqrt
import os
import pandas as pd



import csv
f= open("Pokemon.csv")
reader = csv.reader(f)
for row in reader:
    print (row)

observaciones = pd.read_csv("Pokemon.csv")

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

def calculoMediana(caracteristica):
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



def calculoModa(caracteristica):
   moda = Counter(caracteristica)
   return moda