from collections import deque

def solution(order):
    answer = 0
    belt = [i for i in range(1,len(order) + 1)]
    sub = []
    queue = deque(belt)
    i = 0
    
    while queue:
        v = queue.popleft()
        if v != order[i]:
            sub.append(v)
        elif v == order[i]:
            answer += 1
            i += 1
        
        while len(sub) and sub[-1] == order[i]:
            sub.pop()
            i+=1
            answer += 1
            
    return answer