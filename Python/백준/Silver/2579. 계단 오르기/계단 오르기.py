import sys
input = sys.stdin.readline

N = int(input())

stair = []
dp = [0] * N

for _ in range(N):
    stair.append(int(input()))


if N == 1:
    print(stair[0])
    sys.exit()
if N == 2:
    print(sum(stair))
    sys.exit()
    

dp[0] = stair[0]
dp[1] = stair[1] + dp[0]
dp[2] = max(stair[0]+stair[2],stair[1]+stair[2])

for i in range(3,N):
    dp[i] = max(stair[i] + stair[i-1] + dp[i-3],stair[i] + dp[i-2])


print(dp[N-1])
