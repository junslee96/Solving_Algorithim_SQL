def solution(str1, str2):
    length = len(str2) - len(str1) + 1
    for i in range(length):
        if str2[i:i+len(str1)] == str1:
            return 1
    return 0