import sys
input = sys.stdin.readline

n = int(input()); coord = []

for _ in range(n):
    coord.append(list(map(int,input().split())))
coord.sort()
for c in coord:
    print( str(c[0])+ " " + str(c[1]))