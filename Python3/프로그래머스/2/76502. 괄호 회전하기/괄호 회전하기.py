def solution(s):
    answer = 0
    ss = []
    N = len(s)
    
    for i in range(N):
        op = []
        for j in range(N):
            op.append(s[(i + j)%N])
        ss.append(op)
        
    for op in ss:
        stack = []
        flag = True
        for v in op:
            if v in "({[":
                stack.append(v)
            else:
                if not stack:
                    flag = False
                    break
                v2 = stack.pop()
                if v == ')' and v2 != '(':
                    flag = False
                    break
                if v == '}' and v2 != '{':
                    flag = False
                    break
                if v == ']' and v2 != '[':
                    flag = False
                    break
        if flag and len(stack) == 0:
            answer += 1
            
    return answer