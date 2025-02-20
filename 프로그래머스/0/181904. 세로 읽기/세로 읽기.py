def solution(my_string, m, c):
    answer = ''
    for i in range(0,len(my_string),m):
        if i + c - 1 < len(my_string):
            answer += my_string[i + c - 1]
    return answer
