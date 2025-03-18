def solution(n):
    # n × n 배열 초기화
    arr = [[0] * n for _ in range(n)]
    
    # 현재 위치와 방향
    x, y = 0, 0
    dx, dy = 0, 1  # 초기 방향은 오른쪽
    
    # 현재 숫자
    num = 1
    
    # 방문 여부를 표시할 배열
    visited = [[False] * n for _ in range(n)]
    
    while num <= n * n:
        # 현재 위치에 숫자 배치
        arr[x][y] = num
        visited[x][y] = True
        num += 1
        
        # 다음 위치로 이동
        nx, ny = x + dx, y + dy
        
        # 다음 위치가 범위를 벗어나거나 이미 방문한 경우 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
            dx, dy = dy, -dx  # 시계방향으로 방향 전환
            nx, ny = x + dx, y + dy
        
        # 다음 위치로 이동
        x, y = nx, ny
    
    return arr