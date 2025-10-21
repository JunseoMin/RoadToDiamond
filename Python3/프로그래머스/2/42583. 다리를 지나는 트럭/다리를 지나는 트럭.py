from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    cars = 0
    totalBridge = 0
    
    while queue:
        out = bridge.popleft()
        if out != 0:
            cars -= 1
        totalBridge -= out
        
        waiting = queue[0]
        
        if cars < bridge_length and totalBridge + waiting <= weight:
            wait = queue.popleft()
            bridge.append(wait)
            
            cars += 1
            totalBridge += wait
        else:
            bridge.append(0)
        
        answer += 1
    return answer + len(bridge)