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
arborescence.show()

# HAUTEUR #
profondeur = arborescence.get_profondeur()
offset_h = 50
h_canvas = offset_h * profondeur + 60

print(profondeur, offset_h, h_canvas)

# LARGEUR #
largeur = arborescence.get_largeur()
offset_l = largeur * 60
l_canvas = int(somme_offsets(offset_l, largeur))*2 + 40

print(largeur, offset_l, l_canvas)

# TKINTER INTERFACE #

HEIGHT, WIDTH = h_canvas, l_canvas
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH, bg= "gray")
arborescence.draw(canvas, (WIDTH, HEIGHT),(offset_l, offset_h))
canvas.grid()
root.mainloop()
