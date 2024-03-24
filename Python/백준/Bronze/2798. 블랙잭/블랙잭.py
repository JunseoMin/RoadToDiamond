n,m = map(int,input().split())
n_list = list(map(int,input().split()))
sumlist = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum =n_list[i]+n_list[j]+n_list[k]
            if sum <= m:
                sumlist.append(sum)
                        
print(max(sumlist))