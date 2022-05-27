# exercice #1

from email import message
from xml.dom import ValidationErr
from django.forms import ValidationError


class Tas_d_aire:

    """
    constructeur
    params: A -> un tableau des entiers pour stocker tous les éléments de Tas, 
    d -> un entier positif, nombre des enfants d'un noeud qui n'est pas une feuille
    """
    def __init__(self, A, d):
        try:
            self.A = self.tab_validateur(A)
            self.d = self.nbre_validateur(d) 

            # construire un tas max d-aire
            self.contruire_tas_max()

        except ValidationErr:
            print('Le tableau ne doit pas être vide') 

        except ValueError:
            print('D doit être un entier au moins égale à 2')       
        
        

    """
    Vérifier si la taille du tableau qui représente le tas est vide ou non
    """
    def tab_validateur(self, A):
        if len(A) == 0:
            raise ValidationErr('')
        return A

    """
    Vérifier si le nombre de d-aire est un entier au moins égale à 2 ou non
    """
    def nbre_validateur(self, d):
        if isinstance(d, int) and d >= 2:
            return d
        raise ValueError('')
    
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


    """
    À partir d'un noeud, vérifier si la clé est supérieure à ses enfants,
    sinon pour garder la nature de tas max, on échange ce noeud avec son fils le plus grand,
    si l'arbre n'est pas équilibré, on continue cette procédure
    """
    def entasser_max(self, i):
        # obtenir tous les enfants d'un noeud
        enfants = self.enfants(i)
        if enfants != ():            
            # affecter la variable iMax avec l'indice du noeud courant
            iMax = i
            # obtenir tous les éléments correspondants les indices des enfants dans le tas            
            elements_enfant = [self.A[j] for j in enfants]
            # obtenir le fils le plus grand
            fils_max = max(elements_enfant)
            # obtenir l'indice du fils le plus grand 
            idx_fils_max = enfants[elements_enfant.index(fils_max)]           
            # vérifier si le fils le plus grand est supérieur à le noeud courant
            # si c'est le cas, on affecte l'indice du fils le plus grand à la variable iMax
            if fils_max > self.A[iMax]:
                iMax = idx_fils_max                            
            # si la valeur de la variabale iMax n'est pas égale à l'indice du noeud courant
            # on échange les deux éléments dans le tableau qui représente le tas
            if iMax != i:
                self.A[i], self.A[iMax] = self.A[iMax], self.A[i]
                # recontruire le tas max
                self.entasser_max(iMax)

    """
    Construire un tas max.
    L'indice du dernier noeud qui n'est pas une feuille : (len(self.A)-1)//self.d
    ou on peut la trouver avec la fonction suivante:
    for i in range(len(self.A)):
        if self.enfants(i) == []:
            return i-1
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
            # stocker l'élément de la racine dans la variable max           
            max = self.A[0]
            # écraser le premier élément par le dernier élément
            self.A[0] = self.A[-1] 
            # enlever le dernier élément               
            del self.A[-1]
            # recontruire le tas max à partir de la racine                 
            self.entasser_max(0)
            return max, self

    """
    Insérer une clé dans le tas, si le tas max n'est pas équilibré, on augmenter la clé 
    jusqu'à le tas max est rétabli
    """
    def inserer_max(self, k):
        self.A.append(float('-inf'))
        self.augmenter_cle(len(self.A)-1, k)
        return self

    """
    
    """
    def augmenter_cle(self, i, k):
        try:
            if k >= self.A[i]:
                self.A[i] = k
                while i > 0 and self.A[self.parent(i)] < self.A[i]:
                    self.A[i], self.A[self.parent(i)] = self.A[self.parent(i)], self.A[i]
                    i = self.parent(i)
        except BaseException:
            print('La clé doit être un nombre')

    """
    
    """
    def affiche(self):
        try:
            print('Le tas max %d-aire:'% self.d, self.A)        
            print('Noeud -> Enfants')
            for i in range(len(self.A)):
                print('  (%d) -> %s' % (i, str(self.enfants(i))))
        except BaseException:
            print('Le tas est invalid')




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
tas1 = Tas_d_aire(tab, 3)
tas4 = Tas_d_aire(tab,1)
tas5 = Tas_d_aire(tab,2.5)
tas6 = Tas_d_aire([],2)
tas7 = Tas_d_aire(tab, 'a')

print('parent0:',tas1.parent(0))
print('enfants:',tas1.enfants(0))

tas1.affiche()
tas4.affiche()


ma, t2 = tas1.extraire_max()
# print('ma:',ma)
# t2.affiche()

t3 = t2.inserer_max('A')
t3.affiche()