from collections import deque

def solution(land):
    answer = -11111
    digged = [[-1 for _ in range(len(land[0]))] for __ in range(len(land))]
    oils = []
    name = 0
    
    for r in range(len(land)):
        for c in range(len(land[0])):
            if land[r][c] == 0: #확인 필요 없음
                continue
            
            if digged[r][c] != -1: # 이미 확인함
                continue
            
            queue = deque([(r,c)])
            visited = set()
            visited.add((r,c))
            
            while queue:
                pr,pc = queue.popleft()
                    
                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr = pr + dr
                    nc = pc + dc
                    
                    if 0 <= nc < len(land[0]) and 0 <= nr < len(land):
                        if (nr,nc) not in visited and land[nr][nc] == 1:
                            queue.append((nr,nc))
                            visited.add((nr,nc))
            
            oils.append(len(visited))
            for rr,cc in visited:
                digged[rr][cc] = name
            name += 1
        
    for c in range(len(land[0])):
        tmp = 0
        visited = []
        for r in range(len(land)):
            if land[r][c] == 0:
                continue
                    
            if digged[r][c] in visited and digged[r][c] != -1:
                continue
            visited.append(digged[r][c])
            tmp += oils[digged[r][c]]
        answer = max(tmp,answer)
        
    return answer