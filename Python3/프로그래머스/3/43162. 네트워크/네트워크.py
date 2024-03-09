def solution(n, computers):
    visited = [False for _ in range(n)]
    ans = 0

    def DFS(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] and not visited[j]:
                DFS(j)
            
    for i in range(n):
        if not visited[i]:
            DFS(i)
            ans+=1
                
    return ans