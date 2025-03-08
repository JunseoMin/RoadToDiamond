def solution(n, number):
    answer = 0
    
    if n == number:
        return 1
    
    dp = [[],[n]]
    for step in range(2,9):
        new = []
        new.append(dp[step - 1][0] * 10 + n)
        
        for i in range(step):
            j = step - i
            for val in dp[i]:
                for val2 in dp[j]:
                    new.append(val + val2)
                    new.append(val - val2)
                    new.append(val2 - val)
                    new.append(val * val2)
                    try:
                        new.append(val // val2)
                        new.append(val2 // val)
                    except:
                        pass
        new.append(int(f"{n}" * step))
        new = list(set(new))
        if number in new:
            return step 
        dp.append(new)
    
    return -1