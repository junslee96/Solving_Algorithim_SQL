def solution(numbers):
    list = sorted(numbers)
    answer = list[-1]*list[-2]
    return answer