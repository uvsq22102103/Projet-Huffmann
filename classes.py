from tkinter import Canvas
from math import log2
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
    def __init__(self, sommet:Sommet):
        self.content = {"r" : sommet, "fg" : None, "fd" : None}
        self.chr_freq = [(sommet.value,sommet.etiquette)]

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
    
    def draw(self, canvas:Canvas, offset=None, __current=None):
        if type(self) == ArbreB:
            if offset == None:
                size = self.__get_size()
                __current = canvas.winfo_reqheight(), 0
                offset = (__current[0]/size,canvas.winfo_reqwidth()/size) 
            ArbreB.draw(self.content, canvas, offset, __current)
        elif type(self) == dict:
            print(__current)
            if self["r"].value == None: # if Sommet non feuille alors continuer
                canvas.create_oval(__current[0]-5,__current[1]-5,__current[0]+5,__current[1]+5,fill="white")
                loc_fg = (__current[0]-offset[0],__current[1]+offset[1]) #pas fini
                loc_fd = (__current[0]+offset[0],__current[1]+offset[1])
                offset = (offset[0]/2, +offset[1]/2)
                ArbreB.draw(self["fg"], canvas, offset,loc_fg)
                ArbreB.draw(self["fd"], canvas, offset,loc_fd)
            else :
                canvas.create_oval(__current[0]-5,__current[1]-5,__current[0]+5,__current[1]+5, fill="red")

                
    
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
    
    def get_encode(self):
        """Retourne un dictionnaire de conversion"""
        code = {}
        for (chr,_) in self.chr_freq:
            code[chr] = self.search(chr)
        return code
    
    def __get_size(self):
        return log2(len(self.chr_freq))


##############################################################################################
