import sys
input = sys.stdin.readline

N = int(input())
chongdancer = set()
chongdancer.add("ChongChong")

for _ in range(N):
    a,b = map(str,input().split())
    if (a in chongdancer) or (b in chongdancer):
        chongdancer.add(a)
        chongdancer.add(b)
        
print(len(chongdancer))