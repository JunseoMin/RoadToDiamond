tmp = 1
for _ in range(3):
    tmp *= int(input())
tmp = str(tmp)
for n in range(10):
    print(tmp.count(str(n)))