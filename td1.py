import math

# page11 1.2.2
# n=1, 8>0
def find_num():
    n=2
    while n > 1:
        if 8*n*n >= 64*math.log(n):
            return n-1
        n+=1

num = find_num() 
print('Number maximum which makes 8n^2 < 64nlgn est %d' % num) # 2, donc -> [2]

# page11 1.1
# 1s=10^6µs
def find_nums(fun,num):
    n=1    
    while n >= 1:
        if fun(n) > num:
            return n-1
        n += 1

# n1=find_nums(lambda x:math.log(x), 10**6) # trop long
n2=find_nums(lambda x: x*math.log(x),10**6) #87848
# n3=find_nums(lambda x: x*math.log(x),10**6*3600) # 188909175
funs=[lambda x:x**3, lambda x:2**x]
t=[10**6, 10**6*3600, 10**6*3600*24*365*100]
nums = [[find_nums(a,b) for a in funs] for b in t]

print(nums)


# page19 2.1.4
def addition_binaire(arr1,arr2):
    pass

