import os
from os import listdir

f = open('data.csv', 'w')
folder_dir = "C:/Users/antdu/OneDrive/Bureau/projet/data/keypoints_labels"
for file in os.listdir(folder_dir):
    monfile = "C:/Users/antdu/OneDrive/Bureau/projet/data/keypoints_labels/" + file
    f1 = open(monfile, 'r')
    for line in f1:
        f.write(line) 

f.close()