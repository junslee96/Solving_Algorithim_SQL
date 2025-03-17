def solution(picture, k):
    result = []
    array = ""
    for arr in picture:
        for i in arr:
            array += i*k
        result += [array]*k
        array = ""
    return result