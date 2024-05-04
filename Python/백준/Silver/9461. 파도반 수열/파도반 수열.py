import sys
input = sys.stdin.readline

N = int(input())

def padoban(n):
    if not memo[n]:
        memo[n] = padoban(n-2) + padoban(n-3)
        return memo[n]
    else:
        return memo[n]

for _ in range(N):
    memo = [1,1,1,1,2,2,3,4,5,7,9] + [0] * 91
    n = int(input())
    print(padoban(n))