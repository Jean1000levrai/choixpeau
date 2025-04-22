import tkinter as tk
from PIL import Image, ImageTk
from open_img_tk import charger_image

def create_choixpeau(img_path, x, y, canvas, root):
    global choixpeau_img1
    choixpeau_img.extend(charger_image(master=root, taille=(500, 500), chemin=img_path, nb_image=3, index_debut=1))
    choixpeau_img1 = canvas.create_image(x ,y , image = choixpeau_img[0])

def choixpeau_speaking_anim(i, canvas, timer):
    if timer > 0:
        if i%2 == 0:
            canvas.itemconfig(choixpeau_img1, image = choixpeau_img[0])
        else:
            canvas.itemconfig(choixpeau_img1, image = choixpeau_img[1])
    else:
        canvas.itemconfig(choixpeau_img1, image = choixpeau_img[0])
    canvas.after(300, choixpeau_speaking_anim, i+1, canvas, timer-1)

def get_asked():
    global eleve, new_root
    keys = ["Nom", "Courage", "Loyaute", "Sagesse", "Malice"]
    i = 0
    for entry in entries:
        eleve[keys[i]] = entry.get()
        i+=1
    new_root.destroy()

def ask(canvas):
    global new_root, new_l, entries
    new_root = tk.Tk()
    ok_btn = tk.Button(text="ok",master=new_root, command=get_asked)
    txt = ["Nom", "Courage", "Loyauté", "Sagesse", "Malice"]
    for i in range(len(txt)):
        tk.Label(master = new_root, text = txt[i]).pack()
        entries.append(tk.Entry(master = new_root))
        entries[i].pack()
    print(entries)
    ok_btn.pack()

def saying(say, canvas, i):
    global choixpeau_say, ch_bulle
    if i > 0:
        if choixpeau_say == None:
            ch_bulle = canvas.create_image(500 ,300 , image = choixpeau_img[2])
            choixpeau_say = canvas.create_text(430,200, text=say)
        i = i -1
        canvas.after(300,saying, say, canvas, i)
    else:
        canvas.delete(ch_bulle)
        ch_bulle = None
        canvas.delete(choixpeau_say)
        choixpeau_say = None

choixpeau_img = []
choixpeau_img1 = None
choixpeau_say = None
ch_bulle = None
new_root = None


entries = []

eleve = {'Nom': '', 'Courage': '', 'Loyaute': '', 'Sagesse': '', 'Malice': ''}

