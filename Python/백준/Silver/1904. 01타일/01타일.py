import sys
N = int(input())

if N == 1:
    print(1)
    sys.exit()

dp = [0] * (N + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N])