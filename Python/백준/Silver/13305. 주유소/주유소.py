import sys

input = sys.stdin.readline

N = int(input())
lengths = list(map(int,input().split()))
costs = list(map(int,input().split()))

answer = 0
pos = 0

while (pos < N-1):
    currCost = costs[pos]
    distance = lengths[pos]
    
    for i in range(pos+1,N-1):
        if currCost <= costs[i]:
            distance += lengths[i]
            pos += 1
        else:
            break
    answer += currCost * distance
    pos += 1

print(answer)