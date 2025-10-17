import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())

maps = []
conditioner = []
for r in range(R):
    arr = list(map(int,input().split()))
    maps.append(arr)
    if arr[0] == -1:
        conditioner.append((r,0))
        
up = conditioner[0][0]
down = conditioner[1][0]
t = 0
while t < T:
    tmpMap = [[0 for _ in range(C)] for __ in range(R)]
    spreaded = set()
    conditioner = []
    for r in range(R):
        for c in range(C):
            if maps[r][c] == 0:
                continue
            
            if maps[r][c] != -1:
                cnt = 0
                acc = maps[r][c] // 5
                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr = r + dr
                    nc = c + dc
                
                    #그 칸이 없으면
                    if nr >= R or nr < 0:
                        continue
                    if nc >= C or nc < 0:
                        continue
                    # 공기청정기가 있거나
                    if maps[nr][nc] == -1:
                        continue
                    
                    spreaded.add((nr,nc))
                    tmpMap[nr][nc] += acc
                    cnt += 1
                maps[r][c] -= acc * cnt
                    
    for r,c in spreaded:
        maps[r][c] += tmpMap[r][c]
    
    
    for r in range(up-1, 0, -1):
        maps[r][0] = maps[r-1][0]
    for c in range(C-1):
        maps[0][c] = maps[0][c+1]
    for r in range(up):
        maps[r][C-1] = maps[r+1][C-1]
    for c in range(C-1, 1, -1):
        maps[up][c] = maps[up][c-1]
    maps[up][1] = 0  # 공기청정기 옆은 깨끗한 공기

    # --- 아래쪽 시계 방향 ---
    for r in range(down+1, R-1):
        maps[r][0] = maps[r+1][0]
    for c in range(C-1):
        maps[R-1][c] = maps[R-1][c+1]
    for r in range(R-1, down, -1):
        maps[r][C-1] = maps[r-1][C-1]
    for c in range(C-1, 1, -1):
        maps[down][c] = maps[down][c-1]
    maps[down][1] = 0
    
    t+=1

answer = 0
for r in range(R):
    for c in range(C):
        if maps[r][c] > 0:
            answer += maps[r][c]
print(answer)