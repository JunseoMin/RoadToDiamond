N = int(input())
f1 = 0
f2 = 0
def fib1(n):
    global f1
    if n ==1 or n == 2:
        f1 += 1
        return 1
    return fib1(n-1) + fib1(n-2)

def fib2(n,f = [0] * 100000000):
    f[1] = f[2] = 1
    global f2
    for i in range(3,n+1):
        f2+=1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

fib1(N)
fib2(N)
print(str(f1) + " " + str(f2))