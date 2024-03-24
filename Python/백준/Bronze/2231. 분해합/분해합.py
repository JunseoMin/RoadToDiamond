n = int(input())
c_list = []
for m in range(n):
    tmp = 0
    sm = str(m)
    for s in sm:
        tmp += int(s)
    if n == tmp + m:
        c_list.append(m)
        
print(min(c_list) if len(c_list) else 0)