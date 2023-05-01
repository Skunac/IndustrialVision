import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

def middlePoint(x1, x2):
    mid = (x1 + x2) / 2
    return mid



# Fonction pour trouver le point le plus proche dans une liste de coordonnées
def find_nearest_point(x, y, coordinates):
    nearest_point = None
    nearest_distance = float("inf")

    for point in coordinates:
        distance = np.sqrt((point[0] - x)**2 + (point[1] - y)**2)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_point = point

    return nearest_point

# CSV avec toutes les données
df = pd.read_csv('data_link_output_img.csv', usecols=['name',
                 'center_x0','center_y0'], sep=',')

# CSV avec x,y
data = pd.read_csv("data_link_output_img_xy_only.csv")

# Créer un dictionnaire pour stocker les coordonnées x et y avec les noms correspondants

data_dict = {}
for i, row in data.iterrows():
    name = row['name']
    coords = []
    for col in range(1, len(data.columns), 2):
        coords.append((row[data.columns[col]], row[data.columns[col + 1]]))
    data_dict[name] = coords

middlepoints = {}

# Parcours des lignes du DataFrame
for _, row in df.iterrows():
    name = row['name']
    x, y = row['center_x0'], row['center_y0']
    middlepoints[name] = (x, y)
    

# Trouver le point le plus proche pour chaque paire de coordonnées dans middlepoints en utilisant les coordonnées de data_dict
for name, (x, y) in middlepoints.items():
    if name in data_dict:
        coordinates = data_dict[name]
        nearest_point = find_nearest_point(x, y, coordinates)
        print("Le point le plus proche de ({}, {}) pour '{}' dans data_dict est {}".format(x, y, name, nearest_point))
    else:
        print("Le nom '{}' n'a pas été trouvé dans data_dict.".format(name))

