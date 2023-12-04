# importation de la classe Noeud
import arbre_binaire_recherche as abr

# importation de la bibliothèque Expressions Régulières
import re


def index_roman(file):
    """ Cette fonction crée un arbre binaire de recherche à partir
    d'un fichier texte, en classant les mots par ordre alphabétique.
    Paramètre d'entrée : un fichier texte
    Sortie : un ABR"""
    # récupération du texte dans le fichier
    texte = open(file, 'r', encoding='utf-8')
    tableau = texte.readlines()
    texte.close()

    # initialisation de l'arbre binaire de recherche
    arbre = None

    for ligne in tableau:  # Pour chaque ligne du texte
        ligne = ligne.lower()  # Formatage du fichier en minuscules
        liste_mots = re.split('[;_,.?!\"\'\-\%\n() `&]', ligne)  # On sépare les mots en enlevant les caractères
        # spéciaux
        while '' in liste_mots:  # Si il y a des caratères vides
            liste_mots.remove('')  # On les enleves

        for mot in liste_mots:  # Pour chaque mot de la ligne
            if arbre is None:  # Si l'arbre est vide
                arbre = abr.Noeud(mot)  # On l'initialise avec comme seul noeud mot
                continue  # On passe cette ittération de la boucle
            arbre.inserer(mot)  # Sinon on insere le mot dans l'arbre
    return arbre
