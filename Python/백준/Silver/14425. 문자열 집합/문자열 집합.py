import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ndic = {};ans = 0

for _ in range(n):
    ndic[input().strip()] = 1
for __ in range(m):
    ans += ndic.get(input().strip(),0)
print(ans)