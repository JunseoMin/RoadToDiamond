import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
K = int(input())
orders = []

board = [[0 for _ in range(N)] for __ in range(N)]

for _ in range(K):
    r,c = map(int,input().split())
    board[r-1][c-1] = 1
    
L = int(input())

for _ in range(L):
    t,A = input().split()
    orders.append((int(t),A))

time = 0
direction = (0,1)
head = (0,0)
body = deque([(0,0)])
while 1:
    # 1. 몸길이를 늘려 머리를 다음 칸으로 이동
    pr,pc = head
    dr,dc = direction
    r,c = pr+dr,pc+dc
    head = (r,c) #다음칸
    
    if r >= N or r < 0:
        break
    if c >= N or c < 0:
        break        
    if head in body:
        break
    body.append(head) #몸길이 늘림
    
    if board[r][c] == 1:
        board[r][c] = 0
    else:
        body.popleft()
    time+=1
    # ---- X초가 끝남
    if len(orders) and time == orders[0][0]:
        _,A = orders.pop(0)
        if A == 'L':
            if direction == (0,1):
                direction = (-1,0)
            elif direction == (-1,0):
                direction = (0,-1)
            elif direction == (0,-1):
                direction = (1,0)
            elif direction == (1,0):
                direction = (0,1)
        else:
            if direction == (0,1):
                direction = (1,0)
            elif direction == (1,0):
                direction = (0,-1)
            elif direction == (0,-1):
                direction = (-1,0)
            elif direction == (-1,0):
                direction = (0,1)
print(time+1)