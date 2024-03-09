import sys
input = sys.stdin.readline
n = int(input())
score_l = list(map(int,input().split()))
tmp = 0
s_max = max(score_l)
for i in range(n):
    tmp += (score_l[i]/s_max)*100

print(tmp/n)