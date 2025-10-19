def solution(citations):
    citations.sort(reverse = True)
    N = len(citations)
    for i in range(N):
        if citations[i] <= i + 1:
            return max(citations[i], i)
    return N