def solution(board):
    n = len(board)  # 행 크기
    m = len(board[0])  # 열 크기
    danger_zone = [[0] * m for _ in range(n)]  # 위험 지역 표시
    
    # 방향 벡터: 상, 하, 좌, 우, 대각선 8방향
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # 상, 하, 좌, 우
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # 좌상, 우상, 좌하, 우하
    ]
    
    # 지뢰 주변 지역을 위험 지역으로 표시
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:  # 지뢰인 경우
                danger_zone[i][j] = 1  # 현재 위치 위험 지역으로 설정
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:  # 지도 내에 있는 경우만 처리
                        danger_zone[nx][ny] = 1
    
    # 안전 지역 계산
    safe_count = 0
    for i in range(n):
        for j in range(m):
            if danger_zone[i][j] == 0:  # 위험 지역이 아니면 안전 지역
                safe_count += 1
    
    return safe_count
