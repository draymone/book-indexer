class File:
    def __init__(self):
        self.ma_file = []
        
    def file_vide(self):
        return len(self.ma_file) == 0

    def ajouter(self, ma_valeur):
        self.ma_file.append(ma_valeur)

    def retirer(self):
        return self.ma_file.pop(0)

    def premier(self):
        return self.ma_file[0]

    def taille(self):
        return len(self.ma_file)
