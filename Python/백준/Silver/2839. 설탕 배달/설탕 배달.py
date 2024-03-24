import sys
sys.setrecursionlimit(10000)

n = int(input())
redict = {}

def reculsive(remain):
    if remain in redict:
        return redict[remain]
        pass
    if remain < 0:
        return float('inf')
    if not remain:
        return 0
    redict[remain] = min(reculsive(remain-3),reculsive(remain-5)) + 1
    return redict[remain]
    
sol = reculsive(n)
print(sol if sol != float('inf') else -1)