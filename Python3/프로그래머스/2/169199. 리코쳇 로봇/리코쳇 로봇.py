from collections import deque



def solution(b):
    answer = 0
    R = None
    G = None
    board = [[0 for _ in range(len(b[0]))] for _ in range(len(b))]
    
    for r in range(len(b)):
        for c in range(len(b[0])):
            if b[r][c] == 'R':
                R = (r,c,0)
            elif b[r][c] == 'G':
                G = (r,c)
            elif b[r][c] == 'D':
                board[r][c] = 1
    
    queue = deque([R])
    visited = set()
    visited.add((R[0],R[1]))
    
    while queue:
        r,c,v = queue.popleft()
        
        if (r,c) == G:
            return v
        
        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:   # 방향설정
            nr,nc = r,c
            while 1:
                nr += dr
                nc += dc
                if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]) or board[nr][nc]==1:
                    nr -= dr
                    nc -= dc
                    break
                
            if (nr,nc) not in visited:
                queue.append((nr,nc,v+1))
                visited.add((nr,nc))
                
    print(visited)
    return -1