import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

stack = deque([i for i in range(1,N+1)])

for _ in range(N-1):
    stack.popleft()
    stack.append(stack.popleft())

print(stack.pop())