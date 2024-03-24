import sys
n = int(input()) - 1

if not n:
    print(666)
    sys.exit()
    
sixs = "666"; i=0
num = 666
while 1:  
    num += 1
    if sixs in str(num):
        i+=1
        if i == n:
            print(num)
            sys.exit()
    
'''
666    0

1666    1 
2666    2
3666    3
4666    4
5666    5
--5
6660    6
6661    7
6662    8
6663    9
6664    10
6665    11
6666    12
--7
10666
26666
36666
46666
56666
----5
66660
66661
66662
66663
66664
66665
66666
----7
'''