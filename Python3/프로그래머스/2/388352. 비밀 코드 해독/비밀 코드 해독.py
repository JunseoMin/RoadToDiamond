from itertools import combinations as comb

def solution(n, q, ans):
    sol = 0
    nums = [ i for i in range(1 , n + 1)]
    
    for passkey in comb(nums,5):
        valid = True
        for question,answer in zip(q,ans):
            cnt = 0
            if answer != len(set(question) & set(passkey)):
                valid = False
                break
                
        if valid:
            sol += 1
            
    return sol
