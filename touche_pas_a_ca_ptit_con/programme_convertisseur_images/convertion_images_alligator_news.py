# ------------------------------------
#     Copyright : Thomas LÉPINE
# ------------------------------------

from PIL import Image as imagePillow # Librairie Pillow (traitement d'images)
import numpy as np # Numpy -> Traitement matricielle (NB : une image est une matrice composée pixels grosso modo)
from resizeimage import resizeimage # Diminuer la taille d'une image pour moins de stockage
import os # Librairie pour les fonctions interagissant avec le système (fichiers, ...)

def fonctionsImage(image):
	newImage = image.convert("RGB", palette=imagePillow.WEB) # Image.convert(mode=None, matrix=None, dither=None, palette=0, colors=256) # https://pillow.readthedocs.io/en/stable/_modules/PIL/Image.html#Image.convert
	# print("Infos : " + image.mode + " -> mode / format -> " + image.format)
	# print("Infos : " + newImage.mode + " -> mode")
	if newImage.size[1] > 800: #Si la hauteur dépasse 800 pixels on redimensionne l'image
		newImage = resizeimage.resize_height(newImage, 800)

	newImage.save(output_directory + filename.split('.')[0] + ".webp", "webp") #On enregistre l'image au bon format
	newImage.close() # libère les ressources systèmes
	image.close() # libère les ressources systèmes


#General informations
chemin_courant = os.getcwd()
#print(chemin_courant)
path_used = chemin_courant.split('\\')
#print(path_used)
#Recompose le chamin du fichier finalle
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
	image = imagePillow.open(input_directory + filename)
	fonctionsImage(image)
	nb_converti += 1	

print('\n')
print("Fin du programme, " + str(nb_converti) + " image(s) ont été converti, appuyez sur une touche pour arrêter ...")
input()