from collections import defaultdict

def solution(participant, completion):
    answer = ''
    maratone = defaultdict(int)
    
    for parti in participant:
        maratone[parti] += 1
    
    for comp in completion:
        maratone[comp] -= 1
    
    for key,val in maratone.items():
        if val != 0: return key
    
