def solution(l, r):
    result = []
    for num in range(l,r+1):
        if all(digit in '05' for digit in str(num)):
            result.append(num)
    return result if result else [-1]
