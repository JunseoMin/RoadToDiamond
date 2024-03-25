import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(int(input()))

nli = []; count = [0] * 10001

for _ in range(n):
    num = int(input())
    count[num]+=1

for num in range(10001):
    if count[num]:
        for j in range(count[num]):
            print(num)