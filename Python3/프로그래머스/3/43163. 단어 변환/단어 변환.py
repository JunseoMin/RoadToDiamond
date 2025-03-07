from collections import deque

def isDiffOne(w1,w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
            
    return True if cnt == 1 else False

def solution(begin, target, words):
    answer = 0
    queue = deque([(begin,0)])
    visited = set([begin])
    
    while queue:
        word, d = queue.popleft()
        
        if word == target:
            return d
        
        for nextw in words:
            if nextw in visited:
                continue
            
            if isDiffOne(word,nextw):
                queue.append((nextw,d+1))
                visited.add(nextw)
    return 0