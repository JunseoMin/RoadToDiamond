import sys
input = sys.stdin.readline
n,m = map(int,input().split())

n_li = [i for i in range(m+1)]
n_li[0]=0; n_li[1]=0

for i in range(2,m+1):
    if not (n_li[i]):
        continue

    for j in range(i*2,m+1,i):
        n_li[j] = 0

for i in range(n,m+1):
    if n_li[i]:
        print(n_li[i])
