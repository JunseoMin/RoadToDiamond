import sys

input = sys.stdin.readline
r = c = 0
mmax = -1

for i in range(9):
    nmat = list(map(int,input().split()))
    for j in range(9):
        if nmat[j] > mmax:
            mmax = nmat[j]
            r = i + 1
            c = j + 1
            
print(mmax)
print(str(r) + " " + str(c))