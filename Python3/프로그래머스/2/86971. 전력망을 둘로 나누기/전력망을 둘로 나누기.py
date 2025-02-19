def num_connections(node,tree,visited = []):
    if node in visited:
        return 0
    cnt = 1
    visited.append(node)
    for nd in tree[node]:
        cnt += num_connections(nd, tree, visited)
    
    return cnt


def solution(n, wires):
    answer = 200
    
    for i in range(n):
        tmp = wires[:i] + wires[i+1:]
        tree = {i: [] for i in range(1, n + 1)}
        
        for v1,v2 in tmp:
            tree[v1].append(v2)
            tree[v2].append(v1)
        
        answer = min(answer, abs(2*num_connections(1, tree, []) - n))
        
    return answer