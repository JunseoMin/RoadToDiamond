def dfs():
    return

def solution(numbers, target):
    stack = [(0,0)]
    ans = 0
    
    while stack:
        curr, idx = stack.pop()
        
        if idx == len(numbers):
            if curr == target:
                ans += 1
        else:
            stack.append((curr - numbers[idx],idx+1))
            stack.append((curr + numbers[idx],idx+1))
    
    return ans