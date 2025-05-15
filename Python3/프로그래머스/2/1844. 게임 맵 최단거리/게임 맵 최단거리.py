from collections import deque

def solution(maps):
    answer = 0
    queue = deque([(0,0,1)])
    visited = set()
    costs = [100000]
    
    while queue:
        x,y,cost = queue.popleft()
        if (x,y) in visited:
            continue
        if cost > min(costs):
            continue
        visited.add((x,y))
        
        if (x,y) == (len(maps[0]) - 1, len(maps) - 1):
            return cost
        
        if x+1 < len(maps[0]) and maps[y][x+1] == 1 and (x+1,y) not in visited:
            queue.append((x+1,y,cost+1))        
        if y+1 < len(maps) and maps[y+1][x] == 1 and (x,y+1) not in visited:
            queue.append((x,y+1,cost+1))
        if x-1 >= 0 and maps[y][x-1] == 1 and (x-1,y) not in visited:
            queue.append((x-1,y,cost+1))
        if y-1 >= 0 and maps[y-1][x] == 1 and (x,y-1) not in visited:
            queue.append((x,y-1,cost+1))
    
    return -1