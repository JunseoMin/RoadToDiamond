from collections import deque

def solution(priorities, location):
    answer = 0
    queue = []
    for i,p in enumerate(priorities):
        if i == location:
            queue.append((p,True))
        else:
            queue.append((p,False))
    queue = deque(queue)
    while queue:
        maxi = max(queue)
        v,k = queue.popleft()
        
        if v != maxi[0]:
            queue.append((v,k))
            continue
        
        if v == maxi[0] and k:
            return answer + 1
        answer += 1
            
            
