import sys 
input = sys.stdin.readline 
N,M = map(int,input().split()) 
r,c,d = map(int,input().split()) 
maps = [] 
dirs = [[-1,0],[0,1],[1,0],[0,-1]] # N E S W 
answer = 0 
for _ in range(N): 
    maps.append(list(map(int,input().split())))
    
while(True):
    if maps[r][c] == 0:
        answer += 1
        maps[r][c] = 10
    moved = False
    for dr,dc in dirs:
        if not moved and maps[r + dr][c + dc] == 0:
            while not moved:
                # Rotate CC
                d = (d+3)%4
                ddr,ddc = dirs[d]
                
                if maps[r + ddr][c + ddc] == 0:
                    r += ddr
                    c += ddc
                    moved = True
    if moved:
        continue
        
    dr,dc = dirs[d]
    
    if maps[r - dr][c - dc] == 1:
        break
    else:
        r -= dr
        c -= dc


print(answer)