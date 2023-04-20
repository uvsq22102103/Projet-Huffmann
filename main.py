# IMPORT #
import interface as gui

# CONSTANTES #
HEIGHT = 1080
WIDTH = 1920
NAME = "Projet Huffman"

# LANCEMENT GUI #
root = gui.ttkb.Window(themename="morph", title=NAME)
app = gui.App(root, HEIGHT, WIDTH, NAME)
root.mainloop()