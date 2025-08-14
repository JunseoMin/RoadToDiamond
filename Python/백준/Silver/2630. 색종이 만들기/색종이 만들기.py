import sys
input = sys.stdin.readline

def check(p):
    if len(p) == 1:
        return True
    
    prev = p[0][0]
    for l in p:
        for v in l:
            if not (prev == v):
                return False
            prev = v
    return True

def divide(p, div):
    top = p[:div]
    bottom = p[div:]
    
    d1 = [row[:div] for row in top]
    d2 = [row[div:] for row in top]
    d3 = [row[div:] for row in bottom]
    d4 = [row[:div] for row in bottom]
    
    return [d1, d2, d3, d4]

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

w = 0
b = 0
div = N
papers = [paper]

while papers:
    tmp = []
    div = div // 2
    for p in papers:
        # print(p)
        if check(p):  # If paper contains same color
            if p[0][0]:
                b += 1
            else:
                w += 1
        else:
            # If contains different color → Divide
            dp = divide(p, div)
            tmp.extend(dp)
    papers = tmp

print(w)
print(b)
