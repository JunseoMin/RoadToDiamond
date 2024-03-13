import sys

input = sys.stdin.readline

n,m = map(int,input().split())

summat = [[0 for i in range(m)] for _ in range(n)]

A = []
B=[]

for _ in range(2*n):
    A = list(map(int,input().split()))
    for k in range(m):
        summat[_%n][k%m] += A[k]

for i in range(n):
    tmp = ''
    for j in range(m):
        tmp += str(summat[i][j]) + " "
    print(tmp[:-1])