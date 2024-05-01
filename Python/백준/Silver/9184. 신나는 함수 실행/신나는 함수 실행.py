import sys

input = sys.stdin.readline
wdic = {}

def w(a,b,c):
    if (a,b,c) in wdic:
        return wdic[(a,b,c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    
    if a < b and b < c:
        wdic[(a,b,c)] = w(a,b,c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return wdic[(a,b,c)]
    
    wdic[(a,b,c)] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return wdic[(a,b,c)]

inint = list(map(int,input().split()))

# print(w(inint[0],inint[1],inint[2]))
# print(wdic)

while inint != [-1,-1,-1]:
    print('w({}, {}, {}) = '.format(inint[0],inint[1],inint[2]) + str(w(inint[0],inint[1],inint[2])))
    inint = list(map(int,input().split()))
