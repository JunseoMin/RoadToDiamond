import sys
n = int(sys.stdin.readline())
line = 1

while n > line:
    n -= line
    line += 1

if line % 2:
    a = line - n + 1
    b = n
else:
    a = n
    b = line - n + 1

print(f'{a}/{b}')
