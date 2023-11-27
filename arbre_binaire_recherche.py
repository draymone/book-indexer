from enum import Enum
from classe_file import File


class TypeParcours(Enum):
    PREFIXE = 1
    INFIXE = 2
    SUFFIXE = 3
    LARGEUR = 4


class Noeud:
    def __init__(self, valeur):
        """Méthode constructeur pour la classe Noeud.
        Paramètre d'entrée : valeur
        valeur : int ou str"""
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def get_valeur(self):
        """Méthode accesseur pour obtenir la valeur du noeud
        Aucun paramètre en entrée"""
        return self.valeur

    def droit_existe(self):
        """Méthode renvoyant True si l'enfant droit existe
        Aucun paramètre en entrée"""
        return self.droit is not None

    def gauche_existe(self):
        """Méthode renvoyant True si l'enfant gauche existe
        Aucun paramètre en entrée"""
        return self.gauche is not None

    def inserer(self, cle):
        """Méthode d'insertion de clé dans un arbre binaire de recherche
        Paramètre d'entrée : valeur
        valeur : int ou str"""
        if cle < self.valeur:
            # on insère à gauche
            if self.gauche_existe():
                # on descend à gauche et on recommence le test initial
                self.gauche.inserer(cle)
            else:
                # on crée un fils gauche
                self.gauche = Noeud(cle)
        elif cle > self.valeur:
            # on insère à droite
            if self.droit_existe():
                # on descend à droite et on recommence le test initial
                self.droit.inserer(cle)
            else:
                # on crée un fils droit
                self.droit = Noeud(cle)

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

        :param type_parcours: (TypeParcours)
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
            return [self.valeur] + self.gauche.__parcours_prefixe__() + self.droit.__parcours_prefixe__()

        # Le noeud a un enfant droit
        if self.droit_existe():
            return [self.valeur] + self.droit.__parcours_prefixe__()

        # Le noeud a un enfant gauche
        if self.gauche_existe():
            return [self.valeur] + self.gauche.__parcours_prefixe__()

        # Le noeud n'a pas d'enfants
        return [self.valeur]

    def __parcours_infixe__(self):
        # Le noeud est nul
        if self is None:
            return None

        # Le noeud a deux enfants
        if self.gauche_existe() & self.droit_existe():
            return self.gauche.__parcours_infixe__() + [self.valeur] + self.droit.__parcours_infixe__()

        # Le noeud a un enfant droit
        if self.droit_existe():
            return [self.valeur] + self.droit.__parcours_infixe__()

        # Le noeud a un enfant gauche
        if self.gauche_existe():
            return self.gauche.__parcours_infixe__() + [self.valeur]

        # Le noeud n'a pas d'enfants
        return [self.valeur]

    def __parcours_suffixe__(self):
        # Le noeud est nul
        if self is None:
            return None

        # Le noeud a deux enfants
        if self.gauche_existe() & self.droit_existe():
            return self.gauche.__parcours_suffixe__() + self.droit.__parcours_suffixe__() + [self.valeur]

        # Le noeud a un enfant droit
        if self.droit_existe():
            return self.droit.__parcours_suffixe__() + [self.valeur]

        # Le noeud a un enfant gauche
        if self.gauche_existe():
            return self.gauche.__parcours_suffixe__() + [self.valeur]

        # Le noeud n'a pas d'enfants
        return [self.valeur]

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
            liste_noeuds.append(node.valeur)
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
        :return: (bool) oui si l'élément est présent dans l'arbre, sinon non
        """
        if self is None:
            return False

        valeur = self.get_valeur()  # On récupère la valeur du noeud
        if valeur == x:  # Si on a la même valeur
            return True  # On a trouvé la clé
        if valeur > x:  # Si la clé est inférieure à la valeur...
            if not self.gauche_existe():  # (Et que l'arbre gauche ci existe)
                return False
            return self.gauche.recherche(x)  # Elle ne peut que se trouver dans l'arbre gauche
        # Sinon la clé est supérieure à la valeur
        if not self.droit_existe():  # Et si l'arbre gauche existe
            return False
        return self.droit.recherche(x)  # La clé ne peut que se trouver dans l'arbre droit

    def niveaux_arbre(self, index=0, levels_matrix=None):
        if levels_matrix is None:
            levels_matrix = []

        if len(levels_matrix) >= index + 1:  # Si le niveau est déja dans la matrice...
            levels_matrix[index].append(self.valeur)  # On y ajoute l'element
        else:  # Si le niveau n'est pas encore dans la matrice...
            levels_matrix.append([self.valeur])  # On le crée

        # On ajoute la partie gauche de l'arbre
        if self.gauche_existe():
            self.gauche.niveaux_arbre(index + 1, levels_matrix)

        # On ajoute la partie droite de l'arbre
        if self.droit_existe():
            self.droit.niveaux_arbre(index + 1, levels_matrix)

        # On renvoie la matrice
        return levels_matrix

    def __str__(self):
        """Méthode récursive pour obtenir une représentation lisible
        d'un arbre.
        Aucun paramètre en entrée
        Syntaxe :
            >>> print(arbre)"""
        # Keep a list of lines
        lines = list()
        lines.append(str(self.valeur))
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