from collections import defaultdict,deque

def solution(n, wires):
    answer = 123456789
    
    for i in range(len(wires)):
        removedWires = wires[:i] + wires[i+1:]
        graph = defaultdict(list)
        for s,e in removedWires:
            graph[s].append(e)
            graph[e].append(s)
        for node in range(1, n + 1):
            graph[node] = graph[node]
        visited = set()
        gaps = []
        
        for start in graph.keys():
            if start in visited:
                continue
            
            visited.add(start)
            queue = deque([start])
            count = 0
            
            while queue:
                node = queue.popleft()
                count += 1
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            gaps.append(count)
                
        answer = min(answer,abs(gaps[0] - gaps[1]))
    
    return answer