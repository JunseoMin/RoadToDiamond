import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nli = list(map(int, input().split()))

sumli = [0] * N
rli = [0] * M

ans = 0
sumli[0] = nli[0] % M
rli[sumli[0]] += 1
if sumli[0] == 0:
    ans += 1

for i in range(1, N):
    sumli[i] = (sumli[i-1] + nli[i]) % M
    if sumli[i] == 0:
        ans += 1
    rli[sumli[i]] += 1

for i in range(M):
    if rli[i] > 1:
        ans += rli[i] * (rli[i] - 1) // 2

print(ans)

'''
5 3
1 2 3 1 2
'''
