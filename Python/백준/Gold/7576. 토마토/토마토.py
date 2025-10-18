import sys
from collections import deque
input = sys.stdin.readline

C,R = map(int,input().split())

grid = []
queue = deque([])
full = C*R
for r in range(R):
    arr = list(map(int,input().split()))
    grid.append(arr)
    for c in range(C):
        if arr[c] == 1:
            queue.append((r,c))
        if arr[c] == -1:
            full += arr[c]
day = 0

#최대한 확인한 후
while queue:
    for _ in range(len(queue)):  
        r,c = queue.popleft()
        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                queue.append((nr,nc))
    day += 1
    
flag = True
# 전체에서 남은 0개수 확인
for r in range(R):
    for c in range(C):
        if grid[r][c] == 0:
            flag = False
print(day - 1) if flag else print(-1)
