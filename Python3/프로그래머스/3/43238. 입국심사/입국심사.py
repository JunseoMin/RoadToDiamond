def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        total = sum(mid // time for time in times)
        
        if total >= n:
            right = mid
        else:
            left = mid + 1
    
    
    return left