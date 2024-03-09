def solution(genres, plays):
    answer = []
    genre_dict = {}

    valuelist = []
    for i in range(len(plays)):
        genre_dict[genres[i]] = 0
        
    for i in range(len(plays)):
        genre_dict[genres[i]] += plays[i]
    
    genre_list = list(genre_dict.items())
    re_genre = []
    
    for _,value in genre_list:
        re_genre.append([value,_])
    re_genre.sort(reverse = True)
    
    num_genres_dict = {}
    
    for i in range(len(genres)):
        num_genres_dict[genres[i]] = []
    
    for i in range(len(genres)):
        tmp = num_genres_dict[genres[i]]
        tmp.append((plays[i],i))
        num_genres_dict[genres[i]] = tmp
        num_genres_dict[genres[i]].sort(reverse = True)
    
    for _,key in re_genre:
        if len(num_genres_dict[key]) == 1:
            answer.append(num_genres_dict[key][0][1])
        else:
            if num_genres_dict[key][0][0] == num_genres_dict[key][1][0]:
                answer.append(min(num_genres_dict[key][0][1],num_genres_dict[key][1][1]))
                answer.append(max(num_genres_dict[key][0][1],num_genres_dict[key][1][1]))
            else:
                answer.append(num_genres_dict[key][0][1])
                answer.append(num_genres_dict[key][1][1])

    return answer