import tkinter as tk
from tkinter import *
import ttkbootstrap as ttkb
from tkinter.messagebox import *
from tkinter.filedialog import *
from fonctions import proportions, merger, translate, get_texte_from_file
from classes import ArbreB, Sommet

root = ttkb.Window(themename="superhero")
HEIGHT = 900
WIDTH = 1600
root.geometry(f"{WIDTH}x{HEIGHT}")

def mainfonc(text):
    characters_proportions = proportions(text)
    liste_arbres = [ArbreB(Sommet(e,v)) for v,e in characters_proportions]
    merger(liste_arbres)
    arborescence = liste_arbres[0]
    dico_conv = arborescence.get_encode()
    print(dico_conv)
    print(arborescence.get_characters())
    return str(dico_conv)

def get_text():
    canva1.delete("all")
    texte = entreeT.get()
    canva1.create_text(HEIGHT//2 , 10,anchor="n", font= 'arial 10', text=mainfonc(texte), )
    print(entreeT.get())


def cursor_change():
    canva1.config(cursor="dot")
    
def Nouveau():
    f = askopenfile(title="Ouvrir", filetypes=[('txt files','.txt'),('all files','.*')])
    texte = f.read()         
    entreeT.insert(0,texte)

def Apropos():
    showinfo("A propos", "Un projet réalisé par Aymeric GOUDOUT et Cyriac THIBAUDEAU \nIN407 S4 2023")

def temp_textT(e):
   entreeT.delete(0,"end")


#MENU##########
###############
menubar = Menu(root)

menu3 = Menu(root, tearoff=0)
menu3.add_command(label="Ouvrir", command=Nouveau)
menu3.add_command(label="A propos", command=Apropos)
menubar.add_cascade(label="Aide", menu=menu3)

root.config(menu=menubar)


#FRAME#########
###############
labeledframe1 = ttkb.LabelFrame(root, text="Canva",height=1000, width=800, bootstyle="info"  )
labeledframe1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


#LABEL#########
###############



#ENTREE#########
###############
valueT = "Ecrire/copier votre texte ici"
entreeT = ttkb.Entry(root, justify="left", width=100, font=("Arial 13") )
entreeT.insert(0, valueT)
entreeT.bind("<FocusIn>", temp_textT)
entreeT.grid(row=0, column=1, padx=10, pady=10, sticky="ne")


#BOUTONS#######
###############
button = ttkb.Button(root, text="Traiter le texte", command=get_text, width=40, bootstyle="primary")
button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")


#CANVAS########
###############
canva1 = ttkb.Canvas(labeledframe1, height=HEIGHT//2, width=WIDTH//2, bg="grey", borderwidth=10, autostyle=FALSE)
canva1.bind("<Enter>", cursor_change())
canva1.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


#PACK##########
###############





root.mainloop()

