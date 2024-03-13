slist = [[''] for _ in range(15)]
ans = ""
for _ in range(5):
    instr = input()
    for i in range(len(instr)):
        slist[i][0] = slist[i][0]+instr[i]

for i in range(len(slist)):
    ans+=slist[i][0]
    
print(ans)