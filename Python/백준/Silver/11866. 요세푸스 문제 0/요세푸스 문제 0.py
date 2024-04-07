import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
nli = deque([i for i in range(1,N+1)])
cnt = 1
ans = []
while nli:
    if cnt % K:
        nli.append(nli.popleft())
    else:
        ans.append(nli.popleft())    
    cnt += 1

print('<' + str(ans)[1:-1] + '>')
    