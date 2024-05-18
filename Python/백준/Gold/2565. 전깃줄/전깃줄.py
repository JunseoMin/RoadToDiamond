import sys

input = sys.stdin.readline

N = int(input())
wli = []

dp = [1]*101

for i in range(N):
    wli.append(list(map(int,input().split())))

wli.sort()

for i in range(1,N):
    for j in range(i):
        if wli[i][1] > wli[j][1]:
            dp[i] = max(dp[i],dp[j] + 1)

ans = max(dp)
print(N - ans)