from collections import deque

def bfs(start,target,maps):
    sr,sc = start
    queue = deque([(sr,sc,0)])
    
    mr = len(maps)
    mc = len(maps[0])
    visited = [[False for _ in range(mc)] for __ in range(mr)]
    visited[sr][sc] = True
    
    while queue:
        r,c,cost = queue.popleft()
        
        if (r,c) == target:
            return cost
        
        
        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < mr and 0 <= nc < mc and not visited[nr][nc]:
                if maps[nr][nc] == 'X':
                    continue
                queue.append((nr,nc,cost + 1))
                visited[nr][nc] = True
    return -1

def solution(maps):
    answer = 0
    S = None; E = None; L = None;
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'S':
                S = (r,c)
            if maps[r][c] == 'E':
                E = (r,c)
            if maps[r][c] == 'L':
                L = (r,c)
    
    a1 = bfs(S,L,maps)
    if a1 == -1:
        return -1
    a2 = bfs(L,E,maps)
    if a2 == -1:
        return -1
    
    return a1 + a2