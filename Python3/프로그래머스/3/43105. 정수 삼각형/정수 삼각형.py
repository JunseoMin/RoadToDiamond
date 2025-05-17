def solution(triangle):
    answer = 0
    dp = [[[] for _ in range(len(triangle[rank]))] for rank in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j < 1:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
                continue
            if j > len(triangle[i-1]) - 1:
                dp[i][j] = dp[i-1][-1] + triangle[i][j]
                continue
                
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
            
    return max(dp[-1])