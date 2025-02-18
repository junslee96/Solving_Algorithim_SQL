def solution(a, b, c, d):
    dice = sorted([a, b, c, d])
    
    # 네 주사위의 숫자를 리스트로 정렬
    if dice[0] == dice[3]:
        return 1111 * dice[0]
    
    # 네 숫자가 모두 같은 경우
    if dice[0] == dice[2] or dice[1] == dice[3]:
        p = dice[1]
        q = dice[0] if dice[0] != p else dice[3]
        return (10 * p + q) ** 2
    
    # 세 숫자가 같고 나머지 하나가 다른 경우
    if dice[0] == dice[1] and dice[2] == dice[3]:
        p = dice[0]
        q = dice[2]
        return (p + q) * abs(p - q)
    
    # 두 개씩 같은 값이 나온 경우
    if dice[0] == dice[1]:
        return dice[2] * dice[3]
    elif dice[1] == dice[2]:
        return dice[0] * dice[3]
    elif dice[2] == dice[3]:
        return dice[0] * dice[1]
    
    # 네 숫자가 모두 다른 경우
    return dice[0]