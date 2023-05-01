import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

import matplotlib.pyplot as plt

# # Les coordonnées normalisées des 21 repères de la main
# landmarks = [[0.5, 0.2], [0.4, 0.3], [0.3, 0.4], [0.2, 0.5], [0.1, 0.6], [0.1, 0.7], [0.2, 0.8], [0.3, 0.9], [0.4, 0.8], [0.5, 0.7], [0.6, 0.6], [0.7, 0.5], [0.8, 0.4], [0.9, 0.3], [0.8, 0.2], [0.7, 0.1], [0.6, 0.1], [0.5, 0.3], [0.5, 0.5], [0.5, 0.7], [0.5, 0.9]]


# df2 = pd.read_csv("data_link_output_img_xy_only.csv")

# # Création de la figure et des axes
# fig, ax = plt.subplots()

# # Tracer les repères de la main
# for landmark in landmarks:
#     ax.plot(landmark[0], landmark[1], marker='o', markersize=10, color='blue')

# # Définir les limites des axes
# ax.set_xlim([0, 1])
# ax.set_ylim([0, 1])

# # Afficher la figure
# plt.show()


# Pour toute le fichier csv :

data = pd.read_csv("data_link_output_img_xy_only.csv",nrows=2)

df = pd.read_csv('data_link_output_img.csv', usecols=['name',
                 'vx11', 'vx12', 'vy11', 'vy12'], sep=',',nrows=2)

# Extraire les coordonnées x et y pour chaque point de repère
x = data.iloc[:, 1:64:2].values.flatten()
y = data.iloc[:, 2:64:2].values.flatten()


# les blessure 
x2 = [df.iloc[0]['center_x0'], df.iloc[0]['center_0']]
y2 = [df.iloc[0]['vy11'], df.iloc[0]['vy12']]

print(x2)
print(y2)

# Dessiner un graphique en nuage de points
plt.scatter(x, y)
plt.scatter(x2,y2,c='r')
plt.show()










# Pour toute le fichier csv :

# data = pd.read_csv("data_link_output_img_xy_only.csv",nrows=2)

# df = pd.read_csv('data_link_output_img.csv', usecols=['name',
#                  'vx11', 'vx12', 'vy11', 'vy12'], sep=',',nrows=2)

# # Extraire les coordonnées x et y pour chaque point de repère
# x = data.iloc[:, 1:64:2].values.flatten()
# y = data.iloc[:, 2:64:2].values.flatten()

# second row = data.iloc[1:2, :]

# for i, row in df.iterrows():
#     x2 = [row['vx11'], row['vx12']]
#     y2 = [row['vy11'], row['vy12']]

# print(x2)
# print(y2)

# # Dessiner un graphique en nuage de points
# plt.scatter(x, y)
# plt.scatter(x2,y2,c='r')
# plt.show()








# Avec les aretes ; a modifer 
# # Lire le fichier CSV
# data = pd.read_csv("data_link_output_img.csv",nrows=1)

# # Extraire les coordonnées x, y et z pour chaque point de repère
# x = data.iloc[:, 1:64:3].values.flatten()
# y = data.iloc[:, 2:64:3].values.flatten()
# z = data.iloc[:, 3:64:3].values.flatten()

# # Dessiner un graphique en nuage de points avec les arêtes entre les points
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Dessiner les points
# ax.scatter(x, y, z, c='blue', marker='o')

# # Dessiner les arêtes
# for i in range(20):
#     for j in range(i+1, 21):
#         ax.plot([x[i], x[j]], [y[i], y[j]], [z[i], z[j]], c='red')

# plt.show()





