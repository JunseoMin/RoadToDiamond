import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tmp = 0
bucket = [i for i in range(1,n+1)]
ans=""

for i in range(m):
    i,j = map(int,input().split())
    i-=1
    j-=1
    tmp = bucket[i]
    bucket[i] = bucket[j]
    bucket[j] = tmp
    
for i in range(n):
    ans += (str(bucket[i]) + " ")
    
print(ans[:-1])