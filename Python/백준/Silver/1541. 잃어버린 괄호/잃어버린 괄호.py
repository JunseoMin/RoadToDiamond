import sys
input = sys.stdin.readline

def calcStrEq(strEq):
    res = 0
    eq = strEq.split('+')
    for v in eq:
        res += int(v)
    return res

eq = input().strip().split('-')
answer = 0
answer += calcStrEq(eq[0])

if len(eq) == 1:
    print(answer)
    sys.exit()

for strEq in eq[1:]:
    answer -= calcStrEq(strEq)

print(answer)