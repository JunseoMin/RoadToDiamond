def solution(rows, columns, queries):
    answer = []
    board = [[ r*columns + c + 1 for c in range(columns)] for r in range(rows)]
    tmp = [[ 0 for _ in range(columns)] for __ in range(rows)]
    for x1,y1,x2,y2 in queries:
        val = 1000000
        indices = set()
        r1 = x1 - 1
        c1 = y1 - 1
        r2 = x2 - 1
        c2 = y2 - 1

        rDns = [(rr,c1) for rr in range(r1+1,r2+1)]
        cUps = [(r1,cc) for cc in range(c1,c2)]
        rUps = [(rr,c2) for rr in range(r1,r2)]
        cDns = [(r2,cc) for cc in range(c1+1,c2+1)]
        
        for r,c in rDns:
            tmp[r-1][c] = board[r][c]
            val = min(board[r][c],val)
            indices.add((r,c))
        for r,c in rUps:
            tmp[r+1][c] = board[r][c]
            val = min(board[r][c],val)
            indices.add((r,c))
        for r,c in cUps:
            tmp[r][c+1] = board[r][c]
            val = min(board[r][c],val)
            indices.add((r,c))
        for r,c in cDns:
            tmp[r][c-1] = board[r][c]
            val = min(board[r][c],val)
            indices.add((r,c))
            
        for r,c in indices:
            board[r][c] = tmp[r][c]
        answer.append(val)
        
    return answer