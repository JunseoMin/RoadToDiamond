import math

def issosu(n):
    if n == 1:
        return False
    if n == 2:
        return True

    for i in range(2,int(math.sqrt(n))+1):
        if not (n%i):
            return False
    return True

_ = input()
ans = 0
tmps = list(map(int,input().split()))

for n in tmps:
    if issosu(n):
        ans+=1
print(ans)