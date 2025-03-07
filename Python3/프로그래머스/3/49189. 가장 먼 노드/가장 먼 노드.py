from collections import deque, defaultdict

def explore(start,graph,visited):
    queue = deque([(start,0)])
    visited = set([start])
    distances = [0]
    
    while queue:
        v,d = queue.popleft()
        
        for nextv in graph[v]:
            if nextv not in visited:
                queue.append((nextv,d+1))
                distances.append(d+1)
                visited.add(nextv)
        
    return distances
        

def solution(n, edges):
    answer = 0
    graph = {i:[] for i in range(1,n+1)}
    
    for v1,v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    answers = explore(1,graph,[])
    maxi = max(answers)
    
    return answers.count(maxi)