def solution(myString, pat):
    result = ""
    for c in myString:
        if c == 'A':
            result += 'B'
        else:
            result += 'A'
    if pat in result:
        return 1
    else:
        return 0
