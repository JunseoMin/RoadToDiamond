import sys
input = sys.stdin.readline

N,M,x,y,K = map(int,input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int,input().split())))
orders = list(map(int,input().split()))

curr = (x,y)
dice = {"u":0,"l":0,"e":0,"w":0,"s":0,"n":0}

for o in orders:
    r,c = curr
    
    if o == 1: #동쪽
        if c + 1 >= M:
            continue
            
        # Roll dice
        u,l,e,w,s,n = dice["u"],dice["l"],dice["e"],dice["w"],dice["s"],dice["n"]
        u,e,w,s,n = dice["u"], dice["e"], dice["w"], dice["s"], dice["n"]
        dice["l"] = e
        dice["u"] = w
        dice["e"] = u
        dice["w"] = l
        print(dice["u"])
        curr = (r,c+1)
        
    if o == 2: #서쪽
        if c - 1 < 0:
            continue
        # Roll dice
        u,l,e,w,s,n = dice["u"],dice["l"],dice["e"],dice["w"],dice["s"],dice["n"]
        
        dice["l"] = w
        dice["u"] = e
        dice["e"] = l
        dice["w"] = u
        print(dice["u"])
        curr = (r,c-1)
        
    if o == 3: #북쪽
        if r - 1 < 0:
            continue
        
        # Roll dice
        u,l,e,w,s,n = dice["u"],dice["l"],dice["e"],dice["w"],dice["s"],dice["n"]
        
        dice["l"] = n
        dice["u"] = s
        dice["n"] = u
        dice["s"] = l
        print(dice["u"])
        curr = (r-1,c)
    if o == 4: #남쪽
        if r + 1 >= N:
            continue
        # Roll dice
        u,l,e,w,s,n = dice["u"],dice["l"],dice["e"],dice["w"],dice["s"],dice["n"]
        
        dice["l"] = s
        dice["u"] = n
        dice["n"] = l
        dice["s"] = u
        print(dice["u"])        
        curr = (r+1,c)    
    nr,nc = curr
    if maps[nr][nc] == 0:
        maps[nr][nc] = dice["l"]
    else:
        dice["l"] = maps[nr][nc]
        maps[nr][nc] = 0
        