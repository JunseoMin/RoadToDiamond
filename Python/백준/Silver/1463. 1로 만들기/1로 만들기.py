import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 1000001

dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
if n < 5:
    print(dp[n])
    sys.exit()


for i in range(5,n+1):
    dp[i] = 1 + min(dp[i-1], dp[i//2] if not i%2 else float('inf'), dp[i//3] if not i%3 else float('inf'))

print(dp[n])