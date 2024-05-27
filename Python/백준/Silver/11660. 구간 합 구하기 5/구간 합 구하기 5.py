import sys

input = sys.stdin.readline

N,M = map(int,input().split())

nli = []

for _ in range(N):
    nli.append(list(map(int,input().split())))

prefix = [[0]*(N+1) for _ in range(N+1)]


for i in range(1,1+N):
    for j in range(1,N+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + nli[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])

'''
4 3 y1y2
1 2 3 4 
2 3 4 5 x1
3 4 5 6 x2
4 5 6 7
'''
# 2 2 3 4
# 3 3 4 4