import sys
from collections import deque
input = sys.stdin.readline
'''
chcek 0 1 1 0
nli 1 2 3 4
M 3
mli 2 4 7
'''
N = int(input())

check = list(map(int,input().split()))
nli = list(map(int,input().split()))
M = int(input())
mli = list(map(int,input().split()))

deq = deque()

for i in range(N):
    if not check[i]:
        deq.append(nli[i])
for m in mli:
    deq.appendleft(m)
    print(deq.pop(),end = ' ')
