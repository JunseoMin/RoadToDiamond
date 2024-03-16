n = int(input())

while n>0:
    yaksu = [1,]
    
    for i in range(2,n):
        if not n%i:
            yaksu.append(i)
            
    if sum(yaksu) == n:
        print("{} = ".format(n) +" + ".join([str(y) for y in yaksu]))
    else:
        print("{} is NOT perfect.".format(n))
        
    n = int(input())