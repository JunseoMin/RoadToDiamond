import sys
input = sys.stdin.readline
N = int(input())
nli = list(map(int,input().split()))
_ = input()
mli = list(map(int,input().split()))
ndic = dict(zip(nli,(1 for _ in range(N))))
for m in mli:
    print(ndic.get(m,0),end = " ")