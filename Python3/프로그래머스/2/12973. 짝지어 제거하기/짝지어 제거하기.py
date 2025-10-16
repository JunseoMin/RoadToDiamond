def solution(s):
    stack = []
    
    for c in s:
        stack.append(c)
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    return 0 if len(stack) else 1