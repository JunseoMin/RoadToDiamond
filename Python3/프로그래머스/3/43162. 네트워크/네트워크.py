from collections import deque

def solution(n, computers):
    answer = n
    graph = {}
    
    for i in range(n):
        tmp = []
        for idx,v in enumerate(computers[i]):
            if v == 1 and idx != i:
                tmp.append(idx)
        graph[i] = tmp 
    
    visited = set()
    print(graph)
    
    for i in range(n):
        queue = deque([i])
        visited.add(i)
        cnt = 0
        while queue:
            curr = queue.popleft()
            
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    cnt += 1
        
        answer -= cnt
    
    return answer