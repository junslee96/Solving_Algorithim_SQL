def solution(numbers, k):
    num = (k-1)*2
    answer = numbers[num % len(numbers)]
    return answer