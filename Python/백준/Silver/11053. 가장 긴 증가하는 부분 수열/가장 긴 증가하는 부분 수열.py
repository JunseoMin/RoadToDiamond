import sys
input = sys.stdin.readline

N = int(input())

nli = list(map(int,input().split()))
dp = [1] * 1001

for i in range(1,N):
    for j in range(i):
        if nli[i] > nli[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp[:10])
print(max(dp))