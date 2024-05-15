import sys
input = sys.stdin.readline

drinks = []
dp = [0] * 10001

N = int(input())

for _ in range(N):
    drinks.append(int(input()))


if N < 3:
    dp[0] = drinks[0]

    if N > 1:
        dp[1] = drinks[1] + dp[0]

    if N > 2:
        dp[2] = max(max(drinks[0]+drinks[2],drinks[1]+drinks[2]),dp[1])
        
    print(dp[N-1])
    sys.exit()



dp[0] = drinks[0]
dp[1] = drinks[1] + dp[0]
dp[2] = max(max(drinks[0]+drinks[2],drinks[1]+drinks[2]),dp[1])

for i in range(3,N):
    dp[i] = max(dp[i-2] + drinks[i],dp[i-3] + drinks[i] + drinks[i-1],dp[i-1])

print(dp[N-1])