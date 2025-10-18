import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())
grid = []
for _ in range(R):
    grid.append(input().strip())

queue = deque([(0,0,1)])
visited = set()
while queue:
    r,c,v = queue.popleft()
    
    if (r,c) == (R-1,C-1):
        print(v)
        break
    
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if (nr,nc) not in visited and grid[nr][nc] == "1":
                queue.append((nr,nc,v+1))
                visited.add((nr,nc))