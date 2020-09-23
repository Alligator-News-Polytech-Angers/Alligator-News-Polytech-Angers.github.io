
# ------------------------------------
#     Copyright : Thomas LÉPINE
# ------------------------------------

from PIL import Image as imageT
from resizeimage import resizeimage
import os;

#General informations
chemin_courant = os.getcwd()
#print(chemin_courant)
path_used = chemin_courant.split('\\')
#print(path_used)
#Recompose le chamin du fichier finally
output_directory = ""
for i in range(0, len(path_used)):
	output_directory += path_used[i] + '\\'	

input_directory_automatic = output_directory + 'images_a_convertir\\'
output_directory += 'ressources\\images\\pop\\' #Chemin où seront sauvegardés les images
print("output_directory USED :" + output_directory + "\n\n")
print("Quel est le chemin du dossier des images à convertir ? (1 pour le chemin automatique)")
input_console = input()
if input_console == '1' :
	input_directory = input_directory_automatic
else :	
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
print("CHEMIN DE SORTIE : " + output_directory)
	
for filename in os.listdir(input_directory):	
	print('> Nom de l\'image = ' + filename)
	if filename.split('.')[1] == 'webp': #Ne convertit pas les fichier déjà au format voulu
		#next #On passe à l'image suivante
		image = imageT.open(input_directory + filename)
		if image.size[1] > 800: #Si la hauteur dépasse 800 pixels on redimensionne l'image
			image = resizeimage.resize_height(image, 800)

		image.save(output_directory + filename.split('.')[0] + ".webp", "webp") #On enregistre l'image au bon format
	else:
		nb_converti += 1	
		image = imageT.open(input_directory + filename)

		if image.size[1] > 800: #Si la hauteur dépasse 800 pixels on redimensionne l'image
			image = resizeimage.resize_height(image, 800)

		image.save(output_directory + filename.split('.')[0] + ".webp", "webp") #On enregistre l'image au bon format

print('\n')
print("Fin du programme, " + str(nb_converti) + " image(s) ont été converti, appuyez sur une touche pour arrêter ...")
input()