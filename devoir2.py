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
        return '(%s%s g:%s d:%s t:%s)' % \
                (
                 self.k, '*' if self.c == R else '',  
                 self.g.k if self.g else 'Nil', 
                 self.d.k if self.d else 'Nil', 
                 self.t if self.t else 0
                )


R = 'Rouge'
N = 'Noir'

class RN_arbre:

    nil = Noeud(None, N)     

    def __init__(self, tab):
        self.tab = tab        
        self.racine = self.nil
        self.min = self.minimum()
        self.max = self.maximum()
        self.contruire_RN_arbre()
    
    @property
    def tab(self):
        return self._tab


    @tab.setter
    def tab(self, val):
        if isinstance(any(val) != int):
            raise ValueError('Les éléments doivent être entiers')
        self._tab = val       


    def trouve_noeud(self, i): 
        x = self.racine       
        if x == self.nil or i == x.k:
            return x
        if x.k > i:
            return self.trouve_noeud(x.g, i)
        return self.trouve_noeud(x.d, i) 


    def contruire_RN_arbre(self):
        if len(self.tab) == 0:
            return self.racine
        for i in self.tab:
            self.arbre_inserer(i)
        return self


    def arbre_inserer(self, i):
        z = Noeud(i, R)
        y = self.nil        
        _noeud = self.trouve_noeud(i)
        if not _noeud:
            x = self.racine
            while x != self.nil:
                y = x
                if z.k < x.k:
                    x = x.g
                else:
                    x = x.d
            z.p = y
            if y == self.nil:
                self.racine = z
            elif z.k < y.k:
                y.g = z
            else:
                y.d = z
        z.g = self.nil
        z.d = self.nil
        z.c = R
        self.inserer_correction_rn()
        self.ajout_pred_succ(z)
        self.determine_rang(z)
        print('Après inserer_correction\n')
        self.affiche()


    def supprimer(self, i):
        z = Noeud(i, R)
        y = z
        y_c_originale = y.c
        _noeud = self.trouve_noeud(i)
        if not _noeud:
           if z.g == self.nil:
               x = z.d
               self.transplante_rn(z, z.d)
           elif z.d == self.nil:
               x = z.g
               self.transplante_rn(z, z.g)
           y = self.arbre_minimum(z.d)
           y_c_originale = y.c
           x = y.d
           if y.p == z:
               x.p = y
           self.transplante_rn(y, y.d)
           y.d = z.d
           y.d.p = y
           self.transplante_rn(z, y)
           y.g = z.g
           y.g.p = y
           y.c = z.c
        if y_c_originale == N:
            self.supprimer_correction_rn(x)


    def lire_rang(self, i):
        x = self.racine
        if x != self.nil:
            r = x.g.t + 1
            if i == r:
                return x
            elif i < x:
                return self.lire_rang(x.g, i)
            return self.lire_rang(x.d, i - r)


    def determine_rang(self, x):
        z = self.trouve_noeud(x)
        if z:
            r = z.g.t + 1
            y = z
            while y != self.racine:
                if y == y.p.d:
                    r = r + y.p.g.t + 1
                y = y.p
            return r
        

    def minimum(self):
        x = self.racine
        while x.g != self.nil:
            x = x.g
        return x 


    def maximum(self):
        x = self.racine
        while x.d != self.nil:
            x = x.d
        return x


    def ajout_pred_succ(self, x):
        
        return x.succ, x.pred


    def supprimer_pred_succ(self, z):
        
        return z.succ, z.pred


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
                elif z == z.p.d:
                    z = z.p                    
                    self.rotation_gauche(z)
                z.p.c = N
                z.p.p.c = R                
                self.rotation_droite(z.p.p) 


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
                elif w.d.c == N:
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
                    self.



    def transplante_rn(self, u, v):
        if u.p == self.nil:
            self.racine = v
        elif u == u.p.g:
            u.p.g = v
        else:
            u.p.d = v
        v.p = u.p


    def rotation_gauche(self, x):
        print('rotation_gauche:%d' % x.k)
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


    def rotation_droite(self, x):
        print('rotation_droite:%d' % x.k)
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

    def arbre_minimum(self, x):
        pass


    def affiche(self, title=None):
        x = self.racine
        if title:
            print(title)
        if x == self.nil:
            print(x)
        else:
            while x != self.nil:
                print(x, end=' ')
                x = x.succ



n = Noeud()
print(n)