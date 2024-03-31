from math import gcd
n = int(input())
m = int(input())

ini = m
gaps = set()
gli = []
for _ in range(n-1):
    _n = int(input())
    gap = _n - m
    gaps.add(gap)
    gli.append(gap)
    m = _n

gaps = list(gaps)
_gcd = gaps[0]

for g in gaps:
    _gcd = gcd(_gcd,g)

ans = 0
for _g in gli:
    ans += _g // _gcd - 1

print(ans)