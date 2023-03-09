######################### Importations ##########################

from fonctions import proportions, merger, translate, get_texte_from_file
from classes import ArbreB, Sommet

#################################################################

training_file = "test_elie.txt" # fichier "de calibrage" sur lequel l'ABR se base pour sa génération.
file_to_encode = "test_elie.txt" # fichier a encoder via l'ABR crée sur le training file.
# possibilité que (training_file = file_to_encode)

####################### Programme principal #####################

with open(training_file) as f:
    texte = "".join(f.readlines())

characters_proportions = proportions(texte)
liste_arbres = [ArbreB(Sommet(e,v)) for v,e in characters_proportions]
merger(liste_arbres)
arborescence = liste_arbres[0]
#arborescence.show()
dico_conv = arborescence.get_encode()
print(dico_conv)
print(arborescence.get_characters())
#texte = get_texte_from_file(file_to_encode)
#print(texte)
#test = translate(texte, dico_conv)
#print(test)
#test = translate(test, dico_conv, True)
#print(test)

# END #