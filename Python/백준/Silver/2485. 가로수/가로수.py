from math import gcd
N = int(input())
m = int(input())

ini = m
gaps = set()
gli = []
for _ in range(N-1):
    n = int(input())
    gap = n - m
    gaps.add(gap)
    gli.append(gap)
    m = n

gaps = list(gaps)
_gcd = gaps[0]

for g in gaps:
    _gcd = gcd(_gcd,g)

cnt = ((m - ini) // _gcd) + 1

print(cnt - N)