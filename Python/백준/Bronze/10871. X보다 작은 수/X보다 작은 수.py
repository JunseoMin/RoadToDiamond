import sys

input = sys.stdin.readline

ans = ""
n,x = map(int,input().split())
n_list = list(map(int,input().split()))

for i in range(n):
    if n_list[i]<x:
        ans+= (str(n_list[i]) + " ")
        

print(ans[:-1])