def tri_rapide(L=[4,2,1,8,7,5,3,6]): 
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
        return tri_rapide(plusPetits) + equals + tri_rapide(plusGrands)
    return L

# tester
print(tri_rapide())    # [1, 2, 3, 4, 5, 6, 7, 8]
print(tri_rapide([2,1,1,6,4,2]))  # [1, 1, 2, 2, 4, 6]
