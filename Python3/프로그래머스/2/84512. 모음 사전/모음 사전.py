import itertools

def solution(word):
    answer = 0
    words = ['A','E','I','O','U']
    
    dictionary = []
    
    for i in range(1,6):
        alphas = itertools.product(words,repeat = i)
        for tup in alphas:
            w = ""
            for a in tup:
                w += a
            dictionary.append(w)
        
    dictionary.sort()
    return dictionary.index(word) + 1
    
    