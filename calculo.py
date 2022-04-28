# crear gráfico

from matplotlib import pyplot as plt
import notas
import csv
import sys

# funcion que cree un gráfico del csv

def grafico(caracteristica):
    plt.hist(caracteristica)
    plt.show()



