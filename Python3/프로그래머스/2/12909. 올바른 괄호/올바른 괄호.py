def solution(s):
    answer = True
    
    left = 0
    
    for v in s:
        if v == '(':
            left += 1
        if v == ')':
            left -= 1
        
        if left < 0:
            return False

    return not(left)