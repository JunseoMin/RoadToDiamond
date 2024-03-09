import sys

input = sys.stdin.readline

alist = []

for _ in range(10):
    n = int(input())
    if not (n % 42 in alist):
        alist.append(n%42)
print(len(alist))