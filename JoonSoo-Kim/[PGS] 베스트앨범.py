def solution(genres, plays):
    answer = []

    # 장르 종류 찾기
    genres_type = set()
    for g in genres:
        genres_type.add(g)
    genres_type = list(genres_type)

    # 노래, 장르별 재생횟수 정리
    songs = []
    genres_num = [0] * len(genres_type)
    for i in range(len(genres)):
        songs.append([genres[i], plays[i], i])
        genres_num[genres_type.index(genres[i])] += plays[i]

    # 장르 종류를 재생 횟수 별로 정렬
    genres_type_temp = []
    while genres_num != []:
        index = genres_num.index(max(genres_num))
        genres_type_temp.append(genres_type[index])
        del genres_type[index]
        del genres_num[index]
    genres_types = genres_type_temp

    for genre in genres_types:
        # 해당 장르의 song list 생성
        song_list = []
        for song in songs:
            if song[0] == genre:
                song_list.append(song)
        # song list를 play로 정렬
        song_list.sort(key=lambda x: x[1], reverse=True)
        # song이 1개인 경우 예외처리
        if len(song_list) == 1:
            answer.append(song_list[0][2])
        else:
            answer.append(song_list[0][2])
            answer.append(song_list[1][2])

    return answer