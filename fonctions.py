

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
    """Traduit un texte selon la conversion, l'opération inverse est possible"""
    output = ""
    try :
        for i in texte:
            output += conversion[i]
        return output
    except :
        raise ValueError(f"le charactère <{i}> n'existe pas dans le text d'entraînement")

def decoding(texte:str, conversion:dict):
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