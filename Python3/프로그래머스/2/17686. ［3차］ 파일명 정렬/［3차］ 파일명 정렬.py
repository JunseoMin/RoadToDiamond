import heapq
from collections import defaultdict

def solution(files):
    answer = []
    numbers = "0123456789"
    names = []
    tags = defaultdict(int)
    
    for idx, file in enumerate(files): 
        HEAD = ""
        NUMBER = ""
        TAIL = ""
        
        j = 0
        for i in range(len(file)):
            if file[i] in numbers:
                j = i
                break
            HEAD += file[i]
        
        for i in range(j, len(file)):
            if file[i] not in numbers:
                j = i
                break
            NUMBER += file[i]
        else:
            j = len(file)
        
        TAIL = file[j:]
        tag = HEAD.lower() + NUMBER
        tags[tag] += 1
        
        heapq.heappush(names, (HEAD.lower(), int(NUMBER), idx, HEAD, NUMBER, TAIL))
    
    while names:
        _, _, _, HEAD, NUMBER, TAIL = heapq.heappop(names)
        answer.append(HEAD + NUMBER + TAIL)
    
    return answer
