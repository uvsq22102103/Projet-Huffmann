##########
# import #

from toolbox import *

#############
### CLASS ###

class AppMain():

    """Application pour un utilisateur lambda"""

    def __init__(self, root: tk.Tk, HEIGHT, WIDTH, NAME) -> None:
        self.NAME = NAME
        self.root = root
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.update()
        self.arbre = None

        #MENU##########
        ###############
        self.menubar = Menu(root)

        self.menuFICHIER = Menu(root, tearoff=0)
        self.menuFICHIER.add_command(label="Ouvrir", command=self.import_text)
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
        self.Sortie.grid(row = 0, rowspan=2, column=0, columnspan = 2, padx=10, pady=10, sticky="nsew")

        #BOUTONS#######
        ###############
        self.buttonArbre = ttkb.Button(self.frame_not_canva, text="Afficher l'arbre de Huffman de votre texte",
                                       width=40, command=self.affiche_arbre)
        self.buttonArbre.grid(row=0, column=0, padx=10, sticky="nw")

        self.buttoncryptage = ttkb.Button(self.framecryptENT, text="Encoder votre texte",
                                          width=40, command=self.cryptage)
        self.buttoncryptage.grid(row=1, column=0, padx=10)

        self.buttonDecrypte = ttkb.Button(self.framecryptENT, text="Decoder votre texte binaire",
                                          width=40, command=self.decryptage)
        self.buttonDecrypte.grid(row=2, column=0, padx=10)

        self.buttoncreacrypt = ttkb.Button(self.framecryptENT, text="Enregistrer un dictionnaire\n de cryptage d'Huffman",
                                           width=40, command=self.ExportCodes)
        self.buttoncreacrypt.grid(row=0, column=0, padx=10)

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

        self.scrollLISTA = ttkb.Scrollbar(self.frame_not_canva, orient="horizontal", bootstyle="primary")
        self.scrollLISTA.grid(row=2, column=0, sticky="wse")

        self.scrollLISTB = ttkb.Scrollbar(self.frame_not_canva, orient="vertical", bootstyle="primary")
        self.scrollLISTB.grid(row=1, column=0, pady=10, sticky="nse")

        self.scrollLISTA.configure(command=self.listbox.xview)
        self.scrollLISTB.configure(command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.scrollLISTB.set, xscrollcommand=self.scrollLISTA.set)


    def affiche_arbre(self):
        '''Fonction principale de la première page : Dessine
        l'arbre dans le canva et ajoute les données de cette arbre dans une listbox'''
        self.canva1.delete(tk.ALL)
        self.listbox.delete(0, tk.END)
        texte = self.entreeD1.get("1.0", tk.END)[:-1] # <=== pour retirer le \n de fin de texte
        self.arbre = ArbreB_Huffmann.build_from_text(texte)

        ## Offset + Dessin arbre ##

        # HAUTEUR #
        profondeur = self.arbre.get_profondeur()
        offset_h = 120
        h_canvas = offset_h * (profondeur+1)
        
        # LARGEUR #
        largeur = self.arbre.get_largeur()
        offset_l = (largeur ** log2(profondeur)) * 10
        l_canvas = int(somme_offsets(offset_l, largeur))*2 + 40
        self.canva1.configure(scrollregion=(0,0,l_canvas,h_canvas))
        self.arbre.draw(self.canva1, (l_canvas, h_canvas),(offset_l, offset_h))
        
        ## Création d'une listebox qui affiche le chemin associé aux lettres ##
        self.listbox.config(font= 'arial 12', listvariable=Variable(value=self.arbre.__str__()))


    def cryptage(self):
        '''Fonction qui va crypter un texte à partir d'un dictionnaire de conversion'''
        self.Sortie.delete(1.0 , tk.END)
        dico = get_dico_from_huffman_save()
        texte = self.entreeD2.get("1.0", tk.END)[:-1] # <=== pour retirer le \n de fin de texte
        texte_encodé = encoding(dico, texte)
        showinfo(title="Encodage",
                 message=f"texte compressé à {pourcentage_compression(texte, texte_encodé)}%")
        self.Sortie.insert(tk.END, texte_encodé)


    def decryptage(self):
        '''Fonction qui va décrypter un texte à partir d'un dictionnaire de conversion'''
        self.Sortie.delete(1.0 , tk.END)
        dico = get_dico_from_huffman_save()
        final_txt = decoding(dico, self.entreeD2.get("1.0", tk.END).replace("\n",""))
        self.Sortie.insert(tk.END, final_txt)
        

    def import_text(self):
        '''Insérer le contenu d'un fichier texte dans self.entreeD1'''
        self.entreeD1.delete("1.0", tk.END)
        texte = file_dialog(action="r",filetypes= [('txt files','.txt'),('all files','.*')])      
        self.entreeD1.insert(tk.END, texte)
        self.affiche_arbre()


    def ExportCodes(self):
        '''Exporte un fichier de conversion de la forme
        n*(ord(charactere) code)'''
        texte = self.entreeD2.get("1.0", tk.END)[:-1] # <=== pour retirer le \n de fin de texte
        arbre = ArbreB_Huffmann.build_from_dico(proportions(texte))
        encodage = arbre.get_encode_dict()
        checksum = encodage["checksum"]
        del encodage["checksum"]
        output = " ".join([f'{ord(charactere)} {code}' for charactere, code in encodage.items()])
        output += "\n" + checksum
        file_dialog(action="w", text=output, extension=".huffmann")


    def webgithub(self):
        webbrowser.open('https://github.com/uvsq22102103/Projet-Huffmann#guide')


    def Apropos(self):
        showinfo("A propos", "Un projet réalisé par Aymeric GOUDOUT et Cyriac THIBAUDEAU \nIN407 S4 2023")



class AppUnittest():

    """Application dédiée à l'unittest"""

    def __init__(self, root:tk.Tk, height, width, name) -> None:
        self.arbre = None
        ## Partie GUI ##
        # Racine #
        self.root = root
        self.root.title(name + " - Unitest")
        self.root.geometry(f"{width}x{height}")

        # Menu #
        self.menu = Menu(root)

        self.menuARBRE = Menu(root, tearoff=0)
        self.menuARBRE.add_command(label="Créer à partir d'un texte", command=self.create_from_text)
        self.menuARBRE.add_command(label="Rajout de texte", command=self.add_from_text)
        self.menuARBRE.add_command(label="Décomposition", command=self.decomposer)

        self.menu.add_cascade(label="Arbre", menu= self.menuARBRE)
        
        self.menuSOMMET = Menu(root, tearoff=0)
        self.menuSOMMET.add_command(label="Ajouter", command=self.add_sommet)
        self.menuSOMMET.add_command(label="Retirer", command=self.rm_sommet)

        self.menu.add_cascade(label="Sommet", menu= self.menuSOMMET)

        self.root.config(menu=self.menu)

        # Frame #
        self.frameprincipale = tk.Frame(self.root)
        self.frameprincipale.pack(fill="both", expand=True, padx=10, pady=10)

        self.frameprincipale.columnconfigure(1, weight=1)
        self.frameprincipale.rowconfigure(1, weight=1)
        self.frameprincipale.update()

        # Label #
        self.labelAffichage = tk.Label(self.frameprincipale, text=">Pas d'arbre<")
        self.labelAffichage.grid(row = 0, column = 0, sticky="nsew", pady=10)

        # Canva #
        self.canvas1 = tk.Canvas(self.frameprincipale, borderwidth=10, scrollregion=(0,0,2200,2000), cursor="dot", bg="grey")
        self.canvas1.grid(row=0, rowspan=2, column=1, padx=10, pady=10, sticky="nsew")

        self.scrollVERT = tk.Scrollbar(self.frameprincipale, orient="vertical",width=20)
        self.scrollVERT.grid(row=0, rowspan=2, column=2, sticky="nse")

        self.scrollHORI = tk.Scrollbar(self.frameprincipale, orient="horizontal",width=20)
        self.scrollHORI.grid(row=2, column=1, columnspan=2, sticky="nwe")

        self.scrollVERT.configure(command=self.canvas1.yview)
        self.scrollHORI.configure(command=self.canvas1.xview)
        self.canvas1.configure(yscrollcommand=self.scrollVERT.set, xscrollcommand=self.scrollHORI.set)


    def affichage(self):
        self.canvas1.delete("all")
        if self.arbre != None:
            texte = self.arbre.__str__()
            self.labelAffichage.config(text=texte)
            ## Offset + Dessin arbre ##

            # HAUTEUR #
            profondeur = self.arbre.get_profondeur()
            offset_h = 120
            h_canvas = offset_h * (profondeur+1)
            
            # LARGEUR #
            largeur = self.arbre.get_largeur()
            offset_l = (largeur ** log2(profondeur)) * 10
            l_canvas = int(somme_offsets(offset_l, largeur))*2 + 40
            self.canvas1.configure(scrollregion=(0,0,l_canvas,h_canvas))
            self.arbre.draw(self.canvas1, (l_canvas, h_canvas),(offset_l, offset_h))
        else:
            self.labelAffichage.config(text=">Pas d'arbre<")

    
    def rm_sommet(self):
        charactère = ""
        while len(charactère) != 1:
            charactère = askstring(title="Enlever un sommet",
                                prompt="Saisir un Charactère",
                                initialvalue="x")
        self.arbre -= charactère
        self.affichage()


    def add_sommet(self):
        charactère = ""
        while len(charactère) != 1:
            charactère = askstring(title="Ajouter un sommet",
                                prompt="Saisir un Charactère",
                                initialvalue="x")
        poids = 0
        while poids < 1:
            poids = askinteger(title="Ajouter un sommet",
                                prompt="Saisir un poids",
                                initialvalue=5)
        sommet = Sommet(poids, charactère)
        if self.arbre == None:
            self.arbre = ArbreB_Huffmann(sommet)
        else:
            self.arbre += sommet
        self.affichage()
    
    
    def create_from_text(self):
        texte = askstring(title="Créer un nouvel arbre depuis un texte",
                          prompt="Veuillez entrer un texte quelconque")
        self.arbre = ArbreB_Huffmann.build_from_text(text=texte)
        self.affichage()
    
    
    def add_from_text(self):
        if self.arbre != None:
            texte = askstring(title="Ajouter à cet arbre du texte",
                            prompt="Veuillez entrer un texte quelconque")
            self.arbre = self.arbre + ArbreB_Huffmann.build_from_text(texte)
            self.affichage()
    

    def decomposer(self):
        if self.arbre != None:
            g, d = self.arbre.decomposition()
            q = askinteger(title="Choisir la partie de l'arbre à conserver",
                        prompt="Garder le côté gauche (1) ou droit (2) ?")
            if q == 1:
                self.arbre = g
            elif q == 2:
                self.arbre = d
            self.affichage()
