import sys

input = sys.stdin.readline

instr = input().strip()
N = int(input())

for _ in range(N):
    a,l,r =map(str,input().split())
    l = int(l)
    r = int(r)

    print(instr[l:r+1].count(a))