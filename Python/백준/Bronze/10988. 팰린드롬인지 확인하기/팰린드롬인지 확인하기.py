instr = input()

n = len(instr)
def sol():    
    for i in range(n):
        if not(instr[i] == instr[n-i-1]):
            print(0)
            return
    print(1)

sol()