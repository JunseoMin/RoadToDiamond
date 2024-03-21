x = []
y = []
x1=0
y1=0
for _ in range(3):
    _x,_y = map(int,input().split())
    x.append(_x)
    y.append(_y)
    
    if _ == 2:
        if x.count(_x) == 2:
            x.remove(_x)
            x.remove(_x)
            x1 = x[0]
        else:
            x1 = _x
            
        if y.count(_y) == 2:
            y.remove(_y)
            y.remove(_y)
            y1 = y[0]
        else:
            y1 = _y
print(" ".join([str(x1),str(y1)]))