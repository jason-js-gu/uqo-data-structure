
# pile
import ctypes

class Pile:
    def __init__(self, taille):
        self._top = -1
        self._capacity = taille
        self._P = (self._capacity * ctypes.py_object)()

    def isEmpty(self):
        return self._top == -1

    def emplier(self, x):
        if self._top == self._capacity -1:
            raise ValueError("Pile pleine: ", x, " ne peut étre ajouté") 
        self._top += 1
        self._P[self._top] = x
        return self

    def depiler(self):
        if self._top == -1:
            raise ValueError("Ne peut depiler car la pile est vide")
        X = self._P[self._top]
        self._top -= -1
        return X

    def afficher(self):
        print("[", end='')
        for i in range(self._top+1): 
            print(self._P[i], end=', ')
        print("]")



P = Pile(6)
P.emplier(4)
P.afficher()
P.emplier(1)
P.afficher()
P.emplier(3)
P.afficher()
P.depiler()
P.afficher()