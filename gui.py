import tkinter as tk
from tkinter import *
import ttkbootstrap as ttkb
from tkinter.messagebox import *
from tkinter.filedialog import *
from fonctions import proportions, merger, translate, get_texte_from_file
from classes import ArbreB, Sommet

root = ttkb.Window(themename="superhero")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
hauteur = 900
largeur = 1600
root.geometry(f"{largeur}x{hauteur}")

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
    canva1.create_text( int(canva1.cget("width"))//2 ,int(canva1.cget("height"))-10 , justify='center',anchor="n", font= 'arial 10', text=mainfonc(texte) )
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
labeledframe1 = ttkb.LabelFrame(root, width = largeur, height = hauteur, text="Canva", bootstyle="info"  )
labeledframe1.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


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
canva1 = ttkb.Canvas(labeledframe1, bg="grey", borderwidth=10, autostyle=FALSE)
canva1.bind("<Enter>", cursor_change())
canva1.pack(padx=10, pady=10, expand=True, fill="both" )
#canva1.grid(row=2, column=0, columnspan=2, padx=10,pady=10)

#PACK##########
###############





root.mainloop()

