import sys
s1,s2 = map(str,sys.stdin.readline().split())
print(max(int(s1[2]+s1[1]+s1[0]),int(s2[2]+s2[1]+s2[0])))