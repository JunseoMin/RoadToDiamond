import sys
input = sys.stdin.readline
tmp = 0.0
stmp = 0.0
for _ in range(20):
    _,score,point = map(str,input().split())
    score = float(score)
    
    if point == 'A+':
        point = 4.5
    if point == 'A0':
        point = 4.0
    if point == 'B+':
        point = 3.5
    if point == 'B0':
        point = 3.0
    if point == 'C+':
        point = 2.5
    if point == 'C0':
        point = 2.0
    if point == 'D+':
        point = 1.5
    if point == 'D0':
        point = 1.0
    if point == 'F':
        point = 0.0
    if point  == 'P':
        continue
    stmp += score
    tmp += (score * point)

print(tmp/stmp)