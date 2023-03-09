import tkinter as tk
from tkinter import *
import ttkbootstrap as ttkb
from tkinter.messagebox import *
from tkinter.filedialog import *
#from fonctionsGUI import *

root = ttkb.Window(themename="superhero")
HEIGHT = 900
WIDTH = 1600
root.geometry("1600x900")

def get_text():
    canva1.delete("all")
    texte = entreeT.get()
    #entreeA.delete(0,"end")
    #entreeA.insert(0, texte)
    canva1.create_text(300, 50, font= 'arial 15', text=texte)
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

#def temp_textA(e):
#   entreeA.delete(0,"end")


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
labeledframe1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
#LABEL#########
###############



#ENTREE#########
###############
valueT = "Ecrire/copier votre texte ici"
entreeT = ttkb.Entry(root, justify="left", width=100, font=("Arial 13") )
entreeT.insert(0, valueT)
entreeT.bind("<FocusIn>", temp_textT)
entreeT.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

#valueA = "Le résultat s'affichera ici !"
#entreeA = ttkb.Entry(root, justify="left",width=100, font=("Arial 13"))
#entreeA.insert(0, CONSTRUCTION ARBRE)
#A lier avec les fonctions d'Aymerique
#entreeA.insert(0, valueA)
#entreeA.bind("<FocusIn>", temp_textA)


#BOUTONS#######
###############
button = ttkb.Button(root, text="Récupérer le texte", command=get_text, width=40, bootstyle="primary")
button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")


#CANVAS########
###############
canva1 = ttkb.Canvas(labeledframe1, height=HEIGHT//2, width=WIDTH//2, bg="grey", borderwidth=10, autostyle=FALSE)
#canva1.focus_set()
canva1.bind("<Enter>", cursor_change())
canva1.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


#PACK##########
###############
#entreeA.pack(pady=20)




root.mainloop()

