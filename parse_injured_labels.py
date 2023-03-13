import os
from os import listdir

f = open('injured_labels_data.csv','w')
folder_dir = "C:/Users/antdu/Mon Drive/projet/data/injury_labels"
for file in os.listdir(folder_dir):
    ffile = "C:/Users/antdu/Mon Drive/projet/data/injury_labels/" + file
    f1 = open(ffile,'r')
    for line in f1:
        formated_line = "{} {}".format(file,line)
        usable_line = formated_line.replace(" ",", ")
        f.write(usable_line)

f.close()
f1.close()