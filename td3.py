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
from turtle import left


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


def find_max_crossing_subarray(arr,low,mid,high):
    left_sum = float('-inf')
    sum, max_left, max_right = 0, 0, 0
    for i in range(mid, low+1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for j in range(mid+1, high+1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(arr, low, high):
    if low == high:
        return (low, high, arr[low])
    else:
        mid = (low + high)//2
        (left_low, left_high, left_sum) = find_maximum_subarray(arr, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(arr, mid+1, high)
        (cross_low, cross_hight, cross_sum) = find_max_crossing_subarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_hight, cross_sum)

arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(find_maximum_subarray(arr, 0, len(arr)-1))