import os
from os import listdir
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

f = open('Manocsv.csv', 'r', newline='\n')
compte_main_gauche = 0
compte_main_droite = 0

reader = csv.reader(f,delimiter=',')
for row in reader:
    for objet in row:
        if objet == "Gauche":
            compte_main_gauche = compte_main_gauche + 1

        elif objet == "Droite":
            compte_main_droite = compte_main_droite + 1

print("main gauche : ", compte_main_gauche, "main droite : ", compte_main_droite)


names = ["main gauche", "main droite"]
values = [compte_main_gauche, compte_main_droite]

fig, ax = plt.subplots()

ax.bar(names, values, color=['#FF6347','#007FFF'])
ax.set_title("Répartition des blessures par main")


plt.show()