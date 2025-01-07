def solution(n):
    answer = 0
    if n % (n**0.5) == 0:
        return 1
    else:
        return 2
        