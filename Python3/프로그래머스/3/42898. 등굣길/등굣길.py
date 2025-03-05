def solution(m, n, puddles):
    answer = 0
    
    map = [[[True ,0] for _ in range(m)] for _ in range(n)]
    
    for x,y in puddles:
        map[y-1][x-1][0] = False
    
    map[0][0][1] = 1
    
    for x in range(m):
        for y in range(n):
            if not map[y][x][0]:
                continue
            
            if x+1 < m and map[y][x+1][0]:
                map[y][x+1][1] += map[y][x][1]
            if y+1 < n and map[y+1][x][0]:
                map[y+1][x][1] += map[y][x][1]
                
    return map[-1][-1][1] % 1000000007