import sys,math

input = sys.stdin.readline

b,n = map(str,input().split())
n = int(n)
m = len(b)-1
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

ans = 0
for i in range(m, -1 ,-1):
    k = 0
    sq = m -i
    if b[i] in alpha:
        k = alpha.index(b[i]) + 10
    else:
        k = int(b[i])
    ans += (math.pow(n,sq)*k)
    
print(int(ans))