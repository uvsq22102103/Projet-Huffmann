# IMPORT #
import interface as gui

# CONSTANTES #
HEIGHT = 1080
WIDTH = 1920
NAME = "Projet Huffman"

# LANCEMENT GUI #

q = None
while q not in [1, 2]:
    q = gui.askinteger(NAME, prompt="Interface principale (1) ou Interface Unitest (2) ?",
                       initialvalue=1)
if q == 1:
    root = gui.ttkb.Window(themename="morph", title=NAME)
    app = gui.AppMain(root, HEIGHT, WIDTH, NAME)
elif q == 2:
    root = gui.tk.Tk()
    app = gui.AppUnitest(root)
root.mainloop()