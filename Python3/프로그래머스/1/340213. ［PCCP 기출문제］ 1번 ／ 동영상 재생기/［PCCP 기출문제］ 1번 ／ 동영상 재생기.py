def time2sec(time):
    return 60*int(time[:2]) + int(time[3:])

def sec2time(sec):
    return "{0:02d}:{1:02d}".format(int(sec/60),int(sec%60))

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    videoL   = time2sec(video_len)
    curr     = time2sec(pos)
    opS      = time2sec(op_start)
    opE      = time2sec(op_end)
    
    if opS <= curr and curr <= opE:
        curr = opE
    for command in commands:
        if command == 'prev':
            curr -= 10
        if command == 'next':
            curr += 10
        
        if curr < 0:
            curr = 0
        if curr > videoL:
            curr = videoL
        if opS <= curr and curr <= opE:
            curr = opE
    
    
    return sec2time(curr)