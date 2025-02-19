def solution(brown, yellow):
    answer = []
    maxgaro = int(brown / 2)
    
    for garo in range(maxgaro,0,-1):
        sero = (brown - garo * 2) / 2
        if (garo - 2) * int(sero) == yellow:
            return [garo,sero+2]
    
    return "answer"