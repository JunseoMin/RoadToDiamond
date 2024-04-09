import math

def comb_len(n,r):
    #nCr
    r = n-r if n-r < r else r
    tmp1 = 1
    for up in range(n,n-r,-1):
        tmp1 *= up
    return tmp1//math.factorial(r)


_n,_r = map(int,input().split())
print(comb_len(_n,_r))