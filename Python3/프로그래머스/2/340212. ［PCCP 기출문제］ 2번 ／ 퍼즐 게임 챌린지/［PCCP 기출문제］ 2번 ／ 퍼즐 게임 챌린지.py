def solution(diffs, times, limit):
    N = len(diffs)
    start = 1
    end = max(diffs)
    cost = limit + 1
    
    while start <= end:
        level = (start + end) // 2
        cost = 0
        time_prev = 0
        
        for i in range(N):
            diff = diffs[i]
            time_curr = times[i]
            
            if diff > level:
                reN = diff - level
                cost += (reN + 1) * time_curr
                cost += reN * time_prev
            else:
                cost += time_curr
            
            if cost > limit:
                break
                
            time_prev = time_curr
        if cost <= limit:
            end = level - 1
        else:
            start = level + 1

    return start