def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    for l in lost[:]:
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)
    
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l-1)
        elif l + 1 in reserve:
            reserve.remove(l+1)
        else:
            n-=1
    
    return n