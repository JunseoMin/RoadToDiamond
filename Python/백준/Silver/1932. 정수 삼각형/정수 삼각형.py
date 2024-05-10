import sys
input = sys.stdin.readline

N = int(input())
tri = []

for _ in range(N):
    tri.append(list(map(int,input().split())))

dp_dic = {}

def dp(depth,idx):
    if depth == N-1:
        return tri[depth][idx]

    if (depth,idx) in dp_dic:
        return dp_dic[(depth,idx)]
    
    dp_dic[(depth,idx)] = tri[depth][idx] + max(dp(depth+1,idx),dp(depth+1,idx+1))
    return dp_dic[(depth,idx)]

print(dp(0,0))