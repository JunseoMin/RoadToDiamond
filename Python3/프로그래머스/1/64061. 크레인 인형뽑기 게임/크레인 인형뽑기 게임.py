def solution(board, moves):
    answer = 0
    stack = []
    rows = len(board)
    
    for m in moves:
        col = m - 1
        for r in range(rows):
            if board[r][col] != 0:
                stack.append(board[r][col])
                board[r][col] = 0
                break
                
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer