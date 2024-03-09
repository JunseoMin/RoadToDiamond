import sys

input = sys.stdin.readline

small = -1*float('inf')
ans = -1

for i in range(9):
    k = int(input())
    
    if small < k:
        small = k
        ans = i

print(small)
print(ans+1)