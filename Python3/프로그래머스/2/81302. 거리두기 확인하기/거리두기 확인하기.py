from collections import deque

def solution(places):
    answer = []
    
    for place in places:
        queue = []
        flag = True
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P' and flag:
                    visited = set()
                    visited.add((r,c))
                    queue = deque([(r,c,0)])
                    
                    while queue:
                        r,c,v = queue.popleft()

                        if place[r][c] == 'P' and 0 < v <= 2:
                            answer.append(0)
                            flag = False
                            break
            
            
                        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nr = r + dr
                            nc = c + dc
                
                            if 0<=nr<5 and 0<=nc<5:
                                if place[nr][nc] != 'X' and (nr,nc) not in visited:
                                    visited.add((nr,nc))
                                    queue.append((nr,nc,v+1))
            
        if flag:
            answer.append(1)
    return answer