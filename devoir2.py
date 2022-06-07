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


    def __str__(self):
        return 'Noeud courant :\n\
                -> Clé: %s\n\
                -> Couleur: %s\n\
                -> Parent: %d\n\
                -> Enfant gauche: %d\n\
                -> Enfant droite: %d\n\
                -> Taille: %d\n\
                -> Précédeur: %d\n\
                -> Successeur: %d\n' % \
                (
                 self.k, self.c, self.p.k, 
                 self.g.k, self.d.k, self.t,  
                 self.pred.k, self.succ.k 
                )

class RN_arbre:

    def __init__(self, tab):
        self.tab = tab

        self.construire_RN_arbre()
    
    @property
    def tab(self):
        return self._tab

    @tab.setter
    def tab(self, val):
        if isinstance(any(val) != int):
            raise ValueError
        self._tab = val       


    def trouve_noeud(self, i):
        racine = Noeud(self.tab[0], 'Noir')
        if self.tab == [] or self.k == i:
            return self
        elif self.k > i:
            return self.trouve_noeud(self.g, i)
        return self.trouve_noeud(self.d, i) 

    
    def arbre_inserer(self, i):
        z = Noeud(i, 'Rouge')
        y = Noeud()
        noeud_original = self.trouve_noeud(i)
        if not noeud_original:
            racine = self.trouve_noeud(self.tab[0])
            while racine.k:
                y = racine
                if z.k < racine.k:
                    racine = racine.g
                else:
                    racine = racine.d
            z.p = y
            if not y.k:
                racine = z
            elif z.k < y.k:
                y.g = z
            else:
                y.right = z
        self.inserer_correction_rn()


    def supprimer(self, i):
        z = Noeud(i, 'Rouge')
        noeud_original = self.trouve_noeud(i)
        if not noeud_original:
           pass


    def lire_range(self, i):
        pass


    def determine_rang(self, x):
        pass


    def minimum(self):
        pass


    def maximum(self):
        pass


    def ajout_pred_succ(self, x):
        pass


    def supprimer_pred_succ(self, z):
        pass


    def inserer_correction_rn(self):
        pass 


    def supprimer_correction_rn(self):
        pass


    def transplante_rn(self):
        pass


    def rotation_droite(self):
        pass


    def rotation_gauche(self):
        pass


    def arbre_minimum(self, x):
        pass


    def affiche(self):
        pass