import sys
input = sys.stdin.readline

from collections import deque

stack = []
N = int(input())
stack = deque(stack)

for _ in range(N):
    inp = input().strip()
    if len(inp) > 1:
        _,n = map(int,inp.split())
        stack.append(n)
        
    else:
        c = int(inp)
        if c == 2:
            try:
                print(stack.pop())
            except:
                print('-1')

        if c == 3:
            print(len(stack))

        if c == 4:
            if len(stack):
                print(0)
            else:
                print(1)

        if c == 5:
            try:
                print(stack[-1])
            except:
                print(-1)