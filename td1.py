import math


# page11 1.2.2
# n=1, 8>0
def find_num():
    n = 2
    while n > 1:
        if 8 * n * n > 64 * n * math.log(n, 2):
            return n - 1
        n += 1


num = find_num()
print('Number maximum which makes 8n^2 < 64nlgn est %d' % num)  # 44, donc


# page11 1.1
# 1s=10^6µs
def find_nums(fun, num):
    n = 1
    while n >= 1:
        if fun(n) > num:
            return n - 1
        n += 1


# n1=find_nums(lambda x:math.log(x,2), 10**6) # trop long
n2 = find_nums(lambda x: x * math.log(x, 2), 10 ** 6)  # 87848
# n3=find_nums(lambda x: x*math.log(x),10**6*3600) # 188909175
funs = [lambda x: x ** 3, lambda x: 2 ** x]
t = [10 ** 6, 10 ** 6 * 3600, 10 ** 6 * 3600 * 24 * 365 * 100]
nums = [[find_nums(a, b) for a in funs] for b in t]

print(nums)


# page19 2.1.4
def addition_binaire(arr1, arr2):
    num1 = num2 = 0
    for i in range(len(arr1)):
        num1 += arr1[i] * (2 ** arr1[i])
        num2 += arr2[i] * (2 ** arr2[i])
    sum = num1 + num2


def addBinary(v1, v2):
    if len(v1) > len(v2):
        v2 = [0] * (len(v1) - len(v2)) + v2
    elif len(v1) < len(v2):
        v1 = [0] * (len(v2) - len(v1)) + v1
    res = []
    retenue = 0
    for i in range(len(v1) - 1, -1, -1):
        somme = v1[i] + v2[i] + retenue
        res.insert(0, somme % 2)
        retenue = somme // 2
    if retenue == 1:
        res.insert(0, retenue)

    return res


print(addBinary([1, 1, 0, 1], [1, 1, 1]))


def tri_selection(t):
    n = len(t)
    for i in range(n - 1):
        min_v = i
        for j in range(i + 1, n):
            if t[j] < t[min_v]:
                min_v = j
        if min_v != i:
            t[i], t[min_v] = t[min_v], t[i]
    return t


a = [5, 7, 3, 4, 11]
print(tri_selection(a))


## initialisation
## conservation
## terminaison

#