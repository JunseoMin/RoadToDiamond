from itertools import combinations as comb
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        combos = []
        for order in orders:
            combos += comb(sorted(order), c)
        counter = Counter(combos)
        if not counter:
            continue
        max_count = max(counter.values())
        if max_count >= 2:
            for k, v in counter.items():
                if v == max_count:
                    answer.append(''.join(k))
    return sorted(answer)
