ll = list(map(int,input().split()))

if sum(ll) - max(ll) > max(ll):
    print(sum(ll))
else:
    print(2*(sum(ll)-max(ll))-1)