from classes import ArbreB


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


def get_texte_from_file(path:str):
    """Prend le chemin d'un fichier et renvoi son contenu en str"""
    with open(path) as f:
        texte = "".join(f.readlines()).lower()
    return texte