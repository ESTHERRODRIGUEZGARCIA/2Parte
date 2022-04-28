
# media

from math import sqrt
import os
import pandas as pd



import csv
f= open("Pokemon.csv")
reader = csv.reader(f)
for row in reader:
    print (row)

observaciones = pd.DataFrame({'NOTAS':np.array(['Pokemon.csv'])})
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


# funcion que cree una columna con el resultado de la media
def calcular_media(dataset, col1, col2):
    media = dataset[col2].sum()/dataset[col1].sum()
    return media

# funcion que me dev
# dos es la multiplicación xi*ni
class Media:
    #Constructor
    def __init__(self, dataset, col1, col2):
        self.dataset = dataset
        self.col1 = col1
        self.col2 = col2

    def calcular_media(self):

        def calcular_dos():
            dos = []
            for i in range (len(self.dataset)):
                resultado = self.dataset[self.col1][i]*self.dataset[self.col2][i]
                dos.append(resultado)
            return dos

        self.dataset["XiNi"] = calcular_dos()
        suma_dos = self.dataset["DOS"].sum()
        suma_ni = self.dataset[self.col2].sum()

        return suma_dos/suma_ni


def calcular_std(dataset, col1, col2):

    def columna_std():
        columna = []
        media = calcular_media(dataset, col1, col2)
        for i in range(len(dataset)):
            resultado = dataset[col2][i] * (dataset[col1][i] - media)*(dataset[col1][i] - media)
            columna.append(resultado)
        return columna

    dataset["Ni*((Xi-media)^2)"] = columna_std()
    suma_columna = dataset["Ni*((Xi-media)^2)"].sum()
    suma_ni = dataset[col2].sum()
    varianza = suma_columna/suma_ni

    return sqrt(varianza)
