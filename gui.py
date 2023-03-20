###################
# imports externes #
from tkinter import Menu, FALSE
import ttkbootstrap as ttkb # install : "pip install ttkbootstrap" in Terminal
from tkinter.messagebox import *
from tkinter.filedialog import *

################
# imports locaux #
from fonctions import *
from classes import ArbreB, Sommet

#################
# Taille de la fenêtre #
HEIGHT = 900
WIDTH = 1600

#############
# Fonctions #

def text_into_dic_affich(text):
    characters_proportions = proportions(text)
    liste_arbres = [ArbreB(Sommet(e,v)) for v,e in characters_proportions]
    merger(liste_arbres)
    arborescence = liste_arbres[0]
    dico_conv = arborescence.get_encode()
    print(dico_conv)
    return str(dico_conv)


def get_text():
    canva1.delete("all")
    texte = entreeT.get()
    canva1.create_text(HEIGHT//2 , 10,anchor="n", font= 'arial 10', text=text_into_dic_affich(texte) )
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

########
# Main #
root = ttkb.Window(themename="superhero")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)


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
entreeT = ttkb.Entry(root, justify="left", width=100, font=("Arial 13") )
entreeT.insert(0, valueT)
entreeT.bind("<FocusIn>", temp_textT)
entreeT.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="ne")


#BOUTONS#######
###############
button = ttkb.Button(root, text="Traiter le texte", command=get_text, width=40, bootstyle="primary")
button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")


#CANVAS########
###############
canva1 = ttkb.Canvas(root,  bg="grey", borderwidth=10, autostyle=FALSE, scrollregion=(0,0,1200,1000))
canva1.bind("<Enter>", cursor_change())
canva1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

canva2 = ttkb.Canvas(root, bg="grey", borderwidth=10, autostyle=FALSE)
canva2.bind("<Enter>", cursor_change())
canva2.grid(row=1, column=3, columnspan=2, padx=10, pady=10, sticky="nsew")



scrollVERT = ttkb.Scrollbar(root, orient="vertical")
scrollVERT.grid(row=1, column=2, sticky="nse")

scrollHORI = ttkb.Scrollbar(root, orient="horizontal")
scrollHORI.grid(row=2, column=0, columnspan=2, sticky="wse")

scrollVERT.configure(command=canva1.yview)
scrollHORI.configure(command=canva1.xview)
canva1.configure(yscrollcommand=scrollVERT.set, xscrollcommand=scrollHORI.set)

#PACK##########
###############





root.mainloop()

