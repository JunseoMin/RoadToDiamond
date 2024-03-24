n,m = map(int,input().split())
board = [];plist = []
for _ in range(n):
    board.append(input())

for y in range(n-7):
    for x in range(m-7):
        tmp = 0
        tmp1 = 0
        for i in range(y,y+8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    if board[i][x+j] != 'B':
                        tmp += 1
                    if board[i][x+j] != 'W':
                        tmp1 += 1
                else:
                    if board[i][x+j] != 'W':
                        tmp += 1
                    if board[i][x+j] != 'B':
                        tmp1 += 1
        plist.append(tmp)
        plist.append(tmp1)
print(min(plist))
