def solution(board):
    n = len(board) # 행의 개수
    danger = set() # 중복 제거를 위한 집합(set)
    # i는 현재 행의 인덱스, row는 현재 행의 리스트
    for i, row in enumerate(board):
        # j는 열의 인덱스, x는 해당 위치의 값
        for j, x in enumerate(row):
            # 현재 위치가 0인 경우
            if not x:
                continue
            # 현재 위치가 1인 경우
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    new_i = i + di 
                    new_j = j + dj  
                    danger.add((new_i, new_j))
    # 위험 지역 위치가 board를 벗어나지 않을 경우를 모두 더해 필드의 크기에서 빼준다.
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
