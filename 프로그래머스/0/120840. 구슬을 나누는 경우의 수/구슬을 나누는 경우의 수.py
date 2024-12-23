def solution(balls, share):
    numer = 1
    denom = 1
    for i in range(balls,balls - share, -1):
        numer *= i
    for i in range(1,share + 1):
        denom *= i
    answer = numer//denom
    return answer