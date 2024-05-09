import sys
input = sys.stdin.readline

N = int(input())

nli = []

for _ in range(N):
    nli.append(list(map(int,input().split())))

dp = [[0]*3 for _ in range(N)]

dp[0] = nli[0]

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + nli[i][0] # select red
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + nli[i][1] # select green
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + nli[i][2] # select blue


print(min(dp[N-1]))