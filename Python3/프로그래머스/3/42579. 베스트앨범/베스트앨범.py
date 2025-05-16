from collections import defaultdict

def solution(genres, plays):
    answer = []
    songs = []

    genredict = defaultdict(list)
    
    for i in range(len(genres)):
        song = {"genre":genres[i], "played":plays[i]}
        songs.append(song)
    
    for i in range(len(songs)):
        genredict[songs[i]["genre"]].append((songs[i]["played"],i))
    
    genre = defaultdict(list)
    genli = []
    for k,v in genredict.items():
        s = 0
        for n in v:
            s += n[0]
        genli.append((s,k))
        
        v.sort(reverse = True)
        genre[k].append(v[0])
        if len(v) >= 2:
            genre[k].append(v[1])
        
    genli.sort(reverse = True)
    # print(genre)
    
    for _,tarGanre in genli:
        if len(genre[tarGanre]) >= 2:
            if genre[tarGanre][0][0] == genre[tarGanre][1][0]:
                answer.append(genre[tarGanre][1][1])
                answer.append(genre[tarGanre][0][1])
            else:
                answer.append(genre[tarGanre][0][1])
                answer.append(genre[tarGanre][1][1])
        else:
            answer.append(genre[tarGanre][0][1])
        
    return answer