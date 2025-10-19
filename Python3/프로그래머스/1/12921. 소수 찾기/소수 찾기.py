def solution(n):
    answer = 0
    nums = [True for _ in range(n+1)]
    nums[0] = nums[1] = False
    for i in range(2,n+1):
        if nums[i] == True:
            for j in range(2*i,n+1,i):
                nums[j] = False
    
    for v in nums:
        if v:
            answer +=1
    
    return answer