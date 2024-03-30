import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ndic = dict(zip(list(map(int,input().split())),[1 for _ in range(n)]))
mli = list(map(int,input().split()))
tmp = 0
for m in mli:
    tmp += ndic.get(m,0)
print(len(ndic) + len(mli) - 2*tmp)