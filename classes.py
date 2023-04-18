from tkinter import Canvas
from fonctions import *
##############################################################################################

class Sommet():
    """Sommet/Noeud d'un ABR possédant comme attribut étiquette et value,
    si (value == None) alors on peut en conclure que ce noeud est
    père sinon il est feuille"""
    def __init__(self, etiquette: float, value: int=None):
        self.etiquette = etiquette
        self.value = value

    def set_etiquette(self, new_etiquette):
        self.etiquette = new_etiquette


##############################################################################################

class ArbreB():
    """Arbre binaire composé de Sommets/Noeuds"""
    
    liste_erreurs = ['"{}" est déjà présent dans ArbreB']

    def __init__(self, sommet:Sommet):
        self.content = {"r" : sommet, "fg" : None, "fd" : None}
        self.chr_freq = [(sommet.value,sommet.etiquette)]
    
    def build_from_text(text:str, keep_maj:bool):
        return ArbreB.build_from_freq(proportions(text, keep_maj))

    def build_from_freq(chr_freq:list[tuple]):
        liste_arbres = [ArbreB(Sommet(e,v)) for v,e in chr_freq]
        while len(liste_arbres) > 1: #Fusion de la liste d'arbres en un seul et même arbre selon l'étiquette des sommets
            liste_arbres.sort(key=lambda x: x.content["r"].etiquette)
            liste_arbres.append(liste_arbres.pop(0)+liste_arbres.pop(0))
        arborescence = liste_arbres[0]
        #arborescence.chr_freq = chr_freq
        return arborescence


    def fusion(self,abr):
        """Fusionne deux arbres en un puis crée une racine contenant un sommet
        ayant la somme des etiquettes des deux fils pour attribut"""
        fg = self.content.copy()
        fd = abr.content.copy()
        self.content = {"r" : Sommet(round(fg["r"].etiquette + fd["r"].etiquette,2)),
                        "fg" : fg, "fd" : fd}
        for i in abr.chr_freq:
            self.chr_freq.append(i)
        del abr
        return self


    def __add__(self,ArbreB):
        return self.fusion(ArbreB)
    

    def show(self,_n=None):
        """Affiche le contenu de l'arbre dans le terminal"""
        if type(self) == ArbreB:
            ArbreB.show(self.content,0)
        else:
            print(" "*7*_n,(self["r"].value, self["r"].etiquette))
            _n+=1
            if not self["r"].value != None:
                ArbreB.show(self["fd"],_n)
                ArbreB.show(self["fg"],_n)


    def draw(self, canvas:Canvas, canvas_size:tuple[int,int], offset:tuple[int,int], node_size:int=5, __current=None):
        if type(self) == ArbreB:
            __current = (canvas_size[0]/2, 30)
            ArbreB.draw(self.content, canvas, canvas_size, offset, node_size, __current)
        else:
            if self["r"].value == None: #noeud non feuille
                canvas.create_oval(__current[0]-node_size,__current[1]-node_size,__current[0]+node_size,__current[1]+node_size,fill="white")
                loc_fg = (__current[0]-offset[0],__current[1]+offset[1])
                loc_fd = (__current[0]+offset[0],__current[1]+offset[1])
                canvas.create_line(__current[0],__current[1],loc_fg[0],loc_fg[1],fill="black")
                canvas.create_line(__current[0],__current[1],loc_fd[0],loc_fd[1],fill="black")
                offset = (offset[0]/2, +offset[1])
                ArbreB.draw(self["fg"], canvas, canvas_size, offset, node_size, loc_fg)
                ArbreB.draw(self["fd"], canvas, canvas_size, offset, node_size, loc_fd)
            else: # feuille
                canvas.create_oval(__current[0]-node_size,__current[1]-node_size,__current[0]+node_size,__current[1]+node_size, fill="red")


    def search(self,elem:str):
        """Recherche un element ds un l'arbre et renvoi son équivalent binaire 
        selon le grand Oufman"""
        if type(self) == ArbreB: # 
            return ArbreB.search(self.content,elem)
        elif type(self) == dict:
            if self["r"].value == None: # if Sommet non feuille alors continuer
                g = ArbreB.search(self["fg"], elem)
                d = ArbreB.search(self["fd"], elem)
                if g == True:
                    return "0"
                elif d == True:
                    return "1"
                elif type(g) == str:
                    return "0"+g
                elif type(d) == str:
                    return "1"+d
            elif self["r"].value == elem: # if ce Sommet est la feuille recherchée
                return True
            else:
                return False


    def get_encode_dict(self):
        """Retourne un dictionnaire de conversion"""
        code = {}
        for (chr,_) in self.chr_freq:
            code[chr] = self.search(chr)
        return code
    

    def get_profondeur(self, __depth:int=0):
        if type(self) == ArbreB:
            return ArbreB.get_profondeur(self.content)
        elif type(self) == dict:
            if self["r"].value == None: # if Sommet non feuille alors continuer
                fg = ArbreB.get_profondeur(self["fg"], __depth + 1)
                fd = ArbreB.get_profondeur(self["fd"], __depth + 1)
                return fd if fd > fg else fg
            else: # feuille
                return __depth
    
    
    def get_largeur(self, __target:bool = None, __depth:int = 0):
        if type(self) == ArbreB:
            return ArbreB.get_largeur(self.content)
        elif type(self) == dict:
            if __target == None:
                fg = ArbreB.get_largeur(self["fg"], 0, __depth + 1)
                fd = ArbreB.get_largeur(self["fd"], 1, __depth + 1)
                return fg + fd
            elif self["r"].value == None: # if Sommet non feuille alors continuer
                if __target == 0: #gauche
                    return ArbreB.get_largeur(self["fg"], __target, __depth + 1)
                elif __target == 1: #droite
                    return ArbreB.get_largeur(self["fd"], __target, __depth + 1)
            else: #feuille
                return __depth

            
    def supp_chr(self, charactere:str):
        new_chr_freq = []
        for (chr, freq) in self.chr_freq:
            if chr != charactere:
                new_chr_freq.append((chr, freq))
        return ArbreB.build_from_freq(new_chr_freq)
    
    
    def __isub__(self, charactere:str):
        return self.supp_chr(charactere)
    

    def add_sommet(self, sommet:Sommet):
        """chr est un tuple (chr, freq), freq correspond au poids que chr aura dans l'abr"""
        for (chr, freq) in self.chr_freq:
            if chr == sommet.value:
                raise ValueError(ArbreB.liste_erreurs[0].format(chr))
        self.chr_freq.append((sommet.value, sommet.etiquette))
        return ArbreB.build_from_freq(self.chr_freq)
    
    
    def __iadd__(self, sommet: Sommet):
        return self.add_sommet(sommet)
    

    def __str__(self) -> str:
        output = "\n"
        for (chr, freq) in self.chr_freq:
            output += f"{chr} : {freq}\n"
        return output + "\n"


##############################################################################################
