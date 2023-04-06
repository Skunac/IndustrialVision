import matplotlib.pyplot as plt
import pandas as pd
import csv

debut = 1
end = 5
debut2 = 0
end2 = 5
specific_rows = [1,2,3,4]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
df = pd.read_csv('test_3d.csv', sep=",")

#affichae des points de tous les vertices
ax.scatter(df.a,df.b,df.c, color=df.d)


#mise en place de lignes pour chaque doigts
while(True):

    ax.plot(df.iloc[debut:end].a,df.iloc[debut:end].b,df.iloc[debut:end].c)
    debut += 4
    end += 4
    if end > 21:
        break

#liaison entre les derniers points manquants
ax.plot([df.iloc[0].a, df.iloc[1].a], [df.iloc[0].b, df.iloc[1].b], [df.iloc[0].c, df.iloc[1].c])
ax.plot([df.iloc[0].a, df.iloc[5].a], [df.iloc[0].b, df.iloc[5].b], [df.iloc[0].c, df.iloc[5].c])
ax.plot([df.iloc[5].a, df.iloc[9].a], [df.iloc[5].b, df.iloc[9].b], [df.iloc[5].c, df.iloc[9].c])
ax.plot([df.iloc[9].a, df.iloc[13].a], [df.iloc[9].b, df.iloc[13].b], [df.iloc[9].c, df.iloc[13].c])
ax.plot([df.iloc[13].a, df.iloc[17].a], [df.iloc[13].b, df.iloc[17].b], [df.iloc[13].c, df.iloc[17].c])
ax.plot([df.iloc[0].a, df.iloc[17].a], [df.iloc[0].b, df.iloc[17].b], [df.iloc[0].c, df.iloc[17].c])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()