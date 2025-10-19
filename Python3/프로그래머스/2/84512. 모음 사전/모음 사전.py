def solution(word):
    answer = 1
    chars = ["A","E","I","O","U"]
    dictionary = []
    for v1 in chars:
        dictionary.append(v1)
        for v2 in chars:
            dictionary.append(v1 + v2)
            for v3 in chars:
                dictionary.append(v1 + v2 + v3)
                for v4 in chars:
                    dictionary.append(v1 + v2 + v3 + v4)
                    for v5 in chars:
                        dictionary.append(v1 + v2 + v3 + v4 + v5)
        
    return dictionary.index(word) + 1