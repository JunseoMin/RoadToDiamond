import sys
input = sys.stdin.readline
n = int(input())
xn = None;yn = None;xm = None;ym = None
if n == 1:
    print(0)
    sys.exit()

xn, yn = map(int,input().split())
xm = xn;ym = yn
for _ in range(n-1):
    x, y = map(int,input().split())
    if xn > x:
        xn = x
    if yn > y:
        yn = y
    if xm < x:
        xm = x
    if ym < y:
        ym = y
        
    
print((xm - xn)*(ym - yn))