import math

_min, _max = map(int, input().split())

tmp = [True] * (_max - _min + 1)

for i in range(2, int(math.sqrt(_max)) + 1):
    squared = i ** 2
    start = _min // squared
    if start * squared < _min:
        start += 1
    for j in range(start, (_max // squared) + 1):
        idx = squared * j - _min
        if idx >= 0 and idx < len(tmp):
            tmp[idx] = False

count = sum(1 for x in tmp if x)

print(count)
