import pandas as pd
import matplotlib.pyplot as plt


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

print(middleX)

