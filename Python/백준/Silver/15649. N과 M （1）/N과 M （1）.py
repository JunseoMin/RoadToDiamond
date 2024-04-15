import sys
from itertools import permutations

input = sys.stdin.readline
n,m = map(int,input().split())

ans = permutations([i for i in range (1,n+1)],m)

for a in ans:
    for val in a:
        print(val , end=' ')
    print()