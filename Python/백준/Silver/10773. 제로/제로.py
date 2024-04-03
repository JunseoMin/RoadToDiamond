from collections import deque
import sys

input = sys.stdin.readline

N= int(input())
stack = deque()

for _ in range(N):
    n = int(input())
    if n:
        stack.append(n)
    else:
        stack.pop()
        
print(sum(stack))