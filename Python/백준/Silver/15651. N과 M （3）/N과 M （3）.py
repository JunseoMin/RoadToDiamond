import sys

n,m = map(int,sys.stdin.readline().split())
checked = set()

def dfs(depth=0,tup = tuple()):
    if depth == m:
        checked.add(tup)
        return
    for i in range(1,n+1):
        dfs(depth + 1, tup + (i,))

dfs()
for t in sorted(checked):
    for i in t:
        print(i,end=' ')
    print()
    