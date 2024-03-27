n = input()
nli = [n[i] for i in range(len(n))]
nli.sort(reverse = True)
tmp = ""
for i in nli:
    tmp += i
print(tmp)