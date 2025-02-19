def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        substr = str[s:s+l]
        if int(substr) > k:
            answer.append(int(substr))
    return answer