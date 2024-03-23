import sys
a1,a2 = map(int,input().split())
c = int(input())
n0 = int(input())

if c>=a1 and (c-a1)*n0 >= a2 :
    print(1)
else:
    print(0)