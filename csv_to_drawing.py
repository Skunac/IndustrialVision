import numpy
import matplotlib.pyplot as plt
import pandas as pd
import csv
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv(
    'test.csv', usecols=['a','b','c'], sep=",")
fig = px.scatter_3d(df, x="a",y="b",z="c")

fig.update_layout(scene=dict(
    xaxis_title='X AXIS',
    yaxis_title='Y AXIS',
    zaxis_title='Z AXIS'),
    width=1920,
    margin=dict(r=20, b=10, l=10, t=10))



fig.show()