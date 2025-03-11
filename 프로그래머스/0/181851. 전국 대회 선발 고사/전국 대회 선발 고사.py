def solution(rank, attendance):
    # 등수와 인덱스(번호) 저장
    true_rank = [(r,i) for i, (r, a) in enumerate(zip(rank,attendance)) if a]
    # 등수를 불러와 정렬
    true_rank.sort(key=lambda x: x[0])
    # 등수 상위 3명만 번호 저장
    a,b,c = [x[1] for x in true_rank[:3]]
    return 10000*a+100*b+c
    