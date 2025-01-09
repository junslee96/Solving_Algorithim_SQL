def solution(keyinput, board):
    # 딕셔너리로 이동 방향 정의
    directions={"up": (0, 1),"down": (0, -1),"left": (-1, 0),"right": (1, 0)}
    # 현재 좌표 초기화
    position=[0,0]
    # board에 따른 최대 이동 범위 계산
    x_limit=board[0]//2
    y_limit=board[1]//2
    # 키 입력에 따른 이동 처리
    for key in keyinput:
        if key in directions:
            dx,dy=directions[key]
            new_x=position[0]+dx
            new_y=position[1]+dy
            # 맵 경계 벗어나지 않도록 제한
            if -x_limit <= new_x <= x_limit:
                position[0] = new_x
            if -y_limit <= new_y <= y_limit:
                position[1] = new_y
    return position
