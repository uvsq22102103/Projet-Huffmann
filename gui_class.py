##########
# import #
from toolbox import *

#############
# Fonctions #

class App():

    def __init__(self, root: tk.Tk, HEIGHT, WIDTH, NAME) -> None:
        self.NAME = NAME
        self.root = root
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.update()

        #MENU##########
        ###############
        self.menubar = Menu(root)

        self.menuFICHIER = Menu(root, tearoff=0)
        self.menuFICHIER.add_command(label="Ouvrir", command=self.Nouveau)
        self.menuFICHIER.add_command(label="Enregistrer", command= self.Enregistrer)
        self.menubar.add_cascade(label="Fichier", menu=self.menuFICHIER)

        self.menuAIDE = Menu(root, tearoff=0)
        self.menuAIDE.add_command(label="Page GitHub", command=self.webgithub)
        self.menubar.add_cascade(label="Aide", menu=self.menuAIDE)


        self.root.config(menu=self.menubar)

        #NOTEBOOK#########
        ##################
        self.notebookP = ttkb.Notebook(root)
        self.notebookP.pack(pady=10, expand=True, fill="both")

        #FRAME#########
        ###############
        self.labeledframe1 = ttkb.LabelFrame(self.notebookP, text="", bootstyle="info"  )
        self.labeledframe1.pack(fill="both", expand=True, padx=10, pady=10)
        self.labeledframe1.update()

        self.labeledframe1.columnconfigure(1, weight=1)
        self.labeledframe1.rowconfigure(1, weight=1)

        self.frame_not_canva = ttkb.Frame(self.labeledframe1)
        self.frame_not_canva.place(relx=0, rely=0, relwidth=1, relheight=0.40)
        self.frame_not_canva.update()

        self.frame_not_canva.columnconfigure(1, weight=1)
        self.frame_not_canva.rowconfigure(1, weight=1)

        self.frame_canva = ttkb.Frame(self.labeledframe1)
        self.frame_canva.place(relx=0, rely=0.41, relwidth=1, relheight=0.59)
        self.frame_canva.update()

        self.frame_canva.columnconfigure(1, weight=1)
        self.frame_canva.rowconfigure(1, weight=1)

        self.labeledframe2 = ttkb.LabelFrame(self.notebookP, text = "", bootstyle='info')
        self.labeledframe2.pack(fill='both', expand=True, padx=10, pady=10)
        self.labeledframe2.update()

        self.labeledframe2.columnconfigure(1, weight=1)
        self.labeledframe2.rowconfigure(1, weight=1)

        self.framecryptENT = ttkb.Frame(self.labeledframe2)
        self.framecryptENT.place(relx=0, rely=0, relwidth=1, relheight=0.33)
        self.framecryptENT.update()

        self.framecryptENT.columnconfigure(1, weight=1)
        self.framecryptENT.rowconfigure(1, weight=1)

        self.framecryptSOR = ttkb.Frame(self.labeledframe2)
        self.framecryptSOR.place(relx=0, rely=0.34, relwidth=1, relheight=0.66)
        self.framecryptSOR.update()

        self.framecryptSOR.columnconfigure(1, weight=1)
        self.framecryptSOR.rowconfigure(1, weight=1)

        self.notebookP.add(self.labeledframe1, text="General")
        self.notebookP.add(self.labeledframe2, text="Cryptage/Decode")

        #TEXTE#########
        ###############
        self.valueT = "Ecrire/copier votre texte ici"
        self.entreeD1 = ttkb.Text(self.frame_not_canva, font=("Arial 13") )
        self.entreeD1.insert(tk.END, self.valueT)
        self.entreeD1.grid(row=0, rowspan = 2, column=1, columnspan=3, padx=10, pady=10, sticky="new")

        self.entreeD2 = ttkb.Text(self.framecryptENT, font=("Arial 13") )
        self.entreeD2.insert(tk.END, self.valueT)
        self.entreeD2.grid(row=0, rowspan = 3, column=1, padx=10, pady=10, sticky="new")

        self.Sortie = ttkb.Text(self.framecryptSOR, font=("Arial 13"))
        self.Sortie.grid(row = 0, column=0, columnspan = 2, padx=10, pady=10, sticky="sew")

        #BOUTONS#######
        ###############
        self.buttonArbre = ttkb.Button(self.frame_not_canva, text="Créer arbre",  width=40, command=self.mainfct)
        self.buttonArbre.grid(row=0, column=0, padx=10, sticky="nw")

        self.buttoncryptage = ttkb.Button(self.framecryptENT, text="Crypter votre texte", width=40, command=self.cryptage)
        self.buttoncryptage.grid(row=1, column=0, padx=10)

        self.buttonDecrypte = ttkb.Button(self.framecryptENT, text="Décrypter votre texte", width=40, command=self.decryptage)
        self.buttonDecrypte.grid(row=2, column=0, padx=10)

        self.buttoncreacrypt = ttkb.Button(self.framecryptENT, text="Créer un dict de cryptage", width=40, command=self.CreerTXTConv)
        self.buttoncreacrypt.grid(row=0, column=0, padx=10)

        self.buttonlistbox = ttkb.Button(self.frame_not_canva, text = "Ajouter un sommet", width=40,)
        self.buttonlistbox.grid(row=2, column=0)

        #CANVAS########
        ###############
        self.canva1 = ttkb.Canvas(self.frame_canva, borderwidth=10, scrollregion=(0,0,2200,2000), cursor="dot")
        self.canva1.grid(row=0, rowspan = 2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.scrollVERT = ttkb.Scrollbar(self.frame_canva, orient="vertical", bootstyle="primary")
        self.scrollVERT.grid(row=0, rowspan=2, column=3, sticky="nse")

        self.scrollHORI = ttkb.Scrollbar(self.frame_canva, orient="horizontal", bootstyle="primary")
        self.scrollHORI.grid(row=1, column=0, columnspan=2, sticky="wse")

        self.scrollVERT.configure(command=self.canva1.yview)
        self.scrollHORI.configure(command=self.canva1.xview)
        self.canva1.configure(yscrollcommand=self.scrollVERT.set, xscrollcommand=self.scrollHORI.set)

        #LISTBOX#######
        ###############
        self.listbox = Listbox(self.frame_not_canva, bg="grey", selectmode=SINGLE)
        self.listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.scrollLISTB = ttkb.Scrollbar(self.frame_not_canva, orient="vertical", bootstyle="primary")
        self.scrollLISTB.grid(row=1, column=0, pady=10, sticky="nse")

        self.scrollLISTB.configure(command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.scrollLISTB.set)


    def mainfct(self):
        '''Fonction principale de la première page : Dessine l'arbre dans le canva et ajoute les données de cette arbre dans une listbox'''
        self.canva1.delete(tk.ALL)
        self.listbox.delete(0, tk.END)
        texte = self.entreeD1.get("1.0", tk.END)
        arbo = ArbreB.build_from_text(texte, True) # mettre un case cochable pour le booléen

        # Offset + Dessin arbre #
        # HAUTEUR #
        profondeur = arbo.get_profondeur()
        offset_h = 120
        h_canvas = offset_h * profondeur + 60
        # LARGEUR #
        largeur = arbo.get_largeur()
        offset_l = (largeur ** log2(profondeur)) * 10
        l_canvas = int(somme_offsets(offset_l, largeur))*2 + 40
        self.canva1.configure(scrollregion=(0,0,l_canvas,h_canvas))
        arbo.draw(self.canva1, (l_canvas, h_canvas),(offset_l, offset_h))
        #offset = self.entreeD1.delete(0,"end") by Cyriac
        #canvas_size = 2200, 2200
        #arbo.draw(canva1, canvas_size)
        
        #Ecriture proportions
        letter_path = abr_path(arbo)
        var = Variable(value=letter_path)
        self.listbox.config(font= 'arial 12', listvariable=var)


    def cryptage(self):
        '''Fonction qui va crypter un texte à partir d'un dictionnaire de conversion'''
        self.Sortie.delete(1.0 , tk.END)
        f = askopenfile(title="Ouvrir votre texte pour crypter", filetypes=[('txt files','.txt'),('all files','.*')])
        final_txt = encoding(self.entreeD2.get("1.0", tk.END), get_dico(f))
        self.Sortie.insert(tk.END, final_txt)


    def decryptage(self):
        '''Fonction qui va décrypter un texte à partir d'un dictionnaire de conversion'''
        self.Sortie.delete(1.0 , tk.END)
        f = askopenfile(title="Ouvrir votre texte train", filetypes=[('txt files','.txt'),('all files','.*')])
        if f is None:
            return
        final_txt = decoding(self.entreeD2.get("1.0", tk.END).replace("\n",""), get_dico(f))
        self.Sortie.insert(tk.END, final_txt)
        

    def Nouveau(self):
        '''Insérer le contenu d'un fichier texte dans l'entrée principale'''
        self.entreeD1.delete("1.0", tk.END)
        with codecs.open(askopenfilename(title="Ouvrir"), encoding='utf-8') as f:
            texte = f.read()         
            self.entreeD1.insert(tk.END, texte)
            self.mainfct()


    def Enregistrer(self):
        '''Enregistrer le contenu de l'entrée principale dans un fichier texte'''
        f = asksaveasfile(title = "Enregistrer", mode='w', defaultextension=".txt")
        if f is None:
            return
        f.write(self.entreeD1.get("1.0", tk.END))
        f.close()


    def CreerTXTConv(self):
        '''Créer un fichier .txt enregistrant le dictionnaire permettant de décrypter un de crypter un texte'''
        texte = self.entreeD2.get("1.0", tk.END)
        arbre = ArbreB.build_from_freq(proportions(texte, True))
        encodage = arbre.get_encode_dict()
        f = asksaveasfile(title = "Enregistrer", mode='w', defaultextension=".txt")
        if f is None:
            return
        for key, value in encodage.items():
            if key == "\n":
                f.write(f'linebreak,{value}\n')
            else:
                f.write(f'{key},{value}\n')
        f.close()


    def webgithub(self):
        webbrowser.open('https://github.com/uvsq22102103/Projet-Huffmann#guide')

