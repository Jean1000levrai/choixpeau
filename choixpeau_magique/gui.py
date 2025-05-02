import tkinter as tk
from PIL import Image, ImageTk
from open_img_tk import charger_image

def create_choixpeau(img_path, x, y, canvas, root):
    """fonction chargé de créer le choixpeau fonctionnel"""
    global choixpeau_img1
    choixpeau_img.extend(charger_image(master=root, taille=(500, 500), chemin=img_path, nb_image=3, index_debut=1))
    choixpeau_img1 = canvas.create_image(x ,y , image = choixpeau_img[0])

def choixpeau_speaking_anim(i, canvas, timer = 10):
    """fonction qui contrôle l'animation du choixpeau"""
    # le fait parler lors du compteur
    if timer > 0:
        if i%2 == 0:
            canvas.itemconfig(choixpeau_img1, image = choixpeau_img[0])
        else:
            canvas.itemconfig(choixpeau_img1, image = choixpeau_img[1])
    # le remet à son état initial lorsqu'il a fini de parler
    else:
        canvas.itemconfig(choixpeau_img1, image = choixpeau_img[0])
    canvas.after(300, choixpeau_speaking_anim, i+1, canvas, timer-1)


def ask(canvas):
    """fonction qui fait apparaître une nouvelle fenêtre
    où l'apprenti sorcier peut rentrer ces infos"""
    global new_root, entries
    new_root = tk.Tk()
    ok_btn = tk.Button(text="ok",master=new_root, command=get_asked)
    txt = ["Nom", "Courage", "Loyauté", "Sagesse", "Malice"]
    for i in range(len(txt)):
        tk.Label(master = new_root, text = txt[i]).pack()
        entries.append(tk.Entry(master = new_root))
        entries[i].pack()
    ok_btn.pack()

def get_asked():
    """fonction qui récupère les infos de l'apprenti sorcier"""
    global eleve, new_root
    keys = ["Nom", "Courage", "Loyaute", "Sagesse", "Malice"]
    i = 0
    # on parcourt toutes les entrées
    for entry in entries:
        eleve[keys[i]] = entry.get()    # stocke dans un dictionnaire ces infos
        i+=1
    new_root.destroy()

def saying(say, canvas, timer):
    """fonction qui fait apparaître le verdict du choixpeau"""
    global choixpeau_say, ch_bulle
    # bulle tant que le timer n'est pas écoulé
    if timer > 0:
        # crée la bulle si elle n'éxiste pas
        if choixpeau_say == None:
            ch_bulle = canvas.create_image(500 ,300 , image = choixpeau_img[2])
            choixpeau_say = canvas.create_text(430,200, text=say)
        timer = timer -1
        canvas.after(300,saying, say, canvas, timer)
    else:
        # détruit la bulle à la fin du timer
        canvas.delete(ch_bulle)
        ch_bulle = None
        canvas.delete(choixpeau_say)
        choixpeau_say = None

# futures images
choixpeau_img = []
choixpeau_say = None
ch_bulle = None
new_root = None
entries = []
# dictionnaire des infos de l'apprenti sorcier
eleve = {'Nom': '', 'Courage': '', 'Loyaute': '', 'Sagesse': '', 'Malice': ''}

