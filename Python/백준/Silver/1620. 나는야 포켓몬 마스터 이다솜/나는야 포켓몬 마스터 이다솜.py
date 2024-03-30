import sys
input = sys.stdin.readline
n,m = map(int,input().split())
idxkey = {};strkey = {}

for i in range(n):
    name = input().strip()
    idxkey[i+1] = name
    strkey[name] = i+1
    
for j in range(m):
    question = input().strip()

    if question in strkey.keys():
        print(strkey[question])
    else:
        print(idxkey[int(question)])