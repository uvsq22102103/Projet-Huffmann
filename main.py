######################### Importations ##########################

from fonctions import *
from classes import ArbreB, Sommet
import tkinter as tk # GUI RECURCIVE TEST

#################################################################

training_file = "test_elie.txt" # fichier "de calibrage" sur lequel l'ABR se base pour sa génération.
file_to_encode = "test_elie.txt" # fichier a encoder via l'ABR crée sur le training file.
# possibilité que (training_file = file_to_encode)

####################### Programme principal #####################

with open(training_file) as f:
    texte = "".join(f.readlines())

chr_freq = proportions(texte, True)
arborescence = ArbreB.build_from_freq(chr_freq)

print(arborescence)
arborescence -= "a"
print(arborescence)
arborescence += Sommet(26.5, "a")
arborescence += Sommet(26.5, "a")
print(arborescence)