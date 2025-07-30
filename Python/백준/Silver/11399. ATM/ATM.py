import sys
input = sys.stdin.readline

input()

times = sorted(map(int,input().split()))
answer = 0

for i in range(len(times)):
    answer += sum(times[:i+1])

print(answer)
