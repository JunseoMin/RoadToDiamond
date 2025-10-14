def calcTime(start, end):
    st, sm = map(int, start.split(':'))
    et, em = map(int, end.split(':'))
    return (et * 60 + em) - (st * 60 + sm)

def splitMdy(mdy):
    if len(mdy) == 1:
        return [mdy]
    res = []
    N = len(mdy)
    for i in range(N - 1):
        if mdy[i] == '#':
            continue
        elif mdy[i + 1] == '#':
            res.append(mdy[i] + '#')
        else:
            res.append(mdy[i])
    if mdy[-1] != '#':
        res.append(mdy[-1])
    return res

def solution(m, musicinfos):
    answer = '(None)'
    candidates = []
    m = splitMdy(m)

    for idx, info in enumerate(musicinfos):
        start, end, name, melodyStr = info.split(',')
        time = calcTime(start, end)
        melodyTokens = splitMdy(melodyStr)
        N = len(melodyTokens)
        melodyFull = (melodyTokens * (time // N)) + melodyTokens[:time % N]

        for i in range(len(melodyFull) - len(m) + 1):
            if melodyFull[i:i+len(m)] == m:
                candidates.append((-len(melodyFull), idx, name))
                break

    candidates.sort()
    return candidates[0][2] if candidates else answer
