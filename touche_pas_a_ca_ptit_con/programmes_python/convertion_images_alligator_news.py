# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------

import os # Librairie pour les fonctions interagissant avec le système (fichiers, ...)
from PIL import Image as imagePillow # Librairie Pillow (traitement d'images)
'''
Docs : https://pillow.readthedocs.io/en/stable/reference/Image.html  https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
	   https://pillow.readthedocs.io/en/stable/handbook/concepts.html#filters
'''

def fonctionsImage(image):
	fileNameCut = filename.split('.')
	if fileNameCut[1] == 'png': # Si l'image est au format png
		imageName = output_directory + filename.split('.')[0] + ".png" # Nom de l'image finale
		newImage = image.convert("RGBA", palette=imagePillow.WEB) # Image.convert(mode=None, matrix=None, dither=None, palette=0, colors=256)
		formatImageOut = "png"
	else : # Autre format (ex : jpg, webp, ...)
		imageName = output_directory + filename.split('.')[0] + ".jpg" # Nom de l'image finale
		newImage = image.convert("RGB", palette=imagePillow.WEB) # Image.convert(mode=None, matrix=None, dither=None, palette=0, colors=256)
		formatImageOut = "jpeg"
	image.close() # libère les ressources systèmes

	newHeight = 720
	if newImage.size[1] > newHeight: #Si la hauteur dépasse 720 pixels on redimensionne l'image
		newWidth = newHeight * newImage.size[0] / newImage.size[1] # Calcul de la largeur pour garder les proportions de l'image
		size = (newWidth, newHeight)
		print("     -- New size (Width, Height) -> " + str(size))
		newImage.thumbnail(size, imagePillow.LANCZOS) # BILINEAR = qualité ok- / BICUBIC = qualité ok+ / ANTIALIAS = bonne qualité

	newImage.save(imageName, format=formatImageOut) #On enregistre l'image au bon format
	newImage.close() # libère les ressources systèmes


print("\n\nHello there !\n -> Bienvenue sur ce programme de convertion d'image made in Alligator News, son but est de compresser les images afin de limiter l'impact environnementale du stockage des images !")

#General informations
chemin_courant = os.getcwd()
path_used = chemin_courant.split('\\')

#Recompose le chamin du fichier finale
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
	print("/!\\ Le dossier a déjà été créé /!\\")
	
output_directory += "\\"
print("CHEMIN DE SORTIE : " + output_directory)
	
for filename in os.listdir(input_directory):	
	print('> Nom de l\'image = ' + filename)
	image = imagePillow.open(input_directory + filename, 'r') # Récupère l'image
	fonctionsImage(image) # Transforme et converti l'image (redimenssionne)
	nb_converti += 1

print("Copyright du programme : Thomas Lépine\n")
print("\nFin du programme, " + str(nb_converti) + " image(s) ont été converti, appuyez sur une touche pour arrêter ...")
input() # Attendre qu'une touche soit appuyé pour quitter le programme