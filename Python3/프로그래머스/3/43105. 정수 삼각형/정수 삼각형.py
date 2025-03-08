def solution(triangle):
    answer = 0
    
    dp = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
    
    dp[0] = triangle[0]
    
    for step in range(1,len(triangle)):
        for i in range(len(triangle[step])):
            if i == 0:
                dp[step][i] = dp[step - 1][0] + triangle[step][i]
            if i >= 1 and i < len(triangle[step]) - 1:
                dp[step][i] = max(dp[step - 1][i -1], dp[step - 1][i]) + triangle[step][i]
            if i == (len(triangle[step]) - 1):
                dp[step][i] = dp[step - 1][-1] + triangle[step][i]
    
    return max(dp[-1])