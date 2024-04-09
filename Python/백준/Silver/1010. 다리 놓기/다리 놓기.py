import math

def combination(n,r):
    r = n-r if r > n-r else r
    tmp = 1
    for nn in range(n,n-r,-1):
        tmp *= nn
    return tmp//math.factorial(r)
N = int(input())

for _ in range(N):
    _r,_n = map(int,input().split())
    print(combination(_n,_r))