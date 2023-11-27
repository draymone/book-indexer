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
    texte = open(file,'r',encoding = 'utf-8')
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
        print(liste_mots)
