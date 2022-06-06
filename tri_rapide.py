def tri_rapide(tab):
    tri_sous_tableau_rapide(tab, 0, len(tab)-1)     
    
def tri_sous_tableau_rapide(tab, p, r):      
    if p < r:
        q = partition(tab, p, r)        
        tri_sous_tableau_rapide(tab, p, q-1)        
        tri_sous_tableau_rapide(tab, q+1, r) 

def partition(A, p, r): 
    # prendre le dernier élément comme pivot
    pivot = A[r]
    # pointeur gauche   
    i = p - 1
    # pointeur droite
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


"""
Une autre méthode de force brute
"""
# force brute
def tri_rapide_brute(L=[4,2,1,8,7,5,3,6]): 
    plusPetits,equals,plusGrands=[],[],[]
    if len(L)>1:
        pivot=L[-1]        
        for i in L:
            if i<pivot:
                plusPetits.append(i)
            elif i==pivot:
                equals.append(i)
            else:
                plusGrands.append(i)
        return tri_rapide_brute(plusPetits) + equals + tri_rapide_brute(plusGrands)
    return L

# tests
print(tri_rapide_brute())    # [1, 2, 3, 4, 5, 6, 7, 8]
print(tri_rapide_brute([2,1,1,6,4,2]))  # [1, 1, 2, 2, 4, 6]
print(tri_rapide_brute([]))  # []


tests = [
    {'entrée':[],'sortie':[]},
    {'entrée':[4],'sortie':[4]},
    {'entrée':[9,3],'sortie':[3,9]},
    {'entrée':[4,9,4],'sortie':[4,4,9]},
    {'entrée':[9,4,4,3],'sortie':[3,4,4,9]},
    {'entrée':[3,9,4,4,3],'sortie':[3,3,4,4,9]},
    {'entrée':[3,9,9,4,4,3],'sortie':[3,3,4,4,9,9]},
    {'entrée':[3,6,7,2,4,5,4],'sortie':[2,3,4,4,5,6,7]},
    {'entrée':[4,2,1,8,7,5,3,6],'sortie':[1,2,3,4,5,6,7,8]},
    {'entrée':[0,7,5,1,2,4,8,3,6],'sortie':[0,1,2,3,4,5,6,7,8]},
    {'entrée':[2,5,3,3,-1,0,9,0,0,7],'sortie':[-1,0,0,0,2,3,3,5,7,9]}
]

for i in tests:
    entree = i['entrée']
    sortie = i['sortie']
    tri_rapide(entree)
    print(entree == sortie)
