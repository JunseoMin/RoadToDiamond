from collections import deque,defaultdict


def solution(n, results):
    answer = 0
    wingraph  = defaultdict(list)
    losegraph = defaultdict(list)
    
    for win,lose in results:
        wingraph[win].append(lose)
        losegraph[lose].append(win)
    
    for i in range(1,n+1):
        Wqueue = deque([i])
        Lqueue = deque([i])
        winvisited = set()
        losevisited = set()
        
        while Wqueue:
            curr = Wqueue.popleft()
            if curr in winvisited:
                continue
            winvisited.add(curr)
            
            for neighbor in wingraph[curr]:
                if neighbor not in winvisited:
                    Wqueue.append(neighbor)
    
        while Lqueue:
            curr = Lqueue.popleft()
            if curr in losevisited:
                continue
            losevisited.add(curr)
            
            for neighbor in losegraph[curr]:
                if neighbor not in losevisited:
                    Lqueue.append(neighbor)
                    
        if len(winvisited.union(losevisited)) == n:
            answer += 1
    return answer

'''
4
3   1 
2
5'''