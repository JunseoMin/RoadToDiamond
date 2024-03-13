import sys

input = sys.stdin.readline

square = [[0 for _ in range(100)] for __ in range(100)]

n = int(input())

for _ in range(n):
    x,y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            square[y+i][x+j] = 1
    

print(sum(sli.count(1) for sli in square))    
