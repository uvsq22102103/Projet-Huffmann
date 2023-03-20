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

chr_freq = proportions(texte)
arborescence = ArbreB.build_from_freq(chr_freq)
# END #
# GUI RECURCIVE TEST #
HEIGHT, WIDTH = 600, 600
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH, bg= "black")
arborescence.draw(canvas, (HEIGHT,WIDTH))
canvas.grid()
root.mainloop()