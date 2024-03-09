import sys

input = sys.stdin.readline

n,m = map(int,input().split())
buckets = [i for i in range(1,n+1)]


for _ in range(m):
    tmp = []
    i,j = map(int,input().split())
    tmp = buckets[i-1:j]
    tmp.reverse()
    buckets[i-1:j] = tmp

print(" ".join(str(n) for n in buckets))