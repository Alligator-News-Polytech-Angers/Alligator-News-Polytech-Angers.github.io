
# ------------------------------------
#     Copyright : Thomas LÉPINE
# ------------------------------------

from PIL import Image as imageT
from resizeimage import resizeimage
import os;
import random as rm;

#General informations
chemin_courant = os.getcwd()
#print(chemin_courant)
path_used = chemin_courant.split('\\')
#print(path_used)
#Recompose le chamin du fichier finally
output_directory = ""
for i in range(0, len(path_used)-2):
	output_directory += path_used[i] + '\\'	
	
output_directory += 'ressources\\images\\pop\\' #Chemin où seront sauvegardés les images

print("Quel est le chemin du dossier des images à convertir ?")
input_directory = input() + "\\"

print('\n')
print("De quel édition il s'agit ?")
output_directory += input()
print('\n')
nb_converti = 0

if not os.path.exists(output_directory):
	os.makedirs(output_directory) #Créer le répertoire s'il n'exite pas	
else:
	print("/!\\ Le dossier existe déjà /!\\")
	
output_directory += "\\"	
	
for filename in os.listdir(input_directory):	
	print('> Nom de l\'image = ' + filename)
	if filename.split('.')[1] == 'webp': #Ne convertit pas les fichier déjà au format voulu
		next #On passe à l'image suivante
	else:
		nb_converti += 1	
		image = imageT.open(input_directory + filename)

		if image.size[1] > 800: #Si la hauteur dépasse 800 pixels on redimensionne l'image
			image = resizeimage.resize_height(image, 800)

		image.save(output_directory + filename.split('.')[0] + ".webp", "webp") #On enregistre l'image au bon format

print('\n')
print("Fin du programme, " + str(nb_converti) + " image(s) ont été converti, appuyez sur une touche pour arrêter ...")
input()