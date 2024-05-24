import sys

input = sys.stdin.readline

instr = input().strip()
N = int(input())
S = len(instr)
sumdic = {}

for a in range(ord('a'),ord('z')+1):
    c_a = chr(a)
    sumdic[c_a] = [0] * S
    sumdic[c_a][0] = 1 if instr[0] == c_a else 0

    for i in range(1,S):
        if instr[i] == c_a:
            sumdic[c_a][i] = sumdic[c_a][i-1] + 1
        else:
            sumdic[c_a][i] = sumdic[c_a][i-1]


for _ in range(N):
    a,l,r =map(str,input().split())
    l = int(l)
    r = int(r)

    if l == 0:
        print(sumdic[a][r])
        continue

    print(sumdic[a][r]-sumdic[a][l-1])