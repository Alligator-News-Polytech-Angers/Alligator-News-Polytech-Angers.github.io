from PIL import Image as imageT
from resizeimage import resizeimage
import os;
import random as rm;

#General informations
input_directory="input/"
output_directory="output/"


for filename in os.listdir(input_directory):
	
	if filename[-4:] == 'webp': #Ne converti pas les fichier déjà converti
		break
	else:
		print(filename)	
		image = imageT.open(input_directory + filename)

		if image.size[1] > 1000: #Si la hauteur dépasse 1000 pixels on redimensionne
			image = resizeimage.resize_height(image, 1000)

		image.save(output_directory + filename[:-4] + ".webp", "webp")
	