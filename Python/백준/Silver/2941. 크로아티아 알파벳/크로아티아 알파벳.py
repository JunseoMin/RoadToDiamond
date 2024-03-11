instr = input()

alphas = ['c=','c-','dz=','d-','lj','nj','s=','z=']
tmp = 0
for ca in alphas:
    tmp += instr.count(ca)

print(len(instr) - tmp)