n = int(input())
nlist = []
for _ in range(n):
    nlist.append(int(input()))
nlist.sort()
for k in nlist:
    print(k)