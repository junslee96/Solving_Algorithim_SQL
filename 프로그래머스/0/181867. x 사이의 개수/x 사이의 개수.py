def solution(myString):
    myString_split = myString.split('x')
    result = []
    for str in myString_split:
        result.append(len(str))
    return result