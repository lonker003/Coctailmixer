import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd



data_output = pd.read_table("output.txt")
print(data_output.columns)


def Hitze_output(data):
    Temperatur  = np.asarray(data['Temperatur'][50:])
    Gewicht = np.asarray(data['Gewicht'][50:])
    Zeit = np.asarray(data['Zeit'][50:])
    
    plt.figure(figsize=(8,5),layout="constrained")
    plt.errorbar(
        Temperatur,Gewicht,
        xerr=0,
        yerr=0,
        marker='+',
        linestyle='',
        color='orange',
        label='Daten mit Unsicherheiten'
    )
    plt.grid()
    plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=3, shadow=True)
    plt.xlabel('Temperatur in Grad',fontsize = 15)
    plt.ylabel('Gewicht in gr',fontsize = 15)
    plt.savefig('Hitze-Kilo_Diagramm.pdf')
    return 

Hitze_output(data_output)