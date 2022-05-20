# exercice #1

class Tas_d_aire:

    """
    constructeur
    params: A -> un tableau des entiers, d -> un entier positif
    """
    def __init__(self, A, d):
        self.A = A
        self.d = d 

    """
    méthode pour trouver le parent d'un noeud
    params: i -> l'indice d'un noeud dans le tableau
    """
    def parent(self, i):
        return self.A[(i-1)//2]

    """
    méthode pour trouver tous les enfants d'un noeud s'il y a lieu
    params: i -> l'indice d'un noeud dans le tableau
    """
    def enfants(self, i):
        # deux enfants
        if 2*i + 1 <= len(self.A)-1 and 2*i + 2 <= len(self.A)-1:
            return [self.A[2*i+1], self.A[2*i+2]]
        # seulement un enfant gauche
        elif 2*i + 1 <= len(self.A)-1:
            return [self.A[2*i+1]]
        # si le noeud est une feuille, il n'y a pas d'enfant
        return []

    def entasser_max(self, i):
        iMax = i
        filsG_idx = 2*i + 1
        filsD_idx = 2*i + 2
        if filsG_idx < self.d and self.A[filsG_idx] > self.A[iMax]:
            iMax = filsG_idx
        if filsD_idx < self.d and self.A[filsD_idx] > self.A[iMax]:
            iMax = filsD_idx
        if iMax != i:
            self.A[i], self.A[iMax] = self.A[iMax], self.A[i]
            entasser_max(self, iMax)

    def extraire_max(self, i):
        pass

    def inserer_max(self):
        pass

    def augmenter_cle(i, k):
        pass

    def affiche(self):
        print(self.A)
