N = int(input())

nli = sorted(list(map(int,input().split())))

if not N%2:
    print(nli[0]*nli[-1])
else:
    print(nli[N//2]**2)