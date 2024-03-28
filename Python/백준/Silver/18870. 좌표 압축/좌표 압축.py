import sys
input = sys.stdin.readline
_ = int(input())
nli = list(map(int,input().split()))
nset = sorted(list(set(nli)))

ndic = {}
for i in range(len(nset)):
    ndic[nset[i]] = i

for n in nli:
    print(str(ndic[n]),end=" ")