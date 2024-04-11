import sys
input = sys.stdin.readline


def recursion(s, l, r,cnt):
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1,cnt)

def isPalindrome(s):
    cnt = 0    
    return recursion(s, 0, len(s)-1,cnt)

N = int(input())

for _ in range(N):
    inst = input().strip()
    ans1,ans2 = isPalindrome(inst)
    print(str(ans1)+' '+str(ans2))