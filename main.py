# IMPORT #
import gui_class as gc

# CONSTANTES #
HEIGHT = 1080
WIDTH = 1920
NAME = "Projet Huffman"

# LANCEMENT GUI #
root = gc.ttkb.Window(themename="morph", title=NAME)
app = gc.App(root, HEIGHT, WIDTH, NAME)
root.mainloop()