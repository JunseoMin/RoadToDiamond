import sys
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def reduce_fraction(numerator, denominator):
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor

a, b = map(int, input().split())
c, d = map(int, input().split())

gbs = lcm(b, d)
result = a * gbs // b + c * gbs // d

result, gbs = reduce_fraction(result, gbs)

print(f"{result} {gbs}")
