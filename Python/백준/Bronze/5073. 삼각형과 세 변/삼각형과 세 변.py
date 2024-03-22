import sys
input = sys.stdin.readline
l1,l2,l3 = map(int,input().split())

while l1 and l2 and l3:
    ll = [l1,l2,l3]
    if sum(ll) - max(ll) <= max(ll):
        print("Invalid")
    elif len(set(ll)) == 1:
        print("Equilateral")
    elif len(set(ll)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
    l1,l2,l3 = map(int,input().split())