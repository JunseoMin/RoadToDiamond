import sys
input = sys.stdin.readline

rows,cols,k = map(int,input().split())

Wprefix = [[0] * cols for __ in range(rows)] # Contains Acc sum
Bprefix = [[0] * cols for __ in range(rows)] # Contains Acc sum

answer = float('inf')
Wboard = [[0] * cols for __ in range(rows)]
Bboard = [[0] * cols for __ in range(rows)]
board = [list(input().strip()) for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        if row % 2:    #odd row
            if col % 2:    # odd col
                Wboard[row][col] = 0 if board[row][col] == 'W' else 1   # Should be white
                Bboard[row][col] = 1 if board[row][col] == 'W' else 0   # Should be black
            else:
                Wboard[row][col] = 1 if board[row][col] == 'W' else 0   # Should be white
                Bboard[row][col] = 0 if board[row][col] == 'W' else 1   # Should be black
        else:
            if col % 2:    # odd col
                Wboard[row][col] = 1 if board[row][col] == 'W' else 0   # Should be black
                Bboard[row][col] = 0 if board[row][col] == 'W' else 1   # Should be white
            else:
                Wboard[row][col] = 0 if board[row][col] == 'W' else 1   # Should be black
                Bboard[row][col] = 1 if board[row][col] == 'W' else 0   # Should be white

#Sum of [0,0] 2 [row,col]
for i in range(rows):
    for j in range(cols):       
        # (0,0) == White
        Wprefix[i][j] = Wboard[i][j] 
        Bprefix[i][j] = Bboard[i][j] 
        if i > 0 : 
            Wprefix[i][j] += Wprefix[i - 1][j]
            Bprefix[i][j] += Bprefix[i - 1][j]
        if j > 0 : 
            Wprefix[i][j] += Wprefix[i][j - 1] 
            Bprefix[i][j] += Bprefix[i][j - 1] 
        if i > 0 and j > 0 : 
            Wprefix[i][j] -= Wprefix[i - 1][j - 1]
            Bprefix[i][j] -= Bprefix[i - 1][j - 1]
        
for i in range(k-1, rows):
    for j in range(k-1, cols):
        Wans = Wprefix[i][j]
        Bans = Bprefix[i][j]
        
        if i >= k:
            Wans -= Wprefix[i-k][j]
            Bans -= Bprefix[i-k][j]
        if j >= k:
            Wans -= Wprefix[i][j-k]
            Bans -= Bprefix[i][j-k]
        if j>=k and i>=k:
            Wans += Wprefix[i - k][j - k]
            Bans += Bprefix[i - k][j - k]
        
        answer = min(Wans, Bans, answer)
    
print(answer)