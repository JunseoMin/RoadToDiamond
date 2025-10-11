def solution(sequence, k):
    l = 0
    total = 0
    answer = [float('inf'), -1, -1]
    
    for r in range(len(sequence)):
        total += sequence[r]
        
        while total > k:
            total -= sequence[l]
            l += 1
        
        if total == k:
            if r - l < answer[0]:
                answer = [r - l, l, r]
    
    return answer[1:]
