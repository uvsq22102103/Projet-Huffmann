from fonctions import proportions, merger, translate, get_texte
from classes import ArbreB, Sommet

characters_proportions = proportions("test.txt")
liste_arbres = [ArbreB(Sommet(e,v)) for v,e in characters_proportions]
arborescence = merger(liste_arbres)
#arborescence.show()
#arborescence.search(chr)
#arborescence.get_characters()
dico_conv = arborescence.get_encode()
texte = get_texte("test.txt")
print(texte)
test = translate(texte, dico_conv)
print(test)
test = translate(test, dico_conv, True)
print(test)