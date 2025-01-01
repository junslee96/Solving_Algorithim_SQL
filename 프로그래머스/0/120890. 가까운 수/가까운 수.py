def solution(array, n):
    answer = 101
    result = 0
    for i in array:
        if abs(n - int(i)) < answer:
            answer = abs(n - int(i))
            result = int(i)
        elif abs(n - int(i)) == answer:
            if int(i) < result:
                result = int(i)
    return result
