def solution(lines):
    overlap_set = set()  # 두 선분 이상 겹치는 좌표
    all_points = set()   # 모든 선분이 지나가는 좌표

    for start, end in lines:
        # 각 선분의 모든 좌표를 추가
        for point in range(start, end):
            if point in all_points:  
                # 이미 지나간 좌표인 경우
                overlap_set.add(point)
            else:
                all_points.add(point)
    return len(overlap_set)

