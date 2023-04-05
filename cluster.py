import numpy
import matplotlib.pyplot as plt
import csv
import pandas as pd
import os
from os import listdir

def middlePoint(x1,x2):
    mid =  (x1+x2)/2
    return (mid)

df = pd.read_csv(
    'data_link_output_img.csv', usecols=['vx11','vx12','vy11','vy12'], sep=",")

middleX = []
middleY = []
for row in df:
    for i in range(1, 50):
        middleX[i] = middlePoint(df.vx11, df.vx12)
        middleY[i] = middlePoint(df.vy11, df.vy12)

print(middleX)
