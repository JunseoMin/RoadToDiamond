import sys
input = sys.stdin.readline

n = int(input())

tmp = 0
numstr = str(input())[:-1]
for m in numstr:
    tmp += int(m)

print(tmp)
        