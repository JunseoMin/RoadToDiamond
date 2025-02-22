def solution(num_list):
    answer = -1
    
    if len(num_list) <= 10:
        answer = 1
        for n in num_list:
            answer *= n
    else:
        answer = 0
        for n in num_list:
            answer += n
    
    return answer