import sys
input = sys.stdin.readline
N = int(input())
tmp = []
log = set()

for _ in range(N):
    inst = input().strip()
    if inst == 'ENTER':
        tmp.append(len(log))
        log = set()
    else:
        log.add(inst)
tmp.append(len(log))
print(sum(tmp))