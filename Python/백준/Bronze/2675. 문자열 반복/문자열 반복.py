import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    ans = ""
    m , instr = map(str, input().split())
    m = int(m)

    for s in instr:
        ans += s*m
        
    print(ans)