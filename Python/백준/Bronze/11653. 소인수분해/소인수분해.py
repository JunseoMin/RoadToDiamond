import sys

n = int(input())
tmp = 0
if n == 1:
    sys.exit()


i = 2
while n>=i:
    if not n%i:
        print(i)
        # print(n)
        n = n//i
        i = 2
        continue

    i+=1