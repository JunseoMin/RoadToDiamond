def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        idx = -1
        for i in range(len(progresses)):
            if progresses[i] < 100:
                break
            idx = i
        if idx != -1:
            answer.append(idx + 1)
            progresses = progresses[idx+1:]
            speeds = speeds[idx+1:]
    return answer