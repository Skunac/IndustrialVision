import os
from os import listdir

f = open('keypoints_labels_data.csv','w')
folder_dir = "G:/Mon Drive/projet/data/keypoints_labels"
for file in os.listdir(folder_dir):
    ffile = "G:/Mon Drive/projet/data/keypoints_labels/" + file
    f1 = open(ffile,'r')
    for line in f1:
        unformated_line = line.replace(", "," ")
        formated_line = "{}, {}".format(file,unformated_line)
        short_formated_line = formated_line[:len(formated_line)-3]
        short_usable_line = short_formated_line.replace("]",",")
        usable_line = short_usable_line.replace("[","")
        f.write(usable_line+'\n')

f.close()
f1.close()