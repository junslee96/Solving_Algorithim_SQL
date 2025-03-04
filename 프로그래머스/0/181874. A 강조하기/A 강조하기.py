def solution(myString):
    result = ""
    for char in myString:
        if char == 'a' or char == 'A':
            result += 'A'
        elif 'B' <= char <= 'Z':
            result += char.lower()
        else:
            result += char
    return result