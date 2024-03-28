import sys
input = sys.stdin.readline
n = int(input())
words = []
for _ in range(n):
    instr = input().strip()
    inst_len = len(instr)
    if not [inst_len,instr] in words:
        words.append([inst_len,instr])
        

words.sort()
for i in range(len(words)):
    print(words[i][1])