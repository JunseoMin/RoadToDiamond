from collections import deque

def solution(numbers, target):
    answer = 0
    
    queue = deque(numbers)
    prevs = [0]
    while queue:
        n = queue.popleft()
        
        tmp = []
        for prev in prevs:
            tmp.append(prev + n)
            tmp.append(prev - n)
        prevs = tmp
        
    for v in prevs:
        if v == target:
            answer += 1
    
    return answer