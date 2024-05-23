import sys

input = sys.stdin.readline

N,K = map(int,input().split())

tmps = list(map(int,input().split()))

acc_sum = [0] * (N - K +1)
acc_sum[0] = sum(tmps[:K])

for i in range(1,N - K +1):
    acc_sum[i] = acc_sum[i-1] - tmps[i-1] + tmps[i + K - 1]

print(max(acc_sum))