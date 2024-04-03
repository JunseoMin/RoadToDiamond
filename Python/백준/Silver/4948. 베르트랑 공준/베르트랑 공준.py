import sys
input = sys.stdin.readline

n = int(input())
while n:
    nums = [i for i in range(2*n +1)]
    nums[0] = 0;nums[1] = 0
    for i in range(2,2*n + 1):
        if not(nums[i]):
            continue
        
        for j in range(i*2,2*n + 1,i):
            nums[j] = 0
            
    tmp = nums[n+1:2*n+1]
    cnt = 0
    for i in tmp:
        if i:
            cnt += 1

    print(cnt)
    n = int(input())