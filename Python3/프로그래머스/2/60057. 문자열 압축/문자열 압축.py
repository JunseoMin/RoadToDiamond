def solution(s):
    N = len(s)
    answer = N
    
    for l in range(1,N//2 + 1):
        # if N % l != 0:  #안나누어지면 skip
        #     continue
        
        string = ""
        tmp = []
        
        for i in range(0,N,l):
            tmp.append(s[i:i+l])
        # print(tmp)
        while tmp:
            c = tmp.pop(0)
            cnt = 1
            for v in tmp:
                if v == c:
                    cnt += 1
                else:
                    break
            tmp = tmp[cnt-1:]
            if cnt != 1:
                string += (str(cnt) + c)
            else:
                string += c
        # print(string)
        answer = min(answer,len(string))
    
    return answer