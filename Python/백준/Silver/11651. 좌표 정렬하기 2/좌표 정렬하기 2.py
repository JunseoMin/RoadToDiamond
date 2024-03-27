import sys
input = sys.stdin.readline
n = int(input())
coord = []
for _ in range(n):
    x,y = map(int,input().split())
    coord.append([y,x])
    
coord.sort()

for i in range(n):
    print(str(coord[i][1]) + " " + str(coord[i][0]))