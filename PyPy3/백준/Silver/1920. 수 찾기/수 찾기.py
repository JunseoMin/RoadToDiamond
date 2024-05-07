import sys

input = sys.stdin.readline

N = int(input())
nli = sorted(list(map(int, input().split())))
M = int(input())


def BS(s_idx, e_idx, n):
    if e_idx >= s_idx:
        mid = s_idx + (e_idx - s_idx) // 2
        if nli[mid] == n:
            return 1
        elif nli[mid] > n:
            return BS(s_idx, mid - 1, n)
        else:
            return BS(mid + 1, e_idx, n)
    else:
        return 0


for i in list(map(int, input().split())):
    result = BS(0, N - 1, i)
    print(result)
