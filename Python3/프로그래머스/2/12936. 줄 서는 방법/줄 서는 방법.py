def factorial(n):
    
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def solution(n, k):
    answer = []
    nums = [i for i in range(1,n+1)]
    
    for L in range(n,0,-1):
        F = factorial(L-1)
        N = (k // F) + 1 if k % F else k // F
        k %= F
        answer.append(nums.pop(N-1))
    
    return answer