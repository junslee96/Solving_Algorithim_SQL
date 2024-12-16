def solution(n):
    answer = 0
    # 1~7 : 1판, 8~14 : 2판
    if n%7 == 0:
        answer = n//7
    else:
        answer = n//7 +1
    return answer

   