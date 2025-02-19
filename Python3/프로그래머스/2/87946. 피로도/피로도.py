import itertools

def solution(k, dungeons):
    answer = -1
    
    paths = itertools.permutations(dungeons)
    for path in paths:
        full = k
        passed = 0
        for mintired, cost in path:
            if mintired <= full and full - cost >= 0:
                full = full - cost
                passed += 1
        answer = max(answer,passed)
    
    return answer