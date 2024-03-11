n = int(input())

k = 2*n-1

for i in range(1,k,2):
    print(" " * int((k-i) / 2) + "*" * i)
for i in range(k,0,-2):
    print(" " * int((k-i) / 2) + "*" * i)