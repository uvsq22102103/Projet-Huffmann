## Sommaire

1. [Description](#description)
2. [Libraires](#librairies)
3. [Installation](#installation)
4. [Guide](#guide)

## Description

  Ce projet a pour but d'implémenter la logique du code d'Huffman dans une application en python, à l'aide de différentes librairies telles que, la plus importante visuellement, ttkbootstrap. A travers une interface graphique, ce projet contient deux parties principales :
- Il est possible d'afficher un arbre respectant les règles du code d'Huffman instancié à partir d'un texte,
- De crypter et décrypter un texte à l'aide d'un dictionnaire de cryptage créé par l'application.

Ce projet à été débuté le 12/02/2023 et est dû pour le 21/04/2023 et sera finalisé avant cette date.

### Screenshots
Affichage d'un arbre :
![Image canva](https://github.com/uvsq22102103/Projet-Huffmann/blob/main/documentation/screenhuffman1emepage.png)
Cryptage d'un texte :
![Image crypt](https://github.com/uvsq22102103/Projet-Huffmann/blob/main/documentation/screenhuffman2emepage.png)

## Librairies

Une liste de librairies utilisées lors de ce projet :

* tkinter
* math
* codecs
* webbrowser
* [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) : Version 1.10.1


## Installation

Il vous sera nécessaire d'installer la librairie ttkbootstrap pour que l'application fonctionne:
* ```python -m pip install ttkbootstrap```

## Guide

### Pour créer et afficher un arbre respectant le code d'Huffman :
* Entrer votre texte à l'emplacement indiqué puis appuyer sur le bouton "Afficher l'arbre d'Huffman de votre texte"
* Votre arbre s'affiche et vous pouvez l'explorer à l'aide de scrollbars. De plus, le chemin de chaque caractère est affiché dans la listbox

### Pour crypter ou décrypter un texte respectant le code d'Huffman : 

#### Cryptage
* Entrer votre texte à l'emplacement indiqué puis appuyez sur le bouton "Enregistrer un dictionnaire de cryptage d'Huffman" 
* Cela enregistrera le dictionnaire nécessaire pour crypter votre texte
* Appuyer sur le bouton "Encoder votre texte" et choisir le dictionnaire que vous avez précedemment créé 
> Si le dictionnaire ne contient pas tout les caractères de votre texte entré, une erreur sera retournée !
* Votre texte crypté s'affiche et vous pouvez le copier  

#### Décryptage
* Entrer votre texte à l'emplacement indiqué puis appuyez sur le bouton "Décoder votre texte binaire"
* Choisissez le dictionnaire de cryptage adapté 
> Attention, une erreur vous sera retourné si vous ne choisissez pas le dictionnaire avec lequel le texte a été encodé !
* Votre texte décrypté s'affiche et vous pouvez le copier






