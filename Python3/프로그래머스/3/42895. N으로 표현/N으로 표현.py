def solution(n, number):
    answer = 0
    if n == number:
        return 1
    
    answers = [[],[n]]
    
    for step in range(2,9):
        new = []
        
        for i in range(step):
            for v1 in answers[i]:
                for v2 in answers[step - i]:
                    new.append(v1 + v2)
                    new.append(v1 - v2)
                    new.append(v2 - v1)
                    new.append(v1 * v2)
                    try:
                        new.append(v1 // v2)
                        new.append(v2 // v1)
                    except:
                        pass
            
        new.append(int(f"{n}"*step))
        if number in new:
            return step
        
        answers.append(list(set(new)))
        
        
    
    return -1