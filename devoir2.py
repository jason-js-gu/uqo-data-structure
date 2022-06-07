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
        if self.tab == [] or self.k == i:
            return self
        elif self.k > i:
            return self.trouve_noeud(self.g, i)
        return self.trouve_noeud(self.d, i) 

    
    def arbre_inserer(self, i):
        z = Noeud(i, 'Rouge')
        noeud_original = self.trouve_noeud(i)
        if noeud_original:
            noeud_original.k = i
            noeud_original.c = z.c
            self.inserer_correction_rn()
        else:
            pass
            