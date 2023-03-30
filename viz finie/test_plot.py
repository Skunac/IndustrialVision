import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
from matplotlib import pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(2, 3, 4, c='red', marker='*', s=1000)
df = pd.read_csv('test.csv')

print(df.head(5))

#plt.show()