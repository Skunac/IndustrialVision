import os
from os import listdir
import csv

f = open('keypoints_labels_data.csv','w')
file = open("test.csv","r",newline='\n')
reader=csv.reader(file,delimiter=',')
for row in reader:
    file_name = row[0]
    for i in range(1,20):
        f.write(file_name + row[i].replace(" ",","))
        f.write('\n')
