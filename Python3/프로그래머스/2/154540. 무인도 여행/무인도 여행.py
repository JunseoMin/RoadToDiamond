from collections import deque

def solution(maps):
    answer = []
    visited = set()
    
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'X' or (r,c) in visited:
                continue
            value = 0                
            queue = deque([(r,c)])
            visited.add((r,c))
            
            while queue:
                pr,pc = queue.popleft()
                value += int(maps[pr][pc])
                for dr,dc in  [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr,nc = pr + dr, pc + dc
                    
                    if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]):
                        if (nr,nc) not in visited and maps[nr][nc] != 'X':
                            queue.append((nr,nc))
                            visited.add((nr,nc))
            answer.append(value)
    
    return sorted(answer) if len(answer) > 0 else [-1]