import sys
input = sys.stdin.readline
n = int(input())
attdic = {}
for _ in range(n):
    name,curr = map(str,input().split())
    if curr[0] == 'e':
        curr = 1
    else:
        curr = 0
    attdic[name] = curr
for name in sorted(attdic.keys(),reverse = True):
    if attdic[name]:
        print(name)