from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = set()
    queue = deque([(begin,0)])
    wL = len(words[0])
    
    while queue:
        curr,cost = queue.popleft()
        if (curr) in visited:
            continue
        visited.add(tuple(curr))
        
        if curr == target:
            return cost
        
        for word in words:
            cnt = 0
            for i in range(wL):
                if word[i] != curr[i]:
                    cnt += 1
            if cnt == 1 and tuple(word) not in visited:
                queue.append((word, cost + 1))
    
    return 0