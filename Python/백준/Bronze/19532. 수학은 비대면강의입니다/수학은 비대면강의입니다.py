import sys
a,b,c,d,e,f = map(int,input().split())

for x in range(-1000,1000):
    for y in range(-1000,1000):
        if not (a * x + b * y  - c ) and not (d * x + e * y  - f):
            print(str(x)+" "+str(y))
            sys.exit()