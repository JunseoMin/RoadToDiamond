import sys
input = sys.stdin.readline

def reculsive(inst,n):
    # print(inst)
    if n == 1:
        return inst
    return reculsive(inst[0:n//3],n//3) +" "*(n//3) + reculsive(inst[0:n//3],n//3)

while 1:
    try:
        N = 3**int(input())
        print(reculsive('-' * N, N))
    except:
        sys.exit()