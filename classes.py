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
        if sommet.value != None:
            self.characters = [sommet.value]

    def fusion(self,abr):
        """Fusionne deux arbres en un puis crée une racine contenant un sommet
        ayant la somme des etiquettes des deux fils pour attribut"""
        fg = self.content.copy()
        fd = abr.content.copy()
        self.content = {"r" : Sommet(round(fg["r"].etiquette + fd["r"].etiquette,2)),
                        "fg" : fg, "fd" : fd}
        self.characters = self.characters + abr.get_characters()
        del abr
        return self
    
    def get_characters(self):
        """Renvoi une liste des charactères que contient cet arbre"""
        return self.characters

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
        for chr in self.get_characters():
            code[chr] = self.search(chr)
        return code


##############################################################################################
