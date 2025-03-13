def solution(str_list, ex):
    answer = ''
    for num in str_list:
        if ex not in num:
            answer += num
    return answer