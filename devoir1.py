# exercice #1

from heapq import heapify
import math


class Tas_d_aire:

    """
    constructeur
    params: A -> un tableau des entiers pour stocker tous les éléments de Tas, 
    d -> un entier positif, nombre des enfants d'un noeud qui n'est pas une feuille
    """
    def __init__(self, A, d):
        self.A = A
        self.d = d 
        # construire un tas max d-aire
        self.contruire_tas_max()

    """
    méthode pour trouver le parent d'un noeud
    params: i -> l'indice d'un noeud dans le tableau, qui commence de 0

    l'index de parent k, ses enfants sont: self.d*k + c ( 1<=c<=self.d)
    l'index de fils i = self.d*k + c, k = i-c/self.d
    k >= i-1//self.d >= i-self.d//self.d
    """
    def parent(self, i):        
        if i > 0 and i < len(self.A):
            return (i-1)//self.d

    """
    méthode pour trouver tous les enfants d'un noeud s'il y a lieu
    params: i -> l'indice d'un noeud dans le tableau
    """
    def enfants(self, i):
        # self.d enfants, i commence de 0
        enfants = []
        if i >= 0 and i < len(self.A):
            for j in range(1, self.d + 1):            
                if self.d*i + j < len(self.A):
                    enfants.append(self.d*i + j)                
        return tuple(enfants)


    def entasser_max(self, i):
        enfants = list(self.enfants(i))
        # print('r-enfants:',enfants)
        if enfants != []:            
            iMax = i            
            elements_enfant = [self.A[j] for j in enfants]
            fils_max = max(elements_enfant) 
            idx_fils_max = enfants[elements_enfant.index(fils_max)]           
            if fils_max > self.A[iMax]:
                iMax = idx_fils_max                            
            if iMax != i:
                self.A[i], self.A[iMax] = self.A[iMax], self.A[i]
                self.entasser_max(iMax)
        # return self

    """
    Construire un tas max
    """
    def contruire_tas_max(self):
        for i in range((len(self.A)-1)//self.d, -1, -1):
            self.entasser_max(i) 
    
    """
    Enlever l'élément le plus grande (la racine) et recontruire le tas max
    """
    def extraire_max(self):
        len_A = len(self.A)
        if len_A > 0:            
            max = self.A[0]
            self.A[0] = self.A[len_A - 1]        
            self.A.remove(self.A[len_A - 1])       
            self.entasser_max(0)
            print('here')
            self.affiche()
            return max, self

    def inserer_max(self, k):
        self.A.append(float('-inf'))
        self.augmenter_cle(len(self.A)-1, k)
        return self

    def augmenter_cle(self, i, k):
        if k >= self.A[i]:
            self.A[i] = k
            while i > 0 and self.A[self.parent(i)] < self.A[i]:
                self.A[i], self.A[self.parent(i)] = self.A[self.parent(i)], self.A[i]
                i = self.parent(i)

    def affiche(self):
        print(self.A)


"""
Question b : la hauteur d'un d-aire tas qui a n éléments
k >= 1
h = k, n(k)_min=self.d**(k-1)+1, n(k)_max=self.d**k

self.d**(k-1)+1 <= n <= self.d**k
k-1 < math.log(n, self.d) <= k

k < log(n, self.d) + 1 && k >= log(n, self.d)
donc k égale à la partie entier de log(n, self.d)+1

"""


tab = [9, 1, 4, 12, 7, 1, 2, 1, 5]
tas1 = Tas_d_aire(tab, 2)
print('parent0:',tas1.parent(0))
print('enfants:',tas1.enfants(0))

tas1.affiche()


ma, t2 = tas1.extraire_max()
print('ma:',ma)
t2.affiche()

# t3 = t2.inserer_max(12)
# t3.affiche()