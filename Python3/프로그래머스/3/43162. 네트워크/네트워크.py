def solution(n, computers):
    answer = 0
    visited = set()
    graph = {i : computers[i] for i in range(len(computers))}
    
    for i in range(n):
        if i in visited:
            continue
            
        stack = [i]
        
        while stack:
            node = stack.pop()
            visited.add(node)
            
            for i in range(len(graph[node])):
                isNeighbor = graph[node][i]
                if isNeighbor and not(i in visited):
                    stack.append(i)
        answer += 1
        
    return answer