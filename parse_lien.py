import os
from os import listdir
import csv

folder_dir = "/home/jonathan/Documents/vdd/donnees_projet_vdd/Nouveau dossier/double_labeled_data_visualisation"
image = ""
monoutput = ""
compteur = 0

f = open("data_link_output_img.csv", "w")

with open("keypoints_labels_data.csv", "r", newline="") as file:
    
    f.write("name, x0, y0 ,z0, x1, y1 ,z1, x2, y2 ,z2, x3, y3 ,z3, x4, y4 ,z4, x5, y5 ,z5, x6, y6 ,z6, x7, y7 ,z7, x8, y8 ,z8, x9, y9 ,z9, x10, y10 ,z10, x11, y11 ,z11, x12, y12 ,z12, x13, y13 ,z13, x14, y14 ,z14, x15, y15 ,z15, x16, y16 ,z16, x17, y17 ,z17, x18, y18 ,z18, x19, y19 ,z19, x20, y20 ,z20, v0, v1, v2, v3, v4")
    f.write("\n")

for file in os.listdir(folder_dir):

    file = file.split(",")

    for val,key in enumerate(file):
 
        if(val%2 != 0):
            monoutput = key.strip(".jpg")
            monoutput = monoutput + ".txt"

        else:
            image = key.strip(".jpg")
            image = image + ".txt"

    # Ouverture du fichier afin d'écrire les données contenus dans notre nouveau fichier
    with open("keypoints_labels_data.csv", "r", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:

            #Si on a cette égalité alors ça veut dire que ce sont les données correspondants à notre image
            if row[0] == monoutput:

                #On affiche le nom au début
                if compteur == 0:
                    compteur = compteur + 1
                    f.write(image + " " + ",".join(row))

                #Si on atteint 20 itérations alors cela veut dire que l'on a lu toutes les données ainsi on passe au images suivantes
                elif compteur == 20:
                    f.write("," + ",".join(row[1:]))   
                    compteur = 0

                #Cas de base on écrit dans le fichier
                else:
                    f.write( "," +",".join(row[1:]))   
                    compteur = compteur + 1


    #Ouverture du second fichier et écriture dans notre fichier de données correspondantes à l'image que l'on traite actuellement
    with open("injured_labels_data.csv", "r", newline="") as file2:
        reader2 = csv.reader(file2, delimiter=",")
        for row in reader2:

            if row[0] == image:

                f.write("," + ",".join(row[1:]))
    f.write("\n")        

f.close()