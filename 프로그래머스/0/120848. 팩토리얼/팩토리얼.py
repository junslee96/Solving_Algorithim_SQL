def solution(n):
    num = 1
    answer = 1
    while num*(answer+1) <= n:
        answer += 1
        num *= answer
    return answer