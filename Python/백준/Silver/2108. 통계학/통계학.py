import sys
input = sys.stdin.readline

N = int(input())
nums = {}
numli = []
tmp = 0
for _ in range(N):
    n = int(input())
    nums[n] = nums.get(n,0) + 1
    numli.append(n)
    tmp += n

numli.sort()

print(round(tmp/N))
print(numli[N//2])

maxval = max(nums.values())
most = []

for k,v in nums.items():
    if v == maxval:
        most.append(k)
most.sort()
print(most[0] if len(most) == 1 else most[1])
print(numli[-1] - numli[0])