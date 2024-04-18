N = int(input())
ans = 0

row = [0]*N

def can_Q(col):
    for r in range(col):
        if row[col] == row[r] or abs(row[col] - row[r]) == abs(col - r):
            return False
    return True

def dfs(col):
    global ans
    if col == N:
        ans += 1
        return

    for r in range(N):
        row[col] = r

        if can_Q(col):
            dfs(col+1)

dfs(0)
print(ans)
