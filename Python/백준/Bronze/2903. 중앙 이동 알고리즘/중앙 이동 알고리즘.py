from math import pow
n = int(input())

def reculsive(row_before=2,i=0):
    if i == n:
        print(int(pow(row_before,2)))
        return
    
    return reculsive((row_before * 2) - 1,i+1)

reculsive()