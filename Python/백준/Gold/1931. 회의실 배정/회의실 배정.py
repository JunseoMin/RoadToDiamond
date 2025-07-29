import sys
input = sys.stdin.readline

N = int(input())
times = []
curr = 0
answer = 0

for _ in range(N):
    times.append(list(map(int,input().split())))
    
times.sort(key = lambda x:(x[1], x[0]))

for b,e in times:
    if b >= curr:
        answer += 1
        curr = e
        
print(answer)