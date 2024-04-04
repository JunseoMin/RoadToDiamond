import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    gstack = deque()
    gwalho = input().strip()
    flag = True
    for g in gwalho:
        if g == '(':
            gstack.append(1)
        else:
            try:
                gstack.pop()
            except:
                print("NO")
                flag = False
                break
    
    if len(gstack):
        flag = False
        print("NO")

    if flag:
        print("YES")
    