from enum import Enum
from classe_file import File


class TypeParcours(Enum):
    # Enumeration des differents types de parcours d'un arbre
    PREFIXE = 1
    INFIXE = 2
    SUFFIXE = 3
    LARGEUR = 4


class Noeud:
    def __init__(self, valeur, count=1):
        """Constructeur de la classe Noeud

        :param valeur: (string) la valeur du noeud
        :param count: (int) l'occurrence du noeud
        """
        self.valeur = valeur
        self.occurrence = count
        self.gauche = None
        self.droit = None

    def get_valeur(self):
        """

        :return: (string) la valeur du noeud
        """
        return self.valeur

    def get_occurrence(self):
        """

        :return: (int) l'occurrence du noeud
        """
        return self.occurrence

    def get_valeurs(self):
        """Méthode accesseur pour obtenir la valeur du noeud et son occurrence

        :return: (tuple) ((string) valeur, (int) occurrence)
        """
        return self.valeur, self.occurrence

    def droit_existe(self):
        """Méthode renvoyant True si l'enfant droit existe
        Aucun paramètre en entrée"""
        return self.droit is not None

    def gauche_existe(self):
        """Méthode renvoyant True si l'enfant gauche existe
        Aucun paramètre en entrée"""
        return self.gauche is not None

    def inserer(self, cle):
        """Insère la cle dans l'ABR, ou augmente son occurrence si elle est déja présente

        :param cle: (string) caractère à insérer
        :return:
        """
        if cle < self.get_valeur():  # Si la clé est inférieure
            if self.gauche_existe():  # Et que l'arbre gauche existe
                self.gauche.inserer(cle)  # On l'y insere
            else:  # Sinon
                self.gauche = Noeud(cle)  # On crée l'enfant gauche avec comme valeur la cle
        elif cle > self.get_valeur():  # Si la clé est supérieure
            if self.droit_existe():  # Et que l'arbre droit existe
                self.droit.inserer(cle)  # On l'y insere
            else:  # Sinon
                self.droit = Noeud(cle)  # On crée l'enfant droit avec comme valeur la cle
        elif cle == self.get_valeur():  # Si on a trouvé la clé
            self.incr_occurrence()  # On incrémente son occurrence

    def taille(self):
        """Methode récursive de calcul de la taille de l'ABR

        :return: (int) la taille de l'ABR
        """
        # Le noeud est nul
        if self is None:
            return 0

        # Le noeud a deux enfants
        if self.gauche_existe() & self.droit_existe():
            return 1 + self.gauche.taille() + self.droit.taille()

        # Le noeud a un enfant droit
        if self.droit_existe():
            return 1 + self.droit.taille()

        # Le noeud a un enfant gauche
        if self.gauche_existe():
            return 1 + self.gauche.taille()

        # Le noeud n'a pas d'enfants
        return 1

    def hauteur(self):
        """Methode récursive de calcul de la hauteur de l'ABR

        :return: (int) la hauteur de l'ABR
        """
        # Le noeud est nul
        if self is None:
            return 0

        # Le noeud a deux enfants
        if self.gauche_existe() & self.droit_existe():
            return 1 + max(self.gauche.hauteur(), self.droit.hauteur())

        # Le noeud a un enfant droit
        if self.droit_existe():
            return 1 + self.droit.hauteur()

        # Le noeud a un enfant gauche
        if self.gauche_existe():
            return 1 + self.gauche.hauteur()

        # Le noeud n'a pas d'enfants
        return 1

    def parcours(self, type_parcours):
        """
        Methode récursice de parcours de l'arbre

        :param type_parcours: (TypeParcours) le type de parcours à faire
        :return: (list) le résultat du parcours de l'arbre
        """
        if type_parcours == TypeParcours.PREFIXE:
            return self.__parcours_prefixe__()

        if type_parcours == TypeParcours.INFIXE:
            return self.__parcours_infixe__()

        if type_parcours == TypeParcours.SUFFIXE:
            return self.__parcours_suffixe__()

        if type_parcours == TypeParcours.LARGEUR:
            return self.__parcours_largeur__()

    def __parcours_prefixe__(self):
        # Le noeud est nul
        if self is None:
            return None

        # Le noeud a deux enfants
        if self.gauche_existe() & self.droit_existe():
            return [self.get_valeur()] + self.gauche.__parcours_prefixe__() + self.droit.__parcours_prefixe__()

        # Le noeud a un enfant droit
        if self.droit_existe():
            return [self.get_valeur()] + self.droit.__parcours_prefixe__()

        # Le noeud a un enfant gauche
        if self.gauche_existe():
            return [self.get_valeur()] + self.gauche.__parcours_prefixe__()

        # Le noeud n'a pas d'enfants
        return [self.get_valeur()]

    def __parcours_infixe__(self):
        # Le noeud est nul
        if self is None:
            return None

        # Le noeud a deux enfants
        if self.gauche_existe() & self.droit_existe():
            return self.gauche.__parcours_infixe__() + [self.get_valeur()] + self.droit.__parcours_infixe__()

        # Le noeud a un enfant droit
        if self.droit_existe():
            return [self.get_valeur()] + self.droit.__parcours_infixe__()

        # Le noeud a un enfant gauche
        if self.gauche_existe():
            return self.gauche.__parcours_infixe__() + [self.get_valeur()]

        # Le noeud n'a pas d'enfants
        return [self.get_valeur()]

    def __parcours_suffixe__(self):
        # Le noeud est nul
        if self is None:
            return None

        # Le noeud a deux enfants
        if self.gauche_existe() & self.droit_existe():
            return self.gauche.__parcours_suffixe__() + self.droit.__parcours_suffixe__() + [self.get_valeur()]

        # Le noeud a un enfant droit
        if self.droit_existe():
            return self.droit.__parcours_suffixe__() + [self.get_valeur()]

        # Le noeud a un enfant gauche
        if self.gauche_existe():
            return self.gauche.__parcours_suffixe__() + [self.get_valeur()]

        # Le noeud n'a pas d'enfants
        return [self.get_valeur()]

    def __parcours_largeur__(self):
        # Variables
        ma_file = File()
        liste_noeuds = []

        # On recupere le premier noeud et on l'ajoute à la file
        node = self
        ma_file.ajouter(node)

        # Tant que la file n'est pas vide
        while not ma_file.file_vide():
            # On retire le premier noeud pour le placer dans le resultat
            node = ma_file.retirer()
            liste_noeuds.append(node.get_valeur())
            # Si le noeud gauche existe on l'ajoute à la file
            if node.gauche_existe():
                ma_file.ajouter(node.gauche)
            # Si le noeud droit existe on l'ajoute à la file
            if node.droit_existe():
                ma_file.ajouter(node.droit)

        # On renvoie le resultat
        return liste_noeuds

    def recherche(self, x):
        """Méthode récursive de recherche d'un élément dans un ABR

        :param x: l'élément à cherche
        :return: (bool) True si l'élément est présent dans l'arbre, False sinon
        """
        if self is None:  # Si l'arbre est vide
            return False  # Return false

        valeur = self.get_valeur()  # On récupère la valeur du noeud
        if valeur == x:  # Si on a la même valeur
            return True  # On a trouvé la clé
        if valeur > x:  # Si la clé est inférieure à la valeur...
            if not self.gauche_existe():  # (Et que l'arbre gauche existe)
                return False
            return self.gauche.recherche(x)  # Elle ne peut que se trouver dans l'arbre gauche
        # Sinon la clé est supérieure à la valeur
        if not self.droit_existe():  # Si l'arbre droite existe
            return False
        return self.droit.recherche(x)  # La clé ne peut que se trouver dans l'arbre droit

    def donner_occurence(self, cle):
        """Méthode récursive de recherche de l'ocurrence d'une clé

        :param cle: (str) clé à chercher
        :return: (int) occurrence de la clé
        """
        if self is None:  # Si le noeud est vide
            return 0  # En renvoie 0

        valeur = self.get_valeur()  # On récupère la valeur du noeud
        if valeur == cle:  # Si on a la même valeur, on est sur la bonne clé
            return self.get_occurrence()  # On récupère l'ocurrence et on la renvoie

        if valeur > cle:  # Si la clé est inférieure à la valeur...
            if not self.gauche_existe():  # (Et que l'arbre gauche existe)
                return False
            return self.gauche.donner_occurence(cle)  # Elle ne peut que se trouver dans l'arbre gauche

        # Sinon la clé est supérieure à la valeur
        if not self.droit_existe():  # Et si l'arbre gauche existe
            return False
        return self.droit.donner_occurence(cle)  # La clé ne peut que se trouver dans l'arbre droit

    def niveaux_arbre(self, index=0, levels_matrix=None):
        ###############################################
        #               METHODE INUTILE               #
        # Je n'avais pas envie de jetter mon travail  #
        # alors je l'ai laissé ici                    #
        ###############################################
        """Renvoie une matrice, dont chaque élément représente une ligne, qui contient un tableau de noeuds

        :param index: (int) le niveau de l'arbre
        :param levels_matrix: (array)
        :return:
        """
        if levels_matrix is None:
            levels_matrix = []

        if len(levels_matrix) >= index + 1:  # Si le niveau est déja dans la matrice...
            levels_matrix[index].append(self.get_valeur())  # On y ajoute l'element
        else:  # Si le niveau n'est pas encore dans la matrice...
            levels_matrix.append([self.get_valeur()])  # On le crée

        # On ajoute la partie gauche de l'arbre
        if self.gauche_existe():
            self.gauche.niveaux_arbre(index + 1, levels_matrix)

        # On ajoute la partie droite de l'arbre
        if self.droit_existe():
            self.droit.niveaux_arbre(index + 1, levels_matrix)

        # On renvoie la matrice
        return levels_matrix

    def incr_occurrence(self):
        """Incrément l'occurrence du noeud de 1

        :return:
        """
        self.occurrence += 1

    def total_occurrence(self):
        """Méthode récursive de recherche du total des occurrences dans un ABR

        :return: (int) total des occurrences
        """
        occurence = self.get_occurrence()  # On récupère l'occurence du noeud

        # On récupère le total des occurrences du sous arbre gauche
        occurence_gauche = 0
        if self.gauche_existe():
            occurence_gauche = self.gauche.total_occurrence()

        # On récupère le total des occurrences du sous arbre droit
        occurence_droite = 0
        if self.droit_existe():
            occurence_droite = self.droit.total_occurrence()

        return occurence + occurence_gauche + occurence_droite  # On renvoie la somme des occurences

    def max_occurrence(self):
        """Méthode récursive de recherche de l'élement avec la plus grande occurrence dans un ABR

        :return: (int) plus grande occurrence
        """
        occurence = self.get_occurrence()  # On récupère l'occurence du noeud

        # On récupère l'occurrence maximale du sous arbre gauche
        occurence_gauche = 0
        if self.gauche_existe():
            occurence_gauche = self.gauche.max_occurrence()

        # On récupère l'occurrence maximale du sous arbre droit
        occurence_droite = 0
        if self.droit_existe():
            occurence_droite = self.droit.max_occurrence()

        return max(occurence_gauche, occurence_droite, occurence)  # On renvoie le maximum des occurences

    def max_occurrence_v2(self):
        """Méthode récursive de recherche de l'élement avec la plus grande occurrence dans un ABR

        :return: (int) plus grande occurrence
        """
        valeurs = self.get_valeurs()  # On récupère les valeur du noeud

        # On récupère les valeurs du noeud le plus présent dans l'arbre gauche
        valeurs_gauche = (0, 0)
        if self.gauche_existe():
            valeurs_gauche = self.gauche.max_occurrence_v2()

        # On récupère les valeurs du noeud le plus présent dans l'arbre droit
        valeurs_droite = (0, 0)
        if self.droit_existe():
            valeurs_droite = self.droit.max_occurrence_v2()

        values = [valeurs, valeurs_gauche, valeurs_droite]  # On crée une liste avec les valeurs de chaque partie
        return max(values, key=lambda x: x[1])  # On renvoie celle avec la plus haute occurrence

    def __str__(self):
        """Méthode récursive pour obtenir une représentation lisible d'un arbre.
        Aucun paramètre en entrée
        Syntaxe :
            >>> print(arbre)"""
        # Keep a list of lines
        lines = list()
        lines.append(str(self.get_valeur()) + ", " + str(self.get_valeurs()[1]))
        # Get left and right sub-trees
        l = str(self.gauche).split('\n')
        r = str(self.droit).split('\n')
        # Append first left, then right trees
        for branch in r, l:
            # Suppress Pipe on right branch
            alt = '| ' if branch is r else '  '
            for line in branch:
                # Special prefix for first line (child)
                prefix = '+-' if line is branch[0] else alt
                lines.append(prefix + line)
        # Collapse lines
        return '\n'.join(lines)
