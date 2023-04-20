import tkinter as tk
from tkinter import Menu, FALSE, Variable, Listbox, SINGLE
import ttkbootstrap as ttkb # install : "pip install ttkbootstrap" in Terminal
from tkinter.messagebox import *
from tkinter.filedialog import *
from math import log2
import codecs
import webbrowser
##############################################################################################

class Sommet():
    """Sommet/Noeud d'un ABR possédant comme attribut étiquette et value,
    si (value == None) alors on peut en conclure que ce noeud est
    père sinon il est feuille"""
    def __init__(self, poids: float, charactere: str=None):
        self.poids = poids
        self.charactere = charactere

    def set_poids(self, new_poids:float):
        self.poids = new_poids
    
    def get_poids(self):
        return self.poids
    
    def set_charactere(self, charactere:str):
        self.charactere = charactere
    
    def get_charactere(self):
        return self.charactere
    


##############################################################################################

class ArbreB_Huffmann():
    """Arbre binaire composé de Sommets/Noeuds"""
    liste_erreurs = ['"{}" est déjà présent dans cet arbre de Huffmann']

    def __init__(self, sommet:Sommet):
        self.content = {"r" : sommet, "fg" : None, "fd" : None}
        self.chr_freq = [(sommet.get_charactere(),sommet.get_poids())]
    
    def build_from_text(text:str, keep_maj:bool):
        return ArbreB_Huffmann.build_from_freq(proportions(text, keep_maj))
    
    def get_poids(self):
        return self.content["r"].get_poids()

    def build_from_freq(chr_freq:list[tuple]):
        liste_arbres = [ArbreB_Huffmann(Sommet(e,v)) for v,e in chr_freq]
        while len(liste_arbres) > 1: #Fusion de la liste d'arbres en un seul et même arbre selon l'étiquette des sommets
            liste_arbres.sort(key=lambda x: x.get_poids())
            liste_arbres.append(liste_arbres.pop(0)+liste_arbres.pop(0))
        arborescence = liste_arbres[0]
        #arborescence.chr_freq = chr_freq
        return arborescence


    def fusion(self,abr:"ArbreB_Huffmann"):
        """Fusionne deux arbres en un puis crée une racine contenant un sommet
        ayant la somme des etiquettes des deux fils pour attribut"""
        fg = self.content.copy()
        fd = abr.content.copy()
        self.content = {"r" : Sommet(round(fg["r"].get_poids() + fd["r"].get_poids(),2)),
                        "fg" : fg, "fd" : fd}
        for i in abr.chr_freq:
            self.chr_freq.append(i)
        del abr
        return self


    def __add__(self,ArbreB):
        return self.fusion(ArbreB)
    

    def show(self,_n=None):
        """Affiche le contenu de l'arbre dans le terminal"""
        if type(self) == ArbreB_Huffmann:
            ArbreB_Huffmann.show(self.content,0)
        else:
            print(" "*7*_n,(self["r"].get_charactere(), self["r"].get_poids()))
            _n+=1
            if not self["r"].get_charactere() != None:
                ArbreB_Huffmann.show(self["fd"],_n)
                ArbreB_Huffmann.show(self["fg"],_n)


    def draw(self, canvas:tk.Canvas, canvas_size:tuple[int,int], offset:tuple[int,int], node_size:int=5, __current=None):
        if type(self) == ArbreB_Huffmann:
            __current = (canvas_size[0]/2, 30)
            ArbreB_Huffmann.draw(self.content, canvas, canvas_size,
                                 offset, node_size, __current)
        else:
            if self["r"].get_charactere() == None: #noeud non feuille
                canvas.create_oval(__current[0]-node_size,__current[1]-node_size,
                                   __current[0]+node_size,__current[1]+node_size,fill="white")
                loc_fg = (__current[0]-offset[0],__current[1]+offset[1])
                loc_fd = (__current[0]+offset[0],__current[1]+offset[1])
                canvas.create_line(__current[0],__current[1],loc_fg[0],loc_fg[1],fill="black")
                canvas.create_line(__current[0],__current[1],loc_fd[0],loc_fd[1],fill="black")
                offset = (offset[0]/2, +offset[1])
                ArbreB_Huffmann.draw(self["fg"], canvas, canvas_size, offset, node_size, loc_fg)
                ArbreB_Huffmann.draw(self["fd"], canvas, canvas_size, offset, node_size, loc_fd)
            else: # feuille
                canvas.create_oval(__current[0]-node_size,__current[1]-node_size,
                                   __current[0]+node_size,__current[1]+node_size, fill="red")
                canvas.create_text(__current[0],__current[1]+(4*node_size), text=self["r"].get_charactere(), fill="black")


    def search(self, charactere:str):
        """Recherche un element dans un l'arbre et renvoi son équivalent binaire 
        selon le grand Oufman"""
        if type(self) == ArbreB_Huffmann: # 
            return ArbreB_Huffmann.search(self.content, charactere)
        elif type(self) == dict:
            if self["r"].get_charactere() == None: # if Sommet non feuille alors continuer
                g = ArbreB_Huffmann.search(self["fg"], charactere)
                d = ArbreB_Huffmann.search(self["fd"], charactere)
                if g == True:
                    return "0"
                elif d == True:
                    return "1"
                elif type(g) == str:
                    return "0"+g
                elif type(d) == str:
                    return "1"+d
            elif self["r"].get_charactere() == charactere: # if ce Sommet est la feuille recherchée
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
        if type(self) == ArbreB_Huffmann:
            return ArbreB_Huffmann.get_profondeur(self.content)
        elif type(self) == dict:
            if self["r"].get_charactere() == None: # if Sommet non feuille alors continuer
                fg = ArbreB_Huffmann.get_profondeur(self["fg"], __depth + 1)
                fd = ArbreB_Huffmann.get_profondeur(self["fd"], __depth + 1)
                return fd if fd > fg else fg
            else: # feuille
                return __depth
    
    
    def get_largeur(self, __target:bool = None, __depth:int = 0):
        if type(self) == ArbreB_Huffmann:
            return ArbreB_Huffmann.get_largeur(self.content)
        elif type(self) == dict:
            if __target == None:
                fg = ArbreB_Huffmann.get_largeur(self["fg"], 0, __depth + 1)
                fd = ArbreB_Huffmann.get_largeur(self["fd"], 1, __depth + 1)
                return fg + fd
            elif self["r"].get_charactere() == None: # if Sommet non feuille alors continuer
                if __target == 0: #gauche
                    return ArbreB_Huffmann.get_largeur(self["fg"], __target, __depth + 1)
                elif __target == 1: #droite
                    return ArbreB_Huffmann.get_largeur(self["fd"], __target, __depth + 1)
            else: #feuille
                return __depth


    def supp_chr(self, charactere:str):
        """Permet de supprimer un Sommet comprenant
        le charactère spécifié de l'arbre actuel en
        gardant la propriété du codage de Hoffmann"""
        new_chr_freq = []
        for (chr, freq) in self.chr_freq:
            if chr != charactere:
                new_chr_freq.append((chr, freq))
        return ArbreB_Huffmann.build_from_freq(new_chr_freq)
    
    
    def __isub__(self, charactere:str):
        return self.supp_chr(charactere)
    

    def add_sommet(self, sommet:Sommet):
        """Permet d'ajouter un sommet dans l'arbre
        en conservant les propriétés du codage de Huffmann"""
        for (chr, _) in self.chr_freq:
            if chr == sommet.charactere:
                raise ValueError(ArbreB_Huffmann.liste_erreurs[0].format(chr))
        self.chr_freq.append((sommet.charactere, sommet.poids))
        return ArbreB_Huffmann.build_from_freq(self.chr_freq)
    
    
    def __iadd__(self, sommet: Sommet):
        return self.add_sommet(sommet)
    

    def __str__(self) -> str:
        output = "\n"
        for (chr, freq) in self.chr_freq:
            output += f"{chr} : {freq}\n"
        return output + "\n"


def proportions(texte:str,keep_maj = False):
    """Prend un texte en argument et retourne les
    occurences par Charactères (= chr) de son content.\n
    str => list(n*tuple(chr,occurences))"""
    if not keep_maj:
        texte = texte.lower()
    proportion = {}
    for i in texte:
        if i in proportion.keys():
            proportion[i] += 1
        else:
            proportion[i] = 1
    len_texte = len(texte)
    for i in proportion.keys():
        proportion[i] = round((proportion[i]/len_texte)*100,2)
    return sorted(proportion.items(), key= lambda item: item[1])


def encoding(texte:str, conversion:dict):
    """Encode un texte selon un dictionnaire de conversion"""
    output = ""
    try :
        for i in texte:
            output += conversion[i]
        return output
    except :
        raise ValueError(f"le charactère <{i}> n'existe pas dans le text d'entraînement")


def decoding(texte:str, conversion:dict):
    """Decode un texte selon un dictionnaire de conversion"""
    conversion_reversed = {}
    for (key, value) in conversion.items():
        conversion_reversed[value] = key
    output = ""
    i, j = 0, 1
    keys = conversion_reversed.keys()
    while i < len(texte):
        while texte[i:j] not in keys:
            j += 1
            if j > len(texte):
                raise ValueError(f"Vous essayez de decoder un texte avec le mauvais dictionnaire")
        output += conversion_reversed[texte[i:j]]
        i = j
        j = i+1
    return output


def get_key_from_value(d:dict, val:str):
    """Reviens à inverser key et value"""
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    else:
        raise ValueError


def get_texte_from_file(path:str):
    """Prend le chemin d'un fichier et renvoi son contenu en str"""
    with open(path) as f:
        texte = "".join(f.readlines()).lower()
    return texte


def somme_offsets(offset:int, hauteurABR:int, k:float=2.0):
    return offset + somme_offsets(offset/k, hauteurABR-1) if hauteurABR > 1 else offset


def get_dico(texte:str)-> dict:
    dico = {}
    liste = texte.split()
    for i in range(0,len(liste), 2):
        dico[chr(int(liste[i]))] = liste[i+1]
    return dico


def abr_path(arbre:ArbreB_Huffmann):
    '''Renvoie les chemins des sommets d'un objet de la classe Arbre'''
    dico_conv = arbre.get_encode_dict()
    output = str("")
    if " " in dico_conv:
        dico_conv["espace"] = dico_conv[" "]
        del dico_conv[" "]
    if "\n" in dico_conv:
        dico_conv["linebreak"] = dico_conv["\n"]
        del dico_conv["\n"]
    sorted_dict = {key: value for key, value in sorted(dico_conv.items())}
    for (key, value) in sorted_dict.items():
        output += f"'{key}'" + ":" + value + "\n"
    return output

def file_dialog(action:str, filetypes:list=[], text:str="", extension:str=""):
    """Permet de lire ou d'écrire sur fichier"""
    if action == "r":
        file = codecs.open(askopenfilename(title="Ouvrir", filetypes=filetypes), encoding='utf-8')
        output = "".join(file.readlines())
        file.close()
        return output
    elif action == "w":
        file = asksaveasfile(title ="Enregistrer", mode='w', defaultextension=extension)
        file.write(text)
        file.close()
    