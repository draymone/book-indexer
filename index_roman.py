# importation de la classe Noeud
import arbre_binaire_recherche as abr

# importation de la bibliothèque Expressions Régulières
import re

import matplotlib.pyplot as plt  # Importation de matplotlib
import numpy as np  # Importation de numppy


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


def dessin_graphe():
    """Dessine un graphique avec matplotlib pour présenter des statistiques sur l'arbre

    :param arbre: (Noeud)
    :return:
    """
    # Création d'un dico qui contient les auteurs et le livre associé
    dicto_auteurs_livre = {"Victor Hugo": "quatreving-treize.txt",
                           "Jules Verne": "le_tour_du_monde_en_80_jours.txt",
                           "Marcel Proust": "du_cote_de_chez_swann.txt",
                           "Colette": "le_ble_en_herbe.txt",
                           "George Sand": "la_mare_au_diable.txt"}

    words = ("homme", "femme", "beau", "même", "très", "aussi", "donc", "car", "dieu", "amour")  # Liste des mots
    compte_mots = {}  # Dico vide pour stocker les auteurs et leur utilisation des mots
    for author in dicto_auteurs_livre:  # Pour chaque auteur
        abr = index_roman(dicto_auteurs_livre[author])  # On récupère son livre
        words_count = []
        for word in words:  # Pour chacun des mots à chercher
            words_count.append(abr.donner_frequence(word))  # On recupere sa valeur
        compte_mots[author] = words_count  # On ajoute l'ensemble des valeurs au compte des mots

    x = np.arange(len(words))  # Les positions des labels
    width = 0.1  # L'épaisseur des barres
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in compte_mots.items():  # On recupere les auteurs et leur compte de mots
        offset = width * multiplier
        ax.bar(x + offset, measurement, width, label=attribute)  # On crée des barres de graphique pour chaque auteur
        multiplier += 1

    ax.set_ylabel("Frequence d'apparitions pour 10 000 mots")  # Légende axe Y
    ax.set_title("Occurrence de mots clés chez plusieurs auteurs")  # Titre
    ax.set_xticks(x + width, words)  # Afficchage des barres
    ax.legend(loc='upper right', ncols=3)  # Affichage de la légende
    ax.set_ylim(0, 45)  # Limite des axes

    plt.show()  # On affiche la fenetre


dessin_graphe()
