import tkinter as tk
from function import attribution_maison, open_csv
import gui


if __name__ == "__main__":
    # -------------------main-------------------
    db_path = "choixpeauMagique.csv"
    list_csv = open_csv(db_path)

    def ask_btn_func():
        """fonction qui demande à l'apprenti sorcier ses infos"""
        gui.ask(canvas)
        ask_btn.pack_forget()
        speak_btn.pack()
    def speak_btn_func():
        """fonction qui utilise l'animation du choixpeau :
        il donne la maison étant attribuée ou renvoie une erreur si 
        les infos ne sont pas données correctement"""
        gui.choixpeau_speaking_anim(1, canvas,12)
        try:
            gui.saying(f"Hum... Humm...!\nHummmmmmmmmm!! \n{gui.eleve['Nom']}, tu es .......\n{attribution_maison(gui.eleve, list_csv)}!!", canvas,12)
        except : 
            gui.saying("Sois sérieux voyons!", canvas, 12)

    # -------------------gui-------------------
    root = tk.Tk()
    height = 400
    width = 800
    canvas = tk.Canvas(width=width, height=height, master=root)

    speak_btn = tk.Button(text="Speak", master=root, command = speak_btn_func)
    ask_btn = tk.Button(text="ask", master=root, command = ask_btn_func)

    # -------------------launching-------------------
    gui.create_choixpeau("img/choixpeau_img_", 200, 300, canvas, root)
    canvas.pack()
    ask_btn.pack()

    root.mainloop()