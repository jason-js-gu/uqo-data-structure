# 6.1.2 page 123
# un tas à n éléments a une hauteur de logn
"""
Une seule feuille, hauteur h
len_n_min = 1+ 2**(h-1)+2**(h-2) + ... + 2**0
          = (2**h-1)/(2-1)=2**h

arbre complet
len_n_max = 2**h + 2**(h-1) + ... + 2**0 = (2**(h+1)-1)/(2-1)=2**(h+1)-1

donc len_n_min <= len_n <= len_n_max
2**h <= len_n <= 2**(h+1)-1<2**(h+1)
h <= lglen_n < h+1
donc entier partie de lglen_n = h
https://ita.skanev.com/14/02/01.html
1+x+x**2+...+x**n=(x**(n+1) -1)/(x-1)
"""

# 6.2.1 page 125
A=[27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

# def max_heap(A, i):
#     imax = i
#     l = 2*i
#     r = 2*i + 1
#     if l < len(A) and r < len(A) and A[l] > A[i] and A[l] >= A[r]:
#         A[l], A[i] = A[i], A[l]
#         imax = l
#     elif r < len(A) and A[r] > A[i] and A[r] >= A[l]:
#         A[r], A[i] = A[i], A[r]
#         imax = r

#     max_heap(A, imax)

# max_heap(A, 3)


"""
6.3.3 page 129
n = N_g + N_d

"""


# hachage

arr = [5,28,19,15,20,33,12,17,10]


# h(k) = (h1(k)+ih2(k))mod249

