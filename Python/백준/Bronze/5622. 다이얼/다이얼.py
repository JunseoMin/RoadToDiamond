import sys

ans = 0
input = sys.stdin.readline
instr = input()

for c in instr:
    if c in 'ABC':
        ans += 3
    if c in 'DEF':
        ans += 4
    if c in 'GHI':
        ans += 5
    if c in 'JKL':
        ans += 6
    if c in 'MNO':
        ans += 7
    if c in 'PQRS':
        ans += 8
    if c in 'TUV':
        ans += 9
    if c in 'WXYZ':
        ans += 10
        
print(ans)