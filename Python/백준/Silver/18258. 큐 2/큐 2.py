import sys
from collections import deque
input = sys.stdin.readline
'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
N = int(input())

stack = deque()

for _ in range(N):
    instr = input().strip()
    if instr == "pop":
        try:
            print(stack.popleft())
        except:
            print("-1")
    elif instr == "size":
        print(len(stack))
    elif instr == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif instr == "front":
        try:
            print(stack[0])
        except:
            print('-1')
    elif instr == "back":
        try:
            print(stack[-1])
        except:
            print('-1')
    else:
        instr, n = map(str,instr.split())
        n = int(n)
        stack.append(n)