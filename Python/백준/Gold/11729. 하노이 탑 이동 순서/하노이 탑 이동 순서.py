import sys
input = sys.stdin.readline

N = int(input())
tmp = 0

def reculsive(n,from_,sub_,to_,nli = []):

    if n == 1:
        nli.append([str(from_) ,str(to_) ])
        return nli
    
    reculsive(n-1,from_,to_,sub_,nli)
    nli.append([str(from_ ),str(to_) ])
    reculsive(n-1,sub_,from_,to_,nli)
    return nli

ans = reculsive(N,1,2,3)

print(len(ans))
for path in ans:
    print(' '.join(path))