import sys

n = int(sys.stdin.readline())

for _ in range(1,n+1):
    a,b = map(int,sys.stdin.readline().split())
    print('Case #' + str(_) + ": " + str(a+b))