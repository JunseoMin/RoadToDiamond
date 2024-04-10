import sys
input = sys.stdin.readline

word = {}
n,m = map(int,input().split())
'''
1.자주 나오는 단어일수록 앞에 배치한다.
2.해당 단어의 길이가 길수록 앞에 배치한다.
3.알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
'''
for _ in range(n):
    inw = input().strip()
    if len(inw) < m:
        continue
    
    tmp = word.get(inw,[0,len(inw),inw])
    tmp[0] += 1
    word[inw] = tmp
    
ans = sorted(word.items() , key = lambda x : (-x[1][0],-x[1][1],x[1][2]))

for s in ans:
    print(s[0])