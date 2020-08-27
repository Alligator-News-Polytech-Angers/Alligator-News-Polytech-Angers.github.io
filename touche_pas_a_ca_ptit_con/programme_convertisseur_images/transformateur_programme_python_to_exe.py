from cx_Freeze import setup, Executable

setup(		
	name = "convertion_images_alligator_news.exe",
	version = "1.0",
	description = "Convertisseur d'images pour le site Alligator News (format webp)",
	executables = [Executable("convertion_images_alligator_news.py")]
)