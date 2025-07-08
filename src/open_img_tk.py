import tkinter as tk
from PIL import Image, ImageTk


def charger_image(chemin, nb_image = 1, taille=None ,index_debut = 1, miroir=False, extension = ".png", master="root"):
    '''fonction qui sert sert à charger les images. Elle prend en parametre : le chemin d'acces(chemin),
    indice du debut(index_debut) et fin/le nombre d'image(nb_image), un tuple pour la taille de l'image 
    et booléen pour savoir si l'image doit etre tournée ou non
    on utilisera la methode ".extend" pour remplir une liste si besoin'''
    image = []  # contiendra les images
    for i in range(index_debut, index_debut + nb_image):
        imag = Image.open(chemin + str(i) + extension)
        if taille != None:
            imag = imag.resize(taille)
        if miroir == True:
            imag = imag.transpose(Image.FLIP_LEFT_RIGHT)
        image.append(ImageTk.PhotoImage(imag, master=master))
    return image
