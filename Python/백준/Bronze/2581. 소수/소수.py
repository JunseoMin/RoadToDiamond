import math

def issosu(n):
    if n == 1:
        return False
    if n == 2:
        return True
    
    for i in range(2,int(math.sqrt(n))+1):
        if not(n%i):
            return False
    return True
    

m = int(input())
n = int(input())
ssl = []
for i in range(m,n+1):
    if issosu(i):
        ssl.append(i)
        
if len(ssl):
    print(sum(ssl))
    print(ssl[0])
else:
    print(-1)
        