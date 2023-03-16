import os
from os import listdir
import csv

folder_dir = "/home/jonathan/Documents/vdd/donnees_projet_vdd/Nouveau dossier/double_labeled_data_visualisation"
image = ""
monoutput = ""

f = open("output.csv", "w")

for file in os.listdir(folder_dir):

    file = file.split(",")

    for val,key in enumerate(file):
 
        if(val%2 != 0):
            monoutput = key.strip(".jpg")
            monoutput = monoutput + ".txt"

        else:
            image = key.strip(".jpg")
            image = image + ".txt"

    with open("keypoint_label_data.csv", "r", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:

            if row[0] == monoutput:
               
                f.write(image + " " + ",".join(row))
#                f.write("\n")

    with open("injured_label.csv", "r", newline="") as file2:
        reader2 = csv.reader(file2, delimiter=",")
        for row in reader2:

            if row[0] == image:

                f.write("," + ",".join(row))
    f.write("\n")        

f.close()