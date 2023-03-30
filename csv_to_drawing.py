import matplotlib.pyplot as plt
import pandas as pd
import csv
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

df = pd.read_csv(
    'test.csv', usecols=['a','b','c','d','e','f'], sep=",")
fig1 = px.scatter_3d(df, x="a", y="b", z="c", color='d')
plt.hold()
fig1 = px.line_3d(df, x="a", y="b", z="c",color='d')

fig1.update_layout(scene=dict(
    xaxis_title='X AXIS',
    yaxis_title='Y AXIS',
    zaxis_title='Z AXIS'),
    width=1920,
    margin=dict(r=20, b=10, l=10, t=10))


fig1.show()