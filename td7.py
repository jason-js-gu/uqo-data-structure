
class Noeud:
    def __init__(self, cle, g=None, d=None, p=None):
        self.cle = cle
        self.g = g
        self.d = d
        self.p = p



    def inorder_tree_walk(self):
        if self.cle:
            self.g.inorder_tree_walk()
            print(self.cle)
            self.d.inorder_tree_walk()


    def inorder_tree_walk_nonrecursive(x):
        pass




nil=Noeud(None)
n2 = Noeud(2,nil,nil)
n4 = Noeud(4,nil,nil)
n3 = Noeud(3,n2,n4)
n6 = Noeud(6,n3)
n7 = Noeud(7)
n7.p = n6
n13 = Noeud(13)
n13.d = nil
n13.p = n7
n9 = Noeud(9,nil,nil)
n9.p = n13
n6.d = n7
n7.d = n13
n7.g = nil
n13.g = n9
n15 = Noeud(15,n6)
n18 = Noeud(18)
n18.p = n15
n17 = Noeud(17,nil,nil)
n17.p = n18
n20 = Noeud(20,nil,nil)
n20.p = n18
n15.d = n18
n18.g, n18.d = n17, n20





n15.inorder_tree_walk()



# page 291
# rotation à droit, le noeud qui monte perd son enfant droite qui devient l'enfant gauche du noeud qui decend

# 13.1.6
"""
N_max est obtenu lorsque pendant de la racine, on alterne noeud noir - noeud rouge - noeud noir et on constitut un graphe complet
On obtient un graphe de hauteur h = 2k
mais le nombre d'un graphe complet de hauteur est : n_max = 2**(h+1) - 1 = 2**(2k) - 1

n_min=2**k - 1
"""

# 13.1.7
"""
le nombre de noeuds rouges est nr = 2**1 + 2**3 + ... + 2**(2k-1)
le nombre de noeuds noirs est nn = 2**0 + 2**3 + ... + 2**(2k-2)

le ratio maximum est: nr/nb = (2**1 + 2**3 + ... + 2**(2k-1)) / (2**0 + 2**3 + ... + 2**(2k-2))
                            = 2 * (2**1 + 2**3 + ... + 2**(2k-1)) / 2 * (2**0 + 2**3 + ... + 2**(2k-2))
                            = 2 * (2**1 + 2**3 + ... + 2**(2k-1)) / (2**1 + 2**3 + ... + 2**(2k-1))
                            = 2

le ratio minimum est obtenu lorsque l'arbre n'a pas de noeud rouge, donc le ratio minimum est 0
"""