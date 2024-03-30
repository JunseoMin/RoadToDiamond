import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dbjdic = {}
dbj = []
for _ in range(n):
    dbjdic[input().strip()] = True
for _ in range(m):
    name = input().strip()
    if dbjdic.get(name,False):
        dbj.append(name)
print(len(dbj))
for name in sorted(dbj):
    print(name)