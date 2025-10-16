def check(gstr):
    stack = []
    for g in gstr:
        if g == '(':
            stack.append(g)
        else:
            if len(stack) <= 0:
                return False
            stack.pop()
    return True

def shift(ustr):
    res = ""
    for g in ustr:
        if g == '(':
            res += ')'
        else:
            res += '('
    return res

def solution(p):
    if p == '':
        return p
    stack = []
    u = p[0]
    v = ''
    cnt = 1
    for ch in p[1:]:
        if ch != p[0]:
            u += ch
            cnt -= 1
        else:
            u += ch
            cnt += 1
        
        if cnt == 0:
            v = p[len(u):]
            break
    
    if check(u):
        return u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        u = u[1:len(u)-1]
        answer += shift(u)
        return answer
