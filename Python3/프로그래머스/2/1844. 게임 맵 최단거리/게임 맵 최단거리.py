from collections import deque

def bfs(start, maps, target):
    queue = deque([(start[0], start[1], 1)])
    visited = set([start])
    
    
    while queue:
        x,y,d = queue.popleft()
        
        if (x,y) == target:
            return d
        
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            mx = x + dx
            my = y + dy
            
            if mx >= len(maps[0]) or mx < 0 or my >= len(maps) or my < 0:
                continue
            
            if maps[my][mx] == 1 and (mx,my) not in visited:
                queue.append((mx,my,d+1))
                visited.add((mx,my))
            
    return -1
    

def solution(maps):
    answer = 0    
    answer = bfs((0,0),maps,(len(maps[0]) -1,len(maps) - 1))
    
    
    return answer
