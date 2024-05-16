N = int(input())
nli = list(map(int,input().split()))

dp_bigger = [1] * 1001
dp_lower = [1] * 1001
dps = [0]*1001

dp_lower[1] = 1     #right
dp_bigger[N] = 1    #left

for i in range(1,N+1):
    for j in range(1,i):
        if nli[i-1] > nli[j-1]:
            dp_bigger[i] = max(dp_bigger[i],dp_bigger[j] + 1)

    k = N+1 - i

    for j in range(N,k-1,-1):
        if nli[k-1] > nli[j-1]:
            dp_lower[k] = max(dp_lower[k],dp_lower[j] + 1)

maxi = -float('inf')
for i in range(N+1):
    sums = dp_bigger[i] + dp_lower[i] -1

    if sums > maxi:
        maxi = sums

print(maxi)