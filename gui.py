###################
# imports externes #
import tkinter as tk
from tkinter import Menu, FALSE, Variable, Listbox, SINGLE
import ttkbootstrap as ttkb # install : "pip install ttkbootstrap" in Terminal
from tkinter.messagebox import *
from tkinter.filedialog import *
from math import log2

################
# imports locaux #
from toolbox import *

#################
# Config fenêtre #
HEIGHT = 1080
WIDTH = 1920
NAME = "Projet Huffman"


#############
# Fonctions #

def crea_abr(text:str):
    '''Permet de créer un objet de la classe Arbre à partir d'un texte'''
    return ArbreB.build_from_text(text)

def abr_path(arbre:ArbreB):
    '''Renvoie les chemins des sommets d'un objet de la classe Arbre'''
    dico_conv = arbre.get_encode_dict()
    output = str("")
    if " " in dico_conv:
        dico_conv["espace"] = dico_conv[" "]
        del dico_conv[" "]
    sorted_dict = {key: value for key, value in sorted(dico_conv.items())}
    for (key, value) in sorted_dict.items():
        output += f"'{key}'" + ":" + value + "\n"
    return output

def mainfct():
    '''Fonction principale de la première page : Dessine l'arbre dans le canva et ajoute les données de cette arbre dans une listbox'''
    canva1.delete(tk.ALL)
    listbox.delete(0, tk.END)
    texte = entreeD1.get("1.0", tk.END)
    arbo = ArbreB.build_from_text(texte, True) # mettre un case cochable pour le booléen

    # Offset + Dessin arbre #
    # HAUTEUR #
    profondeur = arbo.get_profondeur()
    offset_h = 120
    h_canvas = offset_h * profondeur + 60
    # LARGEUR #
    largeur = arbo.get_largeur()
    offset_l = (largeur ** log2(profondeur)) * 10
    l_canvas = int(somme_offsets(offset_l, largeur))*2 + 40
    canva1.configure(scrollregion=(0,0,l_canvas,h_canvas))
    arbo.draw(canva1, (l_canvas, h_canvas),(offset_l, offset_h))
    #offset = entreeD1.delete(0,"end") by Cyriac
    #canvas_size = 2200, 2200
    #arbo.draw(canva1, canvas_size)
    
    #Ecriture proportions
    letter_path = abr_path(arbo)
    var = Variable(value=letter_path)
    listbox.config(font= 'arial 12', listvariable=var)

def get_dico(f)-> dict:
    if f is None:
        return
    dico = {}
    for line in f.readlines():
        line = line.replace("\n","")
        if "linebreak" in line:
            line = line.replace("linebreak","\n")
        dico[line[0]] = line[2::]
    f.close()
    return dico

def cryptage():
    '''Fonction qui va crypter un texte à partir d'un dictionnaire de conversion'''
    T.delete(1.0 , tk.END)
    f = askopenfile(title="Ouvrir votre texte pour crypter", filetypes=[('txt files','.txt'),('all files','.*')])
    final_txt = encoding(entreeD2.get("1.0", tk.END), get_dico(f))
    T.insert(tk.END, final_txt)

def decryptage():
    '''Fonction qui va décrypter un texte à partir d'un dictionnaire de conversion'''
    T.delete(1.0 , tk.END)
    f = askopenfile(title="Ouvrir votre texte train", filetypes=[('txt files','.txt'),('all files','.*')])
    if f is None:
        return
    final_txt = decoding(entreeD2.get("1.0", tk.END).replace("\n",""), get_dico(f))
    T.insert(tk.END, final_txt)
    
def Nouveau():
    '''Insérer le contenu d'un fichier texte dans l'entrée principale'''
    entreeD1.delete("1.0", tk.END)
    f = askopenfile(title="Ouvrir", filetypes=[('txt files','.txt'),('all files','.*')])
    texte = f.read()         
    entreeD1.insert(tk.END, texte)
    mainfct()

def Enregistrer(text):
    '''Enregistrer le contenu de l'entrée principale dans un fichier texte'''
    f = asksaveasfile(title = "Enregistrer", mode='w', defaultextension=".txt")
    if f is None:
        return
    text_save = str(text)
    f.write(text_save)
    f.close()

def CreerTXTConv():
    '''Créer un fichier .txt enregistrant le dictionnaire permettant de décrypter un de crypter un texte'''
    texte = entreeD2.get("1.0", tk.END)
    arbre = ArbreB.build_from_freq(proportions(texte, True))
    encodage = arbre.get_encode_dict()
    f = asksaveasfile(title = "Enregistrer", mode='w', defaultextension=".txt")
    if f is None:
        return
    for key, value in encodage.items():
        if key == "\n":
            f.write(f'linebreak,{value}\n')
        else:
            f.write(f'{key},{value}\n')
    f.close()

def Apropos():
    showinfo("A propos", "Un projet réalisé par Aymeric GOUDOUT et Cyriac THIBAUDEAU \nIN407 S4 2023")

########
# Main #
root = ttkb.Window(themename="superhero", title=NAME)
root.geometry(f"{WIDTH}x{HEIGHT}")

root.update()


#MENU##########
###############
menubar = Menu(root)

menu1 = Menu(root, tearoff=0)
menu1.add_command(label="Ouvrir", command=Nouveau)
menu1.add_command(label="Enregistrer", command= lambda: Enregistrer(entreeD1.get("1.0", tk.END)))
menu1.add_command(label="A propos", command=Apropos)
menubar.add_cascade(label="Aide", menu=menu1)

root.config(menu=menubar)


#NOTEBOOK#########
##################
notebookP = ttkb.Notebook(root)
notebookP.pack(pady=10, expand=True, fill="both")


#FRAME#########
###############
labeledframe1 = ttkb.LabelFrame(notebookP, text="General", bootstyle="info"  )
labeledframe1.pack(fill="both", expand=True, padx=10, pady=10)
labeledframe1.update()

labeledframe2 = ttkb.LabelFrame(notebookP, text = "Cryptage/Decode", bootstyle='info')
labeledframe2.pack(fill='both', expand=True, padx=10, pady=10)
labeledframe2.update()

labeledframe1.columnconfigure(1, weight=1)
labeledframe1.rowconfigure(1, weight=1)

labeledframe2.columnconfigure(1, weight=1)
labeledframe2.rowconfigure(1, weight=1)

frame2 = ttkb.Frame(labeledframe2)
frame2.grid(row=1, column=1, columnspan=2, rowspan=2)

notebookP.add(labeledframe1, text="General")
notebookP.add(labeledframe2, text="Cryptage/Decode")


#TEXTE#########
###############
valueT = "Ecrire/copier votre texte ici"
entreeD1 = ttkb.Text(labeledframe1, width=120, font=("Arial 13") )
entreeD1.insert(tk.END, valueT)
entreeD1.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="ne")

entreeD2 = ttkb.Text(labeledframe2,  width=120, font=("Arial 13") )
entreeD2.insert(tk.END, valueT)
entreeD2.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

T = ttkb.Text(frame2, height=50, width=200)
T.pack(side=tk.LEFT, fill=tk.Y, expand=True)



#BOUTONS#######
###############
buttonArbre = ttkb.Button(labeledframe1, text="Créer arbre",  width=40, command=mainfct)
buttonArbre.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

buttoncryptage = ttkb.Button(labeledframe2, text="Crypter votre texte", width=40, command= cryptage)
buttoncryptage.grid(row=0, column=0, padx=10, pady=10)

buttonDecrypte = ttkb.Button(labeledframe2, text="Décrypter votre texte", width=40, command= decryptage)
buttonDecrypte.grid(row=2, column=0, padx=10, pady=10)

buttoncreacrypt = ttkb.Button(labeledframe2, text="Créer un dict de cryptage", width=40, command= CreerTXTConv)
buttoncreacrypt.grid(row=1, column=0, padx=10, pady=10)

#CANVAS########
###############
canva1 = ttkb.Canvas(labeledframe1,  bg="grey", borderwidth=10, autostyle=FALSE, scrollregion=(0,0,2200,2000), cursor="dot")
canva1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

scrollVERT = ttkb.Scrollbar(labeledframe1, orient="vertical", bootstyle="primary")
scrollVERT.grid(row=1, column=3, sticky="nse", pady=10)

scrollHORI = ttkb.Scrollbar(labeledframe1, orient="horizontal", bootstyle="primary")
scrollHORI.grid(row=2, column=0, columnspan=2, sticky="wse", padx=10)

scrollVERT.configure(command=canva1.yview)
scrollHORI.configure(command=canva1.xview)
canva1.configure(yscrollcommand=scrollVERT.set, xscrollcommand=scrollHORI.set)


#LISTBOX#######
###############
listbox = Listbox(labeledframe1, bg="grey", selectmode=SINGLE)
listbox.grid(row=0, rowspan=2, column=4, columnspan=2, padx=10, pady=10, sticky="nsew")



#MAINLOOP######
###############
root.mainloop()

