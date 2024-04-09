import sys
n = int(input())

if not n:
    print(1)
    sys.exit()


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

print(factorial(n))
