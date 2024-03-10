import sys

ans = ""
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

input = sys.stdin.readline
instr = input()[:-1]

for a in alpha:
    if a in instr:
        ans += (str(instr.index(a)) + " ")
    else:
        ans += (str(-1) + " ")
        
print(ans[:-1])