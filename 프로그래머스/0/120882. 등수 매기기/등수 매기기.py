def solution(score):
    # 평균 점수를 계산
    averages = [sum(s) / len(s) for s in score]
    # 내림차순 정렬된 순위를 구한 후 원래 순서대로 등수 반환
    sorted_indices = sorted(range(len(averages)), key=lambda i: -averages[i])
    ranks = [0] * len(score)
    for rank, idx in enumerate(sorted_indices, start=1):
        if rank > 1 and averages[sorted_indices[rank - 2]] == averages[idx]:
            ranks[idx] = ranks[sorted_indices[rank - 2]]  # 동일한 점수는 동일 등수
        else:
            ranks[idx] = rank
    return ranks
