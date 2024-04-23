import sys

nli = list(map(int,input().split()))
if nli == [1,2,3,4,5,6,7,8]:
    print("ascending")
    sys.exit()
if nli == [8,7,6,5,4,3,2,1]:
    print("descending")
    sys.exit()
print("mixed")
        