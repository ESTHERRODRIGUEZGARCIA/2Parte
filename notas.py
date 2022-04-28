
# media

from math import sqrt
import os
os.chdir("C:\\Datos")
os.getcwd()

import csv
f= open("Pokemon.csv")
reader = csv.reader(f)
for row in reader:
    print (row)

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
