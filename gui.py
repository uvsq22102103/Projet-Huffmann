###################
# imports externes #
import tkinter as tk
from tkinter import Menu, FALSE, Variable, Listbox, SINGLE
import ttkbootstrap as ttkb # install : "pip install ttkbootstrap" in Terminal
from tkinter.messagebox import *
from tkinter.filedialog import *
from math import log2
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

def abr_path(arbre:ArbreB):
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
    canva1.delete("all")
    listbox.delete(0, "end")
    texte = entreeD1.get()
    arbo = crea_abr(texte)

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

def cryptage():
    T.delete(1.0 , tk.END)
    f = askopenfile(title="Ouvrir votre texte train", filetypes=[('txt files','.txt'),('all files','.*')])
    if f is None:
        return
    texte = f.read()
    txt = entreeD2.get().lower()
    #abr = crea_abr(texte)
    dic_conv = texte
    final_txt = encoding(txt, dic_conv)
    T.insert(tk.END, final_txt)

def decryptage(txt):
    pass

def cursor_change():
    canva1.config(cursor="dot")
    
def Nouveau():
    entreeD1.delete(0,"end")
    f = askopenfile(title="Ouvrir", filetypes=[('txt files','.txt'),('all files','.*')])
    texte = f.read()         
    entreeD1.insert(0,texte)
    mainfct()

def Enregistrer(text):
    f = asksaveasfile(title = "Enregistrer", mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text_save = str(text)
    f.write(text_save)
    f.close()

def CreerTXTConv():
    texte = entreeD2.get().lower()
    arbre = ArbreB.build_from_freq(proportions(texte, True))
    encodage = arbre.get_encode_dict()
    f = asksaveasfile(title = "Enregistrer", mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text_save = str(encodage)
    f.write(text_save)
    f.close()

def Apropos():
    showinfo("A propos", "Un projet réalisé par Aymeric GOUDOUT et Cyriac THIBAUDEAU \nIN407 S4 2023")

def temp_textT(e):
   entreeD1.delete(0,"end")

def temp_textT2(e):
    entreeD2.delete(0, "end")

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
menu1.add_command(label="Enregistrer", command= lambda: Enregistrer(entreeD1.get()))
menu1.add_command(label="A propos", command=Apropos)
menu1.add_command(label="Créer texte de conversion", command=CreerTXTConv)
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
frame2.grid(row=2, column=0, columnspan=3)

notebookP.add(labeledframe1, text="General")
notebookP.add(labeledframe2, text="Cryptage/Decode")


#TEXTE#########
###############
T = tk.Text(frame2, height=50, width=300,)
T.pack(side=tk.LEFT, fill=tk.Y, expand=True)

S = tk.Scrollbar(frame2)
S.pack(side=tk.RIGHT, fill=tk.Y)

S.config(command=T.yview)
T.config(yscrollcommand=S.set)

quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(tk.END, quote)


#ENTREE########
###############
valueT = "Ecrire/copier votre texte ici"
entreeD1 = ttkb.Entry(labeledframe1, justify="left", width=120, font=("Arial 13") )
entreeD1.insert(0, valueT)
entreeD1.bind("<Button-1>", temp_textT)
entreeD1.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="ne")

entreeD2 = ttkb.Entry(labeledframe2, justify="left", width=120, font=("Arial 13") )
entreeD2.insert(0, valueT)
entreeD2.bind("<Button-1>", temp_textT2)
entreeD2.grid(row=0, column=1, padx=10, pady=10, sticky="ne")


#BOUTONS#######
###############
buttonArbre = ttkb.Button(labeledframe1, text="Créer arbre",  width=40, command=mainfct)
buttonArbre.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

buttoncryptage = ttkb.Button(labeledframe2, text="Crypter votre texte", width=40, command= cryptage)
buttoncryptage.grid(row=0, column=0, padx=10, pady=10)

buttonDecrypte = ttkb.Button(labeledframe2, text="Décrypter votre texte", width=40)
buttonDecrypte.grid(row=0, column=2, padx=10, pady=10)

buttoncreacrypt = ttkb.Button(labeledframe2, text="Créer un dict de cryptage", width=40, command= CreerTXTConv)
buttoncreacrypt.grid(row=1, column=0, padx=10, pady=10)

#CANVAS########
###############
canva1 = ttkb.Canvas(labeledframe1,  bg="grey", borderwidth=10, autostyle=FALSE, scrollregion=(0,0,2200,2000))
canva1.bind("<Enter>", cursor_change())
canva1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

scrollVERT = ttkb.Scrollbar(labeledframe1, orient="vertical", bootstyle="primary")
scrollVERT.grid(row=1, column=3, sticky="nse", pady=10)

scrollHORI = ttkb.Scrollbar(labeledframe1, orient="horizontal", bootstyle="primary")
scrollHORI.grid(row=2, column=0, columnspan=2, sticky="wse", padx=10)

scrollVERT.configure(command=canva1.yview)
scrollHORI.configure(command=canva1.xview)
canva1.configure(yscrollcommand=scrollVERT.set, xscrollcommand=scrollHORI.set)

#canva2 = ttkb.Canvas(labeledframe2,  bg="grey", borderwidth=10 , autostyle=FALSE)
#canva2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
#canva2.create_text(100, 20, text="Ceci est un text test")

#LISTBOX#######
###############
listbox = Listbox(labeledframe1, bg="grey", selectmode=SINGLE)
listbox.grid(row=1, column=4, columnspan=2, padx=10, pady=10, sticky="nsew")



#MAINLOOP######
###############
root.mainloop()

