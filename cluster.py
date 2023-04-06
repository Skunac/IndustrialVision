import pandas as pd
import matplotlib.pyplot as plt
import math


def middlePoint(x1, x2):
    mid = (x1 + x2) / 2
    return mid


df = pd.read_csv('data_link_output_img.csv', usecols=[
                 'vx11', 'vx12', 'vy11', 'vy12'], sep=',')

middleX = [0] * 50
middleY = [0] * 50
for i, row in df.iterrows():
    middleX[i] = middlePoint(row['vx11'], row['vx12'])
    middleY[i] = middlePoint(row['vy11'], row['vy12'])

#print(middleX)

for i in range(1,20):
    pointToCompare = (middleX[i],middleY[i])
    minDistance = math.inf
    closestSet = None
    for index, row in df.iterrows():
        xValues = [float(row[f'x{i}']) for i in range(1, 21)]
        yValues = [float(row[f'y{i}']) for i in range(1, 21)]
        currentPoints = list(zip(xValues, yValues))