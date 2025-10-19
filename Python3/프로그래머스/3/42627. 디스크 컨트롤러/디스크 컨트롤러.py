import heapq

def solution(jobs):
    answer = 0
    
    N = len(jobs)
    curr = 0
    finished = 0   # 처리한 작업 수
    queue = []
    visited = [False for _ in range(N)]
    
    while finished < N:
        for i,(s,l) in enumerate(jobs):
            if s <= curr and not visited[i]:
                heapq.heappush(queue,(l,s))
                visited[i] = True
        
        if queue:
            l,s = heapq.heappop(queue)
            curr += l
            finished += 1
            answer += (curr - s)
        else:
            curr = min([s for i, (s, l) in enumerate(jobs) if not visited[i]])

    
    return answer // N