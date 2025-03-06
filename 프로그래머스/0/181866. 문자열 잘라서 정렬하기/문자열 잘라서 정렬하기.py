def solution(myString):
    result = []
    myString_split = myString.split('x')
    myString_split.sort()
    for s in myString_split:
        if s:
            result.append(s)
    return result