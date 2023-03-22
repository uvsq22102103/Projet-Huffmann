###################
# imports externes #
import tkinter as tk
from tkinter import Menu, FALSE
import ttkbootstrap as ttkb # install : "pip install ttkbootstrap" in Terminal
from tkinter.messagebox import *
from tkinter.filedialog import *
#from math import log2

################
# imports locaux #
from fonctions import *
from classes import ArbreB, Sommet

#################
# Config fenêtre #
HEIGHT = 1080
WIDTH = 1920
NAME = "Projet Huffman"
#############
# Fonctions #


def crea_abr(text:str):
    characters_proportions = proportions(text)
    arborescence = ArbreB.build_from_freq(characters_proportions)
    return arborescence

def prop_of_abr(arbre:ArbreB):
    dico_conv = arbre.get_encode()
    output = str("")
    if " " in dico_conv:
        dico_conv["espace"] = dico_conv[" "]
        del dico_conv[" "]
    sorted_dict = {key: value for key, value in sorted(dico_conv.items())}
    for (key, value) in sorted_dict.items():
        output += f"'{key}'" + ":" + value + "\n"
    return output

def get_text():
    canva1.delete("all")
    listbox.delete(0, "end")
    texte = entreeT.get()
    arbo = crea_abr(texte)
    #Offset + Dessin arbre
    #hauteurABR = log2(len(arbo.chr_freq))
    #offset = entreeT.delete(0,"end")
    #canva1.configure(scrollregion=)
    #arbo.draw(canva1, offset)
    canva1.create_oval(20,20,100,100)
    #Ecriture proportions
    prop = prop_of_abr(arbo)
    var = tk.Variable(value=prop)
    listbox.config(font= 'arial 12', listvariable=var)


def cursor_change():
    canva1.config(cursor="dot")
    
def Nouveau():
    entreeT.delete(0,"end")
    f = askopenfile(title="Ouvrir", filetypes=[('txt files','.txt'),('all files','.*')])
    texte = f.read()         
    entreeT.insert(0,texte)
    get_text()

def Apropos():
    showinfo("A propos", "Un projet réalisé par Aymeric GOUDOUT et Cyriac THIBAUDEAU \nIN407 S4 2023")

def temp_textT(e):
   entreeT.delete(0,"end")

########
# Main #
root = ttkb.Window(themename="superhero", title=NAME)
root.geometry(f"{WIDTH}x{HEIGHT}")
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.update()

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
#labeledframe1 = ttkb.LabelFrame(root, text="Canva", bootstyle="info"  )
#labeledframe1.grid(row=1, column=0, columnspan=3)
#labeledframe1.update()

#labeledframe2 = ttkb.LabelFrame(root, text = "Prop", bootstyle='info')
#labeledframe2.grid(row=1, column=3, columnspan=1, padx=10, pady=10)
#labeledframe2.update()

#LABEL#########
###############



#ENTREE#########
###############
valueT = "Ecrire/copier votre texte ici"
entreeT = ttkb.Entry(root, justify="left", width=200, font=("Arial 13") )
entreeT.insert(0, valueT)
entreeT.bind("<FocusIn>", temp_textT)
entreeT.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="ne")


#BOUTONS#######
###############
buttonTraiter = ttkb.Button(root, text="Traiter le texte", command=get_text, width=40, bootstyle="primary")
buttonTraiter.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

buttonEncode = ttkb.Button(root, text="Encoder votre texte", width=40)
buttonEncode.grid(row=3, column=0, padx=10, pady=10)

buttonDecode = ttkb.Button(root, text="Décoder votre texte", width=40)
buttonDecode.grid(row=4, column=0, padx=10, pady=10)


#CANVAS########
###############
canva1 = ttkb.Canvas(root,  bg="grey", borderwidth=10, autostyle=FALSE, scrollregion=(0,0,2200,2000))
canva1.bind("<Enter>", cursor_change())
canva1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

scrollVERT = ttkb.Scrollbar(root, orient="vertical", bootstyle="primary")
scrollVERT.grid(row=1, column=3, sticky="nse", pady=10)

scrollHORI = ttkb.Scrollbar(root, orient="horizontal", bootstyle="primary")
scrollHORI.grid(row=2, column=0, columnspan=2, sticky="wse", padx=10)

scrollVERT.configure(command=canva1.yview)
scrollHORI.configure(command=canva1.xview)
canva1.configure(yscrollcommand=scrollVERT.set, xscrollcommand=scrollHORI.set)


#LISTBOX#######
###############
listbox = tk.Listbox(root, bg="grey", selectmode=tk.SINGLE)
listbox.grid(row=1, column=4, columnspan=2, padx=10, pady=10, sticky="nsew")


#PACK##########
###############





root.mainloop()

