import pandas as pd
import matplotlib.pyplot as plt
import math

injury_points={}

#use of dictionnary for reading purposes
def find_key_by_value(dictionary, value):
    return next((key for key, val in dictionary.items() if val == value), None)

def middlePoint(x1, x2):
    mid = (x1 + x2) / 2
    return mid

def closestVertice(vertices, point):
    min_distance = math.inf
    nearest_vertice = None

    for coordinates in vertices:
         distance = math.sqrt((point[0] - coordinates[0]) ** 2 + (point[1] - coordinates[1]) ** 2)
         if distance < min_distance:
            min_distance = distance
            nearest_vertice =coordinates

    return  nearest_vertice


df = pd.read_csv('data_link_output_img.csv', usecols=['name',
                 'vx11', 'vx12', 'vy11', 'vy12'], sep=',')

middleX = [0] * 50
middleY = [0] * 50
for i, row in df.iterrows():
    middleX[i] = middlePoint(row['vx11'], row['vx12'])
    middleY[i] = middlePoint(row['vy11'], row['vy12'])

    injury_points[row['name']]=(middleX[i],middleY[i])



df2 = pd.read_csv("data_link_output_img_xy_only.csv", usecols=all, sep=',')


for i in range(0,50):
    pointToCompare = (middleX[i],middleY[i])

    for index, row in df2.iterrows():
        xValues = [float(row[f'x{k}']) for k in range(0, 20)]
        yValues = [float(row[f'y{k}']) for k in range(0, 20)]
        currentPoints = list(zip(xValues, yValues))

    key = find_key_by_value(injury_points,pointToCompare)
    print( "key : ",key," Injury : ",closestVertice(currentPoints,pointToCompare))  