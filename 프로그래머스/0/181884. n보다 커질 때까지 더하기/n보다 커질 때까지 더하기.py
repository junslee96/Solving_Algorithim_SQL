def solution(numbers, n):
    sum = 0
    i = 0
    while sum <= n:
        sum += numbers[i]
        i += 1
    return sum