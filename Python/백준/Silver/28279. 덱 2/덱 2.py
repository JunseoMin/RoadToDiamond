'''
1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
5: 덱에 들어있는 정수의 개수를 출력한다.
6: 덱이 비어있으면 1, 아니면 0을 출력한다.
7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
'''

import sys
from collections import deque


input = sys.stdin.readline
N = int(input())

deq = deque()

for _ in range(N):
    nst = input().strip()

    if len(nst) > 1:
        option, n = map(int,nst.split())
    else:
        option = int(nst)

    if option == 1:
        deq.appendleft(n)
    elif option == 2:
        deq.append(n)
    elif option == 3:
        try:
            print(deq.popleft())
        except:
            print('-1')
    elif option == 4:
        try:
            print(deq.pop())
        except:
            print('-1')
    elif option == 5:
        print(len(deq))
    elif option == 6:
        if len(deq):
            print(0)
        else:
            print(1)
    elif option == 7:
        if len(deq):
            print(deq[0])
        else:
            print('-1')
    elif option == 8:
        if len(deq):
            print(deq[-1])
        else:
            print('-1')