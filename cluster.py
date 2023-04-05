import numpy
import matplotlib.pyplot as plt
import csv
import pandas as pd
import os
from os import listdir

def squareToPoint(x1,x2,y1,y2):
    midX =  (x1+x2)/2
    midY =  (y1+y2)/2
    return (midX, midY)

df = pd.read_csv(
    'data_link_output_img.csv', usecols=['vx11','vx12','vy11','vy12'], sep=",")

middle = []
for row in df:
    for i in range(1, 50):
        middle[0:2*i] = squareToPoint(df.vx11, df.vx12, df.vy11, df.vy12) #Le 0:2*i c'est parce qu'on retourne 2 valeurs à chaque fois dans squareToPoint()
