# class Matrice:
#     def __init__(self,r,c):
#         self._tableau = [[0 for x in range(c)] for y in range(r)]

#     def get(self, i, j):
#         return self._tableau[i][j]

#     def set(self, i, j, val):
#         self._tableau[i][j] = val

# def matrix_chain_order(p):
#     n = len(p) - 1
#     m = Matrice()
def o_fib(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return o_fib(n-1) + o_fib(n-2)

def fib(n):
    fib_tableau = (n+1) * [-1]
    fib_tableau[0] = 0
    fib_tableau[1] = 1
    fib_aux(fib_tableau, n)
    print(fib_tableau)
    return fib_tableau[n]

def fib_aux(tab, n):
    if tab[n] >= 0:
        return tab[n]
    tab[n] = fib_aux(tab, n-1) + fib_aux(tab, n-2)
    return tab[n]

print(o_fib(5))
fib(5)
