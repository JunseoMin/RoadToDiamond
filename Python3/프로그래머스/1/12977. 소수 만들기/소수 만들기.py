from itertools import combinations

def getPrimes(n):
    primes = [True for i in range(n+1)]
    primes[0] = False; primes[1] = False; primes[2] = True;
    
    for i in range(2,len(primes)):
        if primes[i]:
            for j in range(i,n+1,i):
                if i == j:
                    continue
                primes[j] = False
    return primes
    

def solution(nums):
    answer = 0
    picks = combinations(nums,3)
    
    for pick in picks:
        n = pick[0] + pick[1] + pick[2]
        primes = getPrimes(n)
        if primes[n]: answer += 1
    
    return answer