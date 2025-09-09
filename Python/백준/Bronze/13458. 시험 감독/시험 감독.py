import sys
input = sys.stdin.readline

N = int(input())    # Number of Testroom
A = list(map(int,input().split()))    # numer of applicant in i'th room
B,C = map(int,input().split()) # Master Avility, Becholar Avility

admins = [0 for _ in range(N)]

answer = 0

for i in range(N):
    nApplicants = A[i]
    if nApplicants == 0:
        continue
    if nApplicants - B < 0:
        answer += 1
    else:
        nApplicants -= B
        if nApplicants % C == 0:
            n = nApplicants // C
        else:
            n = (nApplicants // C) + 1
        answer += (1 + n)
print(answer)