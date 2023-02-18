from classes import ArbreB


def proportions(path:str):
    """Prend le chemin d'un fichier quelconque et retourne les
    occurences par Charactères (= chr) de son content.\n
    str => list(n*tuple(chr,occurences))"""
    
    with open(path,"r") as f:
        texte = "".join(f.readlines()).lower()

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


def _staged_merger(liste_abr:list[ArbreB]):
    """Fusion par étages"""
    output = []
    while len(liste_abr) >= 2:
        output.append(liste_abr.pop(0) + liste_abr.pop(0))
    for i in liste_abr:
        output.append(i)
    return output


def merger(liste_abr:list[ArbreB]):
    """Prend une liste d'arbres en argument et fusionne le
    tout en un seul et même arbre."""
    while len(liste_abr) > 1:
        liste_abr = _staged_merger(liste_abr)
    return liste_abr[0]


def translate(texte:str|list[str], conversion:dict, reverse:bool=False):
    """Traduit un texte selon la conversion, l'opération inverse est possible"""
    output = []
    if reverse:
        for i in texte:
            output.append(get_key_from_value(conversion,i))
        output = "".join(output)
    else:
        for i in texte:
            output.append(conversion[i])
    return output


def get_key_from_value(d:dict, val:str):
    """Reviens à inverser key et value"""
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    else:
        raise ValueError


def get_texte(path:str):
    """Prend le chemin d'un fichier et renvoi son contenu en str"""
    with open(path) as f:
        texte = "".join(f.readlines()).lower()
    return texte