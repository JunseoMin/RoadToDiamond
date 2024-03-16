import sys

input = sys.stdin.readline
a,b = map(int,input().split())

while a and b:
    i = 1
    if a > b:
        while 1:
            if b*i > a:
                print("neither")
                break
            
            if b*i == a:
                print("multiple")
                break

            i+=1    
    else:
        while 1:
            if b < a*i:
                print("neither")
                break
            
            if b == a*i:
                print("factor")
                break

            i+=1    
    
    
    a,b = map(int,input().split())
