n = int(input())

def reculsive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return reculsive(n-1) + reculsive(n-2)

print(reculsive(n))