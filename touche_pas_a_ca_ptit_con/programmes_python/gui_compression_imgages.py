"""
# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------
"""
__author__ = ("Thomas LÉPINE")
__contact__ = ("thomas.lep4@gmail.com")
__version__ = "1.0.0"
__copyright__ = "Thomas Lépine"
__date__ = "2021/04"

try:
    from tkinter import *
    from tkinter import filedialog, messagebox, ttk
except ImportError:
    # pour python 2.x
    from Tkinter import *
    from Tkinter import filedialog, messagebox, ttk
from PIL import Image # Librairie Pillow (traitement d'images) 
''' Docs : https://pillow.readthedocs.io/en/stable/reference/Image.html  https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes '''
import sys
# import this
# import antigravity

''' VARIABLES GLOBALES '''
MAIN_WINDOW = None
WINDOWS_OPTIONS = {'width': 1000, 'height': 600, 'background-compressionImg': "#5C8199"}
image_list = []
canvas = None

''' Quitte l'application : '''
def exit():
    global MAIN_WINDOW
    msgBox = messagebox.askquestion(
        'Quitter l\'application', 'Êtes-vous sûr et certain de vouloir quitter l\'application ?', icon='warning')
    if msgBox == 'yes':
       MAIN_WINDOW.destroy()
       MAIN_WINDOW = None

''' ######### COMPRESSION DES IMAGES ######### '''
''' Récupère le/les fichiers : '''
def getFilesImagesAndName():
    global image_list
    image_list = [] # Réinitialisation de la liste
    filePathImport = filedialog.askopenfilenames(parent=MAIN_WINDOW, title='Choisissez un/des fichier(s)')
    # Transformation de la liste de chaine en liste Python
    lstFilePathImport = list(filePathImport)
    for file in lstFilePathImport:
        try :
            img = Image.open(file)
        except :
            error("Un fichier sélectionné n'est pas dans le format image ou n'est pas convertissable" + "\n\nFichier :\n" + str(file) + "\n\nMessage d'erreur du système : " + str(sys.exc_info()[0]))
            image_list = [] # Réinitialisation de la liste
        else :
            """ On ajoute le nom de l'image et sa signature PIL """
            image_list.append(file.split("/")[-1])
            image_list.append(img)

''' Calcule taille image '''
def calculTailleImage(image, option_resize) :
    """ Calcul des dimenssions de la nouvelle image """
    size = [image.size[0], image.size[1]] # Récuère les dimensions de l'image
    if option_resize <= 1:
        # Redimensionne par ratio
        size[0] = size[0] * option_resize
        size[1] = size[1] * option_resize
    elif option_resize == 720 and size[1] > 720:
        # On bloque la hauteur
        size[0] = 720 * size[0] / size[1] # Calcul de la largeur pour garder les proportions de l'image
        size[1] = 720
    elif option_resize == 1080 and size[1] > 1080:
        # On bloque la hauteur
        size[0] = 1080 * size[0] / size[1] # Calcul de la largeur pour garder les proportions de l'image
        size[1] = 1080
    elif option_resize == 1000 and size[0] > 1000:
        # On bloque la largeur
        size[1] = 1000 * size[1] / size[0] # Calcul de la largeur pour garder les proportions de l'image
        size[0] = 1000
    elif option_resize == 1920 and size[0] > 1920:
        # On bloque la largeur
        size[1] = 1920 * size[1] / size[0] # Calcul de la largeur pour garder les proportions de l'image
        size[0] = 1920
    return(size[0], size[1])

''' Compression des images '''
def compressionImg(liste_options) :
    global image_list
    # la liste image_list contient le nom de l'image suivi de sont de l'objet de la classe PIL associé
    if len(image_list) == 0:  # Aucun fichier n'a été selectionné
        error("Aucune image n'a été selectionné\n\nMerci de selectionner une ou plusieurs images avant")
    else :
        directoryPathExport = filedialog.askdirectory()
        if directoryPathExport == '' :
             error("Aucun dossier de destination n'a été selectionné")
        else :
            for i in range(0, len(image_list), 2):
                # On sépare le nom de l'image de son extension actuelle
                image_name = image_list[i].split('.')
                
                # Calcul des dimenssions de la nouvelle image
                size = calculTailleImage(image_list[i+1], liste_options['resize'])

                if liste_options['format'] == 'default' :
                    if image_name[1] != 'png' :
                        image_name[0] = image_name[0] + ".jpg"  # Nom de l'image finale"
                        newImage = image_list[i+1].convert("RGB", palette=Image.WEB) # Encodage de l'image
                        newImage.thumbnail(size, liste_options['quality'])
                        newImage.save(directoryPathExport + '/' + image_name[0], format="jpeg") #On enregistre l'image au bon format
                        # image_list[i+1].close()  # libère les ressources systèmes de cette image
                    else : # Pour les images de type png (sans fond)
                        image_name[0] = image_name[0] + ".png"  # Nom de l'image finale
                        newImage = image_list[i+1].convert("RGBA", palette=Image.WEB) # Encodage de l'image
                        newImage.thumbnail(size, liste_options['quality'])
                        newImage.save(directoryPathExport + '/' + image_name[0], format="png") #On enregistre l'image au bon format
                        # image_list[i+1].close()  # libère les ressources systèmes de cette image
                else :
                    image_name[0] = image_name[0] + "." + liste_options['format']  # Nom de l'image finale"
                    if liste_options['format'] == 'png' :
                        newImage = image_list[i+1].convert("RGBA", palette=Image.WEB) # Encodage de l'image
                    else :
                        newImage = image_list[i+1].convert("RGB", palette=Image.WEB) # Encodage de l'image
                    newImage.thumbnail(size, liste_options['quality'])
                    newImage.save(directoryPathExport + '/' + image_name[0], format="jpeg") #On enregistre l'image au bon format
                    # image_list[i+1].close()  # libère les ressources systèmes de cette image
            # Ouverture d'un pop-up pour avertir que la tâche est terminée
            msgFinTache = messagebox.showinfo(icon='info', title='Tâche terminée',
                message='Les images sélectionnées ont été convertis')
                
''' ERROR : '''
def error(messageError="Erreur rencontrée"):
    messagebox.showinfo(title="Erreur", icon='error', message=messageError)

''' SET VELUES '''
def setCompressionOptions(compression_options, quality_options = None, resize_options = None, format_options = None) :
    """ On update la valeur renseignée """
    if quality_options != None :
        compression_options['quality'] = quality_options
    elif resize_options != None :
        compression_options['resize'] = resize_options
    elif format_options != None :
        compression_options['format'] = format_options

''' HELP : '''
def helpCompressionImg():
    messagebox.showinfo(title="Aide", icon='question', message="Ce programme permet de compresser des images.\n\n1 : Chargez la ou les images souhaitées à l'aide du boutton \"Image(s)\".\n\n2 : Cliquez sur \"Compresser\" et selectionnez le dossier dans lequel vous souhaitez enregistrer la ou les images.\n\nEt voilà ! Vous pouvez ensuite quitter l'application (n'hésitez pas à aller vérifier que l'enregistrement a bien fontionné !)\n\n\nProgramme développé par Thomas Lépine (thomas.lep4@gmail.com)")

# Fenêtre
def appCompressionImg():
    global MAIN_WINDOW
    global canvas
    MAIN_WINDOW.config(background=WINDOWS_OPTIONS['background-compressionImg'])

    MAIN_WINDOW.geometry(str(WINDOWS_OPTIONS['width']) + "x" + str(WINDOWS_OPTIONS['height']))
    MAIN_WINDOW.minsize(980, 590)

    quality_options = {'Bonne +':Image.LANCZOS, 'Bonne':Image.BOX, 'Moyenne':Image.BICUBIC, 'Faible':Image.BILINEAR}
    list_combox_quality = []
    for key in quality_options.keys():
        list_combox_quality.append(key)
    resize_options={'1:1':1, '1:2':1/2, '1:3':1/3, '1:4':1/4, 'Hauteur maximum : 720px':720, 'Hauteur maximum : 1080px':1080, 'Largeur max : 1000px':1000, 'Largeur max : 1920px':1920}
    list_combox_resize = []
    for key in resize_options.keys():
        list_combox_resize.append(key)
    format_options = {'Default':"default", '.png':"png", '.jpg':"jpg", '.webp':"webp"}
    list_combox_format = []
    for key in format_options.keys():
        list_combox_format.append(key)
    # VALEURS PAR DEFAULT :
    compression_options = {'quality':quality_options['Bonne'], 'resize':resize_options['Hauteur maximum : 720px'], 'format':format_options['Default']}

    # Options des bouttons :
    butonsOptionsCompressionImg = {
        'policeButons': "Ebrima",
        'sizeButons': 15,
        'textButon1': "        Image(s)        ",
        'colorButon1': "#E5B5A1",
        'textButon2': "       Compresser       ",
        'colorButon2': "#998B54",
        'textButonHelp': "     Aide     ",
        'colorButonHelp': "#CC8566",
        'textButonMenu': "    Menu    ",
        'colorButonMenu': "#666ECC",
        'textButonExit': "   Quitter   ",
        'colorButonExit': "#E55CE3",
    }

    #Création de la "boîte" frame
    canvas = Frame(MAIN_WINDOW, background=WINDOWS_OPTIONS['background-compressionImg'])
    ####### ---------------------------------------------

    ########### HEADER
    header = Frame(canvas, background=WINDOWS_OPTIONS['background-compressionImg'])
    width = WINDOWS_OPTIONS['width']/9
    height = WINDOWS_OPTIONS['height']/4.8

    image = PhotoImage(file="./assets/logo_alligator_news.png").zoom(2).subsample(17)
    imageCanvas = Canvas(header, width=width, height=height,
                         background=WINDOWS_OPTIONS['background-compressionImg'], border=0, highlightthickness=0)
    imageCanvas.create_image(width/2, height/2, image=image)
    imageCanvas.grid(row=0, column=0, sticky=W)

    titre = Label(header, text='  ~ Outil de compression d\'image(s) ~  ',
                  background=WINDOWS_OPTIONS['background-compressionImg'], font=('Ink Free', 30, 'bold'), fg='#000')  # border=2, relief=SUNKEN
    titre.grid(row=0, column=1, sticky=W)

    image2 = PhotoImage(file="./assets/logo_compression_images.png").zoom(2).subsample(17)
    imageCanvas2 = Canvas(header, width=width, height=height, background=WINDOWS_OPTIONS['background-compressionImg'], border=0, highlightthickness=0)
    imageCanvas2.create_image(width/2, height/2, image=image2)
    imageCanvas2.grid(row=0, column=2, sticky=W)

    header.grid(row=0, column=0, sticky=W)
    ############## ---------------------------------------------

    #Boutons ---------------------------------------------
    buttonsFrame = Frame(canvas, background=WINDOWS_OPTIONS['background-compressionImg'])
    # ---
    getFileButton = Button(buttonsFrame, text=butonsOptionsCompressionImg['textButon1'], command=getFilesImagesAndName, background=butonsOptionsCompressionImg['colorButon1'], font=(
        butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'), fg='black')
    getFileButton.pack(pady=(WINDOWS_OPTIONS['height']/20, WINDOWS_OPTIONS['height']/40))

    comboBoxesFrame = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-compressionImg'])
    # COMBO BOX Qualité
    labelTop1 = Label(comboBoxesFrame, text = "Qualité : ", bg=WINDOWS_OPTIONS['background-compressionImg'], fg='black', font=(butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    labelTop1.grid(row=0, column=0, sticky=W, padx=WINDOWS_OPTIONS['width']/22)
    comboQuality = ttk.Combobox(comboBoxesFrame, values=list_combox_quality, width=int(WINDOWS_OPTIONS['width']/40),
                                    state="readonly", font=(butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons']-5))
    comboQuality.current(1) # Met la première valeure par défaut
    comboQuality.grid(row=1, column=0, sticky=W, padx=WINDOWS_OPTIONS['width']/22)
    comboQuality.bind("<<ComboboxSelected>>", lambda q: setCompressionOptions(compression_options, quality_options=quality_options[comboQuality.get()]))
    # COMBO BOX Resize
    labelTop2 = Label(comboBoxesFrame, text = "Redimensionnement : ", bg=WINDOWS_OPTIONS['background-compressionImg'], fg='black', font=(butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    labelTop2.grid(row=0, column=1, sticky=W, padx=WINDOWS_OPTIONS['width']/22)
    comboResize = ttk.Combobox(comboBoxesFrame, values=list_combox_resize, width=int(WINDOWS_OPTIONS['width']/40),
                                    state="readonly", font=(butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons']-5))
    comboResize.current(4) # Met la première valeure par défaut
    comboResize.grid(row=1, column=1, sticky=W, padx=WINDOWS_OPTIONS['width']/22)
    comboResize.bind("<<ComboboxSelected>>", lambda r : setCompressionOptions(compression_options, resize_options=resize_options[comboResize.get()]))
    # COMBO BOX Format
    labelTop3 = Label(comboBoxesFrame, text = "Format : ", bg=WINDOWS_OPTIONS['background-compressionImg'], fg='black', font=(butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    labelTop3.grid(row=0, column=2, sticky=W, padx=WINDOWS_OPTIONS['width']/22)
    comboFormat = ttk.Combobox(comboBoxesFrame, values=list_combox_format, width=int(WINDOWS_OPTIONS['width']/40),
                                    state="readonly", font=(butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons']-5))
    comboFormat.current(0) # Met la première valeure par défaut
    comboFormat.grid(row=1, column=2, sticky=W, padx=WINDOWS_OPTIONS['width']/22)
    comboFormat.bind("<<ComboboxSelected>>", lambda f : setCompressionOptions(compression_options, format_options=format_options[comboFormat.get()]))
    comboBoxesFrame.pack(pady=(WINDOWS_OPTIONS['height']/30, WINDOWS_OPTIONS['height']/20))

    #Bouton convertion
    convertButton = Button(buttonsFrame, text=butonsOptionsCompressionImg['textButon2'], command=lambda: compressionImg(compression_options), background=butonsOptionsCompressionImg['colorButon2'], fg='black', font=(
        butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    convertButton.pack(pady=WINDOWS_OPTIONS['height']/80)
    # ---
    bottomButonsFrame = Frame(buttonsFrame, background=WINDOWS_OPTIONS['background-compressionImg'])
    helpButton = Button(bottomButonsFrame, text=butonsOptionsCompressionImg['textButonHelp'], command=helpCompressionImg, background=butonsOptionsCompressionImg['colorButonHelp'], fg='black', font=(
        butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    helpButton.grid(row=0, column=0, sticky=W)

    espaceG = Label(bottomButonsFrame, text='              ', background=WINDOWS_OPTIONS['background-compressionImg'])
    espaceG.grid(row=0, column=1, sticky=W)

    # backMenuButton = Button (bottomButonsFrame, text=butonsOptionsCompressionImg['textButonMenu'], command=helpCompressionImg, background=butonsOptionsCompressionImg['colorButonMenu'], fg='black', font=(butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    # backMenuButton.grid(row=0, column=2, sticky=W, padx = WINDOWS_OPTIONS['width']/15)

    espaceD = Label(bottomButonsFrame, text='              ', background = WINDOWS_OPTIONS['background-compressionImg'])
    espaceD.grid(row=0, column=3, sticky=W)

    exitButton = Button(bottomButonsFrame, text=butonsOptionsCompressionImg['textButonExit'], command=exit, background=butonsOptionsCompressionImg['colorButonExit'], fg='black', font=(
        butonsOptionsCompressionImg['policeButons'], butonsOptionsCompressionImg['sizeButons'], 'bold'))
    exitButton.grid(row=0, column=4, sticky=W)
    bottomButonsFrame.pack(pady=(WINDOWS_OPTIONS['height']/10, 0))

    buttonsFrame.grid(row=2, column=0, sticky=S, pady=(WINDOWS_OPTIONS['height']/15, 0))
    ####### ---------------------------------------------

    ########### FOOTER
    footer = Frame(canvas, background = WINDOWS_OPTIONS['background-compressionImg']) # , bd=1, relief=SUNKEN
    labelFooter = Label(footer, text="Powered by Thomas Lépine (thomas.lep4@gmail.com)", background = WINDOWS_OPTIONS['background-compressionImg'], fg='black', font=(butonsOptionsCompressionImg['policeButons'], 10, 'italic'), justify='right')
    labelFooter.pack(anchor=SE)
    footer.grid(row=3, column=0, sticky=SE, pady=((WINDOWS_OPTIONS['height']/25, 0)))
    ############## ---------------------------------------------

    canvas.pack(expand=YES)
    MAIN_WINDOW.mainloop()

def startMenu():
    global MAIN_WINDOW
    MAIN_WINDOW = Tk()
    icoImg = PhotoImage(file="./assets/logo_alligator_news_ico.ico")
    MAIN_WINDOW.title('Alligator tool - Compression d\'image(s)')
    # MAIN_WINDOW.wm_iconbitmap(bitmap ="./assets/logo_alligator_news_ico.ico")
    # MAIN_WINDOW.tk.call('wm', 'iconphoto', MAIN_WINDOW._w, icoImg)
    MAIN_WINDOW.iconbitmap("./assets/logo_alligator_news_ico.ico")
    appCompressionImg() # Lancement de la fenêtre

# ----- START UP :
startMenu() # Lancement du logiciel