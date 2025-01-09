def solution(numbers):
    numbers.sort()
    plus_max=numbers[-1]*numbers[-2]
    minus_max=numbers[0]*numbers[1]
    if plus_max>minus_max:
        return plus_max
    else:
        return minus_max