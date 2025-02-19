
def solution(priorities, location):
    ans = 1
    cp = priorities[:]
    cp[location] += 10
    
    while (len(priorities)):
        if max(priorities) == cp[0]%10:
            if cp[0]>10:
                return ans
            
            priorities.pop(0)
            cp.pop(0)
            ans += 1
        else:
            priorities.append(priorities[0])
            priorities.pop(0)
            cp.append(cp[0])
            cp.pop(0)
                
    return -1