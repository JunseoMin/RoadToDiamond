import sys

N = int(input())

if not N:
    print(1)
    sys.exit()

def reculsive(n):
    if n == 1:
        return 1
    return n*reculsive(n-1)

print(reculsive(N))