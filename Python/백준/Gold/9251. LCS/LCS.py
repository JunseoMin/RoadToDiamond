import sys
input = sys.stdin.readline

instr1 = input().strip()
instr2 = input().strip()
N = len(instr1)
M = len(instr2)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if instr1[i - 1] == instr2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[N][M])
