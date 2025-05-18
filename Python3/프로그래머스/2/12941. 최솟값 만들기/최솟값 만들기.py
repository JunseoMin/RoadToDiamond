import heapq

def solution(A,B):
    answer = 0
    N = len(A)
    
    heapq.heapify(A)
    newB = []
    for b in B:
        newB.append(-b)
    
    heapq.heapify(newB)
    
    for i in range(N):
        answer += heapq.heappop(A) * heapq.heappop(newB) * -1
            
    
    return answer