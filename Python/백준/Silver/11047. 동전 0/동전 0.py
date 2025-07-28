import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))
 
answer = 0

for __ in range(n):
    coin = coins.pop()
    currCoin = (k // coin)
    answer += currCoin
    
    k -= (k // coin) * coin

print(answer)