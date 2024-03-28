import sys
input = sys.stdin.readline
userdic = {}
n = int(input())
for _ in range(n):
    age,name = map(str,input().split())
    age = int(age)
    if age in userdic.keys():
        tmp = []
        tmp = userdic.get(age)
        tmp.append(name)
        userdic[age] = tmp
    else:
        userdic[age] = [name]
for age in sorted(userdic.keys()):
    for name in userdic[age]:
        print(str(age) + " " + name)