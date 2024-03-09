import sys

input = sys.stdin.readline
st_list = [i for i in range(1,31)]

for _ in range(28):
    st_list.remove(int(input()))

print(min(st_list))
print(max(st_list))