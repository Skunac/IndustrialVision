import os
from os import listdir
import csv

folder_dir = "/home/jonathan/Documents/vdd/donnees_projet_vdd/Nouveau dossier/double_labeled_data_visualisation"
image = ""
monoutput = ""
compteur = 0

f = open("data_link_output_img.csv", "w")

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