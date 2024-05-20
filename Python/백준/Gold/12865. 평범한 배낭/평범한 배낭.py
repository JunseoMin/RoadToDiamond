import sys

input = sys.stdin.readline

N,K = map(int,input().split())

napsec = []

for _ in range(N):
    napsec.append(list(map(int,input().split())))

dp = [0]*100001 # maximum value

for w,v in napsec:
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i],dp[i-w] + v)

print(dp[K])