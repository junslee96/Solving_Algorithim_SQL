def solution(s):
    s_count = {}
    for i in s:
        if i in s_count:
            s_count[i] += 1
        else:
            s_count[i] = 1
    answer = [i for i, count in s_count.items() if count ==1]
    answer.sort()
    return ''.join(answer)