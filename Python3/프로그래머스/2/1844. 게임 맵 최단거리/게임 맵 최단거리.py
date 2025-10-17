from collections import deque

def solution(maps):
    answer = 0
    
    queue = deque([(0,0,1)])
    visited = set()
    
    R = len(maps)
    C = len(maps[0])
    
    while queue:
        r,c,v = queue.popleft()
        
        if (r,c) == (R-1,C-1):
            return v
        
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = r + dr
            nc = c + dc
            
            if (0 <= nr < R) and (0 <= nc < C):
                if maps[nr][nc] and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc,v+1))
    return -1