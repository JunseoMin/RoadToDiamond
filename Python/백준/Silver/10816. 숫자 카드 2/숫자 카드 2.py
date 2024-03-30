import sys
input = sys.stdin.readline

_ = int(input())
nli = list(map(int,input().split()))
_ = int(input())
mli = list(map(int,input().split()))
ndic = {}
for i in nli:
    tmp = 0
    tmp = ndic.get(i,0)
    ndic[i] = tmp + 1
for m in mli:
    print(ndic.get(m,0),end = ' ')