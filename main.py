######################### Importations ##########################

from fonctions import proportions, merger, translate, get_texte
from classes import ArbreB, Sommet

#################################################################

training_file = "test.txt" # fichier "de calibrage" sur lequel l'ABR se base pour sa génération.
file_to_encode = "test.txt" # fichier a encoder via l'ABR crée sur le training file.
# possibilité que (training_file = file_to_encode)

####################### Programme principal #####################

characters_proportions = proportions(training_file)
liste_arbres = [ArbreB(Sommet(e,v)) for v,e in characters_proportions]
arborescence = merger(liste_arbres)
#arborescence.show()
#arborescence.search(chr)
#arborescence.get_characters()
dico_conv = arborescence.get_encode()
texte = get_texte(file_to_encode)
print(texte)
test = translate(texte, dico_conv)
print(test)
test = translate(test, dico_conv, True)
print(test)

# END #