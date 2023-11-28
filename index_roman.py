# importation de la classe Noeud d'un ABR
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

    # Boucle : pour chaque ligne du texte
    for ligne in tableau:
        # formatage du fichier texte
        # passage en minuscule
        ligne = ligne.lower()
        # on récupère une liste de mots, en enlevant tous les séparateurs connus
        liste_mots = re.split('[;_,.?!\"\'\-\%\n() `&]', ligne)
        # on enlève les mots vides dans la liste de mots
        while '' in liste_mots:
            liste_mots.remove('')

        # pour chaque mot dans la liste de mots
        for mot in liste_mots:  # Pour chaque mot de la ligne
            if arbre is None:  # Si l'arbre est vide
                arbre = abr.Noeud(mot)  # On l'initialise avec comme seul noeud mot
                pass  # On passe cette ittération de la boucle
            arbre.inserer(mot)  # On insere le mot dans l'arbre/on augmente son occurrence
    return arbre


therefore_i_am = index_roman("therefore_i_am.txt")
print(therefore_i_am.get_valeurs())
print(therefore_i_am.donner_occurence("i"))
print(therefore_i_am.total_occurrence())
print(therefore_i_am.max_occurrence())
print(therefore_i_am.max_occurrence_v2())
