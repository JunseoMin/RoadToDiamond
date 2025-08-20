import sys
input = sys.stdin.readline

def reculsive(x,y,size):
    v = datas[x][y]        
    div = size // 2
    for i in range(x, x + size):
        for j in range(y, y + size):
            if datas[i][j] != v:
                return "(" + reculsive(x,y,div) + reculsive(x,y+div,div) + reculsive(x+div,y,div) + reculsive(x+div,y+div,div) + ")"
    return str(v)

datas = []
N = int(input())
for _ in range(N):
    datas.append(list(map(int,input().strip())))

print(reculsive(0,0,N))