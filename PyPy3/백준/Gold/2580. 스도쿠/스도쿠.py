import sys
input = sys.stdin.readline
sdoku = [ list(map(int,input().split())) for _ in range(9) ]

def check(x,y):
    ans = [i for i in range(1,10)]
    for n in sdoku[y]:
        if n in ans:
            ans.remove(n)

    for n in range(9):
        if sdoku[n][x] in ans:
            ans.remove(sdoku[n][x])
    
    x = x - (x%3)
    y = y - (y%3)
    for i in range(x,x+3):
        for j in range(y,y+3):
            if sdoku[j][i] in ans:
                ans.remove(sdoku[j][i])
    
    return ans

def dfs(x, y):
    if x == 9:
        x = 0
        y += 1
        if y == 9:
            for i in range(9):
                for j in range(9):
                    print(sdoku[i][j], end=" ")
                print()

            sys.exit()

    if sdoku[y][x] == 0:
        can = check(x, y)
        for n in can:
            sdoku[y][x] = n
            dfs(x + 1, y)
            sdoku[y][x] = 0
    else:
        dfs(x + 1, y)

dfs(0, 0)