import sys
input = sys.stdin.readline

_ = input()
nums = list(map(int,input().split()))
operators = list(map(int,input().split()))

def dfs(idx, value, s_operators, max_value, min_value):
    if s_operators == 0:
        max_value[0] = max(max_value[0], value)
        min_value[0] = min(min_value[0], value)
        return
    
    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            if i == 0:
                dfs(idx+1, value + nums[idx+1], s_operators - 1, max_value, min_value)
            elif i == 1:
                dfs(idx+1, value - nums[idx+1], s_operators - 1, max_value, min_value)
            elif i == 2:
                dfs(idx+1, value * nums[idx+1], s_operators - 1, max_value, min_value)
            elif i == 3:
                dfs(idx+1, value // nums[idx+1] if value >= 0 else -(-value // nums[idx+1]), s_operators - 1, max_value, min_value)
            operators[i] += 1

max_value = [-float('inf')]
min_value = [float('inf')]
dfs(0, nums[0], sum(operators), max_value, min_value)

print(max_value[0])
print(min_value[0])
