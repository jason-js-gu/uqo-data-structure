# créer et initialiser la class Noeud
class Noeud:
    def __init__(self, k=None, c=None, p=None, g=None, 
                d=None, t=None, pred=None, succ=None):
        self.k = k
        self.c = c
        self.p = p
        self.g = g
        self.d = d
        self.t = t
        self.pred = pred
        self.succ = succ

    # l'affichage d'un noeud
    def __str__(self):
        return '(%s%s g:%s d:%s t:%s)' % \
                (
                 self.k, '*' if self.c == R else '',  
                 self.g.k if self.g.k else 'Nil', 
                 self.d.k if self.d.k else 'Nil', 
                 self.t if self.t else 0
                )


R = 'Rouge'
N = 'Noir'

class RN_arbre:
    # attribut de la class
    nil = Noeud(None, N)
    nil.p = nil
    nil.g = nil
    nil.d = nil
    nil.t = 0     

    def __init__(self, tab):
        self.tab = tab        
        self.racine = self.nil
        self.min = self.nil
        self.max = self.nil
        self.construire_RN_arbre()
    
    # validation de la propriété tab
    @property
    def tab(self):
        return self._tab

    @tab.setter
    def tab(self, val):
        for i in val:
            if not isinstance(i, int):
                raise ValueError('Les éléments doivent être entiers')
        self._tab = val       

    # vérifier si un noeud dans l'arbre ou non à partir de sa clé
    def trouve_noeud(self, i): 
        x = self.racine       
        while x != self.nil:
            if x.k == i:
                return x
            elif x.k > i:
                x = x.g
            else:
                x = x.d
        return None 

    # créer un arbre rouge-noir 
    def construire_RN_arbre(self):
        if len(self.tab) == 0:
            return self.racine
        for i in self.tab:
            self.arbre_inserer(i)            

    """
    insérer un noeud dans un arbre rouge-noir
    params: i, soit un entier, soit un noeud
    après l'insertion, tous les propriétés doivent être mis à jour
    """
    def arbre_inserer(self, i):
        # si le paramètre i est un entier, créer un nouveau noeud
        if isinstance(i, int):
            z = Noeud(i, R)
          
        elif isinstance(i, Noeud):
            z = i
        # initialiser les attributs du noeud à insérer
        z.p = self.nil
        z.g = self.nil
        z.d = self.nil
        z.t = 1

        y = self.nil
        x = self.racine
        while x != self.nil:
            # mettre à jour la taille de chaque noeud x du chemin simple reliant la racine aux feuilles
            x.t += 1
            y = x 
            if z.k < x.k:
                x = x.g
            else:
                x = x.d
        z.p = y
        # mettre à jour les propriétés racine (s'il y a lieu), min et max d'instance 
        if y == self.nil:
            self.racine = z
            self.min = z
            self.max = z
        elif z.k < y.k:
            y.g = z
            if self.min == z.p:
                self.min = z
        else:
            y.d = z
            if self.max == z.p:
                self.max = z
        # mettre à jour les prédésseur et suucessuer du noeud inséré
        self.ajout_pred_succ(z)
        # réconstruire l'arbre pour corriger les conflits des règlements d'un arbre rouge-noir
        self.inserer_correction_rn(z) 
        # afficher l'arbre après la correction        
        self.affiche('\nAprès inserer_correction')

    
    """
    supprimer un noeud s'il est dans l'arbre
    params: i, un entier delaquelle on vérifie si ce noeud est dans l'arbre ou non
    après la suppression, on doit mettre à jour les propriétés et réconstruire l'arbre
    """
    # 
    def supprimer(self, i):
        # function imbriquée pour décrémenter la taille des ancêtres d'un noeud
        def decrement_taille_chaine(x):
            while x != self.nil:
                x.t -= 1
                x = x.p
        # chercher le noeud à supprimer et le stocker dans la variable z
        z = self.trouve_noeud(i)
        y = z
        y_c_originale = y.c        
        if z: 
            if z.g == self.nil:
                decrement_taille_chaine(z)
                x = z.d
                self.transplante_rn(z, z.d)
            elif z.d == self.nil:
                decrement_taille_chaine(z)
                x = z.g
                self.transplante_rn(z, z.g)
            else:
                # le noeud à supprimer a deux enfants
                y = self.arbre_min(z.d)
                y_c_originale = y.c
                x = y.d
                decrement_taille_chaine(y)
                if y.p == z:
                    x.p = y
                else:
                    self.transplante_rn(y, y.d)
                    y.d = z.d
                    y.d.p = y
                self.transplante_rn(z, y)
                y.g = z.g
                y.g.p = y
                y.c = z.c
                # mettre à jour la taille
                y.t = y.g.t + y.d.t + 1
        # mettre à jour le min et le max de l'arbre
        if self.min == z:
            self.min = z.succ
        if self.max == z:
            self.max = z.pred
        # mettre à jour le précédeur et le successeur du noeud supprimé
        self.supprimer_pred_succ(z)  
        # faire la correction si necéssaire
        if y_c_originale == N:
            self.supprimer_correction_rn(x)

    # obtenir un noeud à partir d'un entier qui représente son rang
    def lire_rang(self, i):
        x = self.racine
        # non récursif
        while x != self.nil:
            r = x.g.t + 1
            if i == r:
                return x
            elif i < r:
                x = x.g
            else:
                i -= r
                x = x.d
    """
    obtenir le rang d'un noeud
    params: x, soit un entier qui représente la clé d'un noeud, soit un noeud
    """
    # 
    def determine_rang(self, x):
        if isinstance(x, int):
            z = self.trouve_noeud(x)
        elif isinstance(x, Noeud):
            z = x
        # print('z:',z)
        if z:
            r = z.g.t + 1
            y = z
            while y != self.racine:
                if y == y.p.d:
                    r = r + y.p.g.t + 1
                y = y.p
            return r
        
    # mettre à jour le précédeur et le successeur d'un noeud inséré
    def ajout_pred_succ(self, x):
        y = x.p
        if y == self.nil:
            x.succ = self.nil
            x.pred = self.nil
        else:
            if x == y.g:
                x.succ = y
                x.pred = y.pred
                x.succ.pred = x
                if x.pred != self.nil:
                    x.pred.succ = x
            else:
                x.pred = y
                x.succ = y.succ
                x.pred.succ = x
                if x.succ and x.succ != self.nil:
                    x.succ.pred = x

    # mettre à jour le précédeur et le successeur d'un noeud supprimé
    def supprimer_pred_succ(self, z):
        if z.pred:
            z.pred.succ = z.succ
        if z.succ:
            z.succ.pred = z.pred        

    # reconstruire l'arbre rouge-noir après l'insertion
    def inserer_correction_rn(self, z):
        while z.p.c == R:
            if z.p == z.p.p.g:
                y = z.p.p.d
                if y.c == R:
                    z.p.c = N
                    y.c = N
                    z.p.p.c = R
                    z = z.p.p
                elif z == z.p.d:
                    z = z.p                    
                    self.rotation_gauche(z)
                z.p.c = N
                z.p.p.c = R                
                self.rotation_droite(z.p.p)
            else:
                y = z.p.p.g
                if y.c == R:
                    z.p.c = N
                    y.c = N
                    z.p.p.c = R
                    z = z.p.p
                else:
                    if z == z.p.g:
                        z = z.p                    
                        self.rotation_droite(z)
                    z.p.c = N
                    z.p.p.c = R                
                    self.rotation_gauche(z.p.p) 
        self.racine.c = N
        
    # reconstruire l'arbre rouge-noir après la suppression
    def supprimer_correction_rn(self, x):
        while x != self.racine and x.c == N:
            if x == x.p.g:
                w = x.p.d
                if w.c == R:
                    w.c = N
                    x.p.c = R
                    self.rotation_gauche(x.p)
                    w = x.p.d
                if w.g.c == N and w.d.c == N:
                    w.c = R
                    x = x.p
                else:
                    if w.d.c == N:
                        w.g.c = N
                        w.c = R
                        self.rotation_droite(w)
                        w = x.p.d
                    w.c = x.p.c
                    x.p.c = N
                    w.d.c = N
                    self.rotation_gauche(x.p)
                    x = self.racine
            else:
                w = x.p.g
                if w.c == R:
                    w.c = N
                    x.p.c = R
                    self.rotation_droite(x.p)
                    w = x.p.g

                if w.d.c == N and w.g.c == N:
                    w.c = R
                    x = x.p
                else:
                    if w.g.c == N:
                        w.d.c = N
                        w.c = R
                        self.rotation_gauche(w)
                        w = x.p.g
                    w.c = x.p.c
                    x.p.c = N
                    w.g.c = N
                    self.rotation_droite(x.p)
                    x = self.racine
        x.c = N

    # transplater un sous arbre d'un noeud vers un autre
    def transplante_rn(self, u, v):
        if u.p == self.nil:
            self.racine = v
        elif u == u.p.g:
            u.p.g = v
        else:
            u.p.d = v
        v.p = u.p

    # rotation gauche à partir d'un noeud
    def rotation_gauche(self, x):
        print('\nrotation_gauche:%d' % x.k)
        y = x.d
        x.d = y.g
        if y.g != self.nil:
            y.g.p = x
        y.p = x.p
        if x.p == self.nil:
            self.racine = y
        elif x == x.p.g:
            x.p.g = y
        else:
            x.p.d = y
        y.g = x
        x.p = y
        # mettre à jour la taille des noeuds affectés par la rotation
        y.t = x.t
        x.t = x.g.t + x.d.t + 1        

    # rotation droite à partir d'un noeud
    def rotation_droite(self, x):
        print('\nrotation_droite:%d' % x.k)
        y = x.g
        x.g = y.d
        if y.d != self.nil:
            y.d.p = x
        y.p = x.p
        if x.p == self.nil:
            self.racine = y
        elif x == x.p.d:
            x.p.d = y
        else:
            x.p.g = y
        y.d = x
        x.p = y
        # mettre à jour la taille des noeuds affectés par la rotation
        y.t = x.t
        x.t = x.g.t + x.d.t + 1

    # trouver la clé minimale dans un arbre enraciné de x
    def arbre_min(self, x):
        while x.g != self.nil:
            x = x.g
        return x

    # afficher l'arbre en ordre croissant
    def affiche(self, title=None):
        x = self.min        
        if title:
            print(title)
        while x != self.nil:
            print(x, end=' ')                
            x = x.succ


n = RN_arbre([4, 7, 12, 15, 3, 5, 14, 18, 16, 17])



