import heapq as hq

def solution(n, k, enemy):
    answer = 0
    queue = []
    i = 0
    N = len(enemy)
    
    if k >= N:
        return N
    
    for i in range(len(enemy)):
        e = enemy[i]
        hq.heappush(queue,-e)
        n -= e
        
        if n < 0:
            if k > 0:
                n += -hq.heappop(queue)
                k -= 1
            else:
                return i
    
    return N