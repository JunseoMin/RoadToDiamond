import sys
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    inst = input().strip()
    tmp = 1 
    sum_ = 0
    flag = False
    for c in inst:
        if c == 'O':
            sum_ += tmp
            tmp += 1
        if c == 'X':
            tmp = 1
    print(sum_)