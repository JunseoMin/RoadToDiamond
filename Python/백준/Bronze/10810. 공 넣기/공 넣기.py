import sys

input = sys.stdin.readline

ans = ""
n,m = map(int,input().split())
nlist = [0 for _ in range(n)]

for i in range(m):
    i,j,k = map(int,input().split())
    for _ in range(i-1,j):
        nlist[_] = k

for i in range(n):
    ans += (str(nlist[i]) + " ")

print(ans[:-1])