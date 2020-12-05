# ------------------------------------------------------
#  Copyright : Thomas LÉPINE  (thomas.lep4@gmail.com)
# ------------------------------------------------------

from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

imageList = []

''' Récupère le/les fichiers : '''
def getFiles ():
    global imageList
    filePathImport = filedialog.askopenfilenames(parent=app, title='Choisissez un/des fichier(s)')
    lstFilePathImport = list(filePathImport) # Transformation de la liste de chaine en liste Python
    imageList = []
    for file in lstFilePathImport :
        img = Image.open(file)
        imageList.append(img.convert('RGB'))

''' Enregistre au format PDF '''
def convertToPdf ():
    global imageList
    filePathExport = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes = [("Fichier PDF","*.pdf")])
    imageList[0].save(filePathExport, save_all=True, append_images=imageList[1:]) # Transformation de la liste d'image en un pdf

''' Quitte l'application : '''
def exit():
    msgBox = messagebox.askquestion('Quitter l\'application','Êtes-vous sûr et certain de vouloir quitter l\'application ?', icon = 'warning')
    if msgBox == 'yes':
       app.destroy()

# Options de la fenêtre
windows = {'width':500, 'height':500, 'background':"#004875"}

# SETUP :
app = tk.Tk()
canvas = tk.Canvas(app, width = windows['width'], height = windows['height'], background = windows['background'], relief = 'raised')
canvas.pack()

label1 = tk.Label(app, text='Outil de conversion\n~ Image(s) -> PDF ~', background='#C8C8C8', font=('Ink Free', 30, 'bold'))
canvas.create_window(windows['width']/2, windows['height']/6, window=label1)

getFileButton = tk.Button(text="        Fichier(s)        ", command=getFiles, background='#E8927C', fg='black', font=('Ebrima', 14, 'bold'))
canvas.create_window(windows['width']/2, windows['height']/2.1, window=getFileButton)

convertButton = tk.Button(text='   Conversion en PDF   ', command=convertToPdf, background='#0B8000', fg='black', font=('Ebrima', 14, 'bold'))
canvas.create_window(windows['width']/2, windows['height']/1.6, window=convertButton)

exitButton = tk.Button (app, text='   Quitter   ', command=exit, background='#CD010D', fg='white', font=('Ebrima', 16, 'bold'))
canvas.create_window(windows['width']/2, windows['height']/1.1, window=exitButton)

app.mainloop()