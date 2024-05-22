import sys

input = sys.stdin.readline

N,M = map(int,input().split())
nli = list(map(int,input().split()))

acc_sum = [0]*(N+1)

for i in range(1,N+1):
    acc_sum[i] = acc_sum[i-1] + nli[i-1]

for _ in range(M):
    i,j = map(int,input().split())

    print(acc_sum[j] - acc_sum[i-1])