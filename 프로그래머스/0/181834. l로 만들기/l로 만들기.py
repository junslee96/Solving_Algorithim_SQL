def solution(myString):
    result = ''
    for x in myString:
        if ord(x) < ord('l'):
            result += 'l'
        else:
            result += x
    return result