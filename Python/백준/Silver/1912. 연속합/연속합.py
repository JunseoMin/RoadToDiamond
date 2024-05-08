import sys

input = sys.stdin.readline

N = int(input())
nli = list(map(int,input().split()))
max_val = -float('inf')

for i in range(1,N):
    nli[i] = max(nli[i],nli[i]+nli[i-1])
    if nli[i] > max_val:
        max_val = nli[i]

if nli[0] > max_val:
    max_val = nli[0]

print(max_val)