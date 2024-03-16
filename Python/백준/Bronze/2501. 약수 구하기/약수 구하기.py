import sys

input = sys.stdin.readline

n,k = map(int,input().split())
i = 1
ans = 1

if k == 1:
    print(1)
    sys.exit()

while i <= n:
    i+=1
    if not n%i:
        ans+=1
        if ans == k:
            print(i)
            sys.exit()

print(0)