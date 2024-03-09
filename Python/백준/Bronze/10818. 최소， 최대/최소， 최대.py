import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))

print(str(min(n_list)) + " " + str(max(n_list)))    