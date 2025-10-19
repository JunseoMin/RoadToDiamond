from itertools import permutations as perm

def solution(k, dungeons):
    answer = -1
    paths = perm(dungeons)
    
    for path in paths:
        current = k
        cnt = 0
        for minimum, cost in path:
            if current < minimum:
                break
            current -= cost
            cnt += 1
        answer = max(answer,cnt)
    
    return answer