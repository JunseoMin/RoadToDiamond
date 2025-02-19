from math import ceil

def solution(progresses, speeds):
    answer = []
    costs = []
    for p,s in zip(progresses, speeds):
        cost = ceil((100 - p) / s)
        costs.append(cost)
    
    curr = costs[0]
    fin = 1
    for i in range(1,len(costs)):
        if curr >= costs[i]:
            fin += 1
        else:
            answer.append(fin)
            fin = 1
            curr = costs[i]
    answer.append(fin)
    
    return answer