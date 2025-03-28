def solution(genres, plays):
    genre_dict = {}
    for i, (genre, play) in enumerate(zip(genres,plays)):
        if genre not in genre_dict:
            genre_dict[genre] = []
        genre_dict[genre].append((i,play))
        
    genre_total = {genre: sum(play for _, play in songs) for genre, songs in genre_dict.items()}
    
    sorted_genres = sorted(genre_total, key=lambda x: genre_total[x], reverse = True)
    
    result = []
    for genre in sorted_genres:
        songs = sorted(genre_dict[genre], key=lambda x: (-x[1],x[0]))
        result.extend([song[0] for song in songs[:2]])
        
    return result