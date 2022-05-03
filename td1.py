import math

# page11 1.2.2
# n=1, 8>0
def find_num():
    n=2
    while n > 1:
        if 8*n*n >= 64*math.log(n,2):
            return n
        n+=1

num = find_num() 
print('Number maximum which makes 8n^2 < 64nlgn est %d' % (num-1)) # 3, donc -> [2,3]

# page11 1.1
