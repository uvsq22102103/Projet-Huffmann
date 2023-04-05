######################### Importations ##########################

from fonctions import *
from classes import ArbreB
#import tkinter as tk

####################### Programme principal #####################

with open("test_elie.txt") as f:
    texte1 = "".join(f.readlines())

with open("Romeo et Juliette.txt") as f:
    texte2 = "".join(f.readlines())

arbre1 = ArbreB.build_from_freq(proportions(texte1, True))

arbre2 = ArbreB.build_from_freq(proportions(texte2, True))

test = "Ceci est un test de qualite."
encodage = encoding(test ,arbre2.get_encode_dict())
print(f"Encodage de '{test}' via arbre2 : {encodage}")
try:
    print(decoding(encodage,arbre1.get_encode_dict()))
except:
    print("Erreur pour decodage via arbre1")
try:
    print(decoding(encodage,arbre2.get_encode_dict()))
except:
    print("Erreur pour decodage via arbre2")