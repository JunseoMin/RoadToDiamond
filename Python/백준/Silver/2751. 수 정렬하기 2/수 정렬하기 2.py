import heapq,sys
input = sys.stdin.readline
n = int(input())
nheap = []

for i in range(n):
    nheap.append(int(input()))
    
for nn in sorted(nheap):
    print(nn)