import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    val = 0
    
    while scoville[0] < K and len(scoville) >= 2:
        v1 = heapq.heappop(scoville)
        v2 = heapq.heappop(scoville)
        new = v1 + 2* v2
        heapq.heappush(scoville,new)
        answer += 1
    
    return answer if scoville[0] >= K else -1