import sys,math
input = sys.stdin.readline

def is_sosu(n):
    if not n or n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if not(n % i):
            return False
    return True
    

N = int(input())

for _ in range(N):
    _n = int(input())
    while(not is_sosu(_n)):
        _n+=1
    print(_n)