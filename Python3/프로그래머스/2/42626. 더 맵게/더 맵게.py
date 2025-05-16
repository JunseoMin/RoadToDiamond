import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return 0
    
    while len(scoville) >= 2:
        small1 = heapq.heappop(scoville)
        small2 = heapq.heappop(scoville)
        
        new = small1 + small2 * 2
        
        heapq.heappush(scoville , new)
        
        answer += 1
        
        if scoville[0] >= K:
            return answer
    return -1